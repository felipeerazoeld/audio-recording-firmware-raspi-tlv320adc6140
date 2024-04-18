#!/bin/sh

. ticktick.sh
DATA=`cat settings.json`
tickParse "$DATA"

i2caddr=``HW["adc_addr"]``
i2cbus=``HW["i2c_bus"]``

echo "i2caddr: $i2caddr"
echo "i2cbus: $i2cbus"

# Helpers
r=0
bin2hex() {
    i=$(echo $1)
    h=$(echo "obase=16;ibase=2;$i" | bc)
    r=$(echo 0x$h)
}
int2hex() {
    i=$(($1 << $2))
    b=$(echo "obase=2;$i" | bc)
    bin2hex $b
}

nomask=0xff
sc_set() {
    i2cset -f -y -m $3 $i2cbus $i2caddr $1 $2
    sleep 0.002
}

# SW Reset
sc_set 0x01 0x01 0x01
sleep 0.02

# Get wake status
i2cget -f -y $i2cbus $i2caddr 0x02

# DSP Config
bin2hex 00001000
v=$r #
bin2hex 11111000
m=$r #
sc_set 0x6C $v $m

# ---- Configure channels

# Configure the desired channel gain setting before powering up the ADC channel and do not change this setting while the ADC is powered on. 
# The programmable range supported for each channel gain is from 0 dB to 42 dB in steps of 1 dB.

#bin2hex 00100001  # this is with AGC/DRE enabled
bin2hex 00100000  # this is with AGC/DRE disabled, only static gain
sv=$r # channel settings value, see page 81 datasheet for example
bin2hex 11111101
sm=$r # channel settings mask, see page 81 datasheet for example

int2hex 35 2 # int representing gain in dB, shift left 2
gv=$r # channel gain value
bin2hex 11111100
gm=$r # channel gain mask

echo "$gv & $gm"

int2hex 205 0 # int representing digital volume in dB, shift left 0, for detail see page 82
dvv=$r # channel vol value
bin2hex 11111111
dvm=$r # channel vol mask

# CH1
sc_set 0x3C $sv $sm
sc_set 0x3D $gv $gm
sc_set 0x3E $dvv $dvm

# CH2
sc_set 0x41 $sv $sm
sc_set 0x42 $gv $gm
sc_set 0x43 $dvv $dvm

#int2hex 10 2  #uncomment to change gain in channel 2
#sc_set 0x42 $r $gm

# CH3
sc_set 0x46 $sv $sm
sc_set 0x47 $gv $gm
sc_set 0x48 $dvv $dvm

# CH4
sc_set 0x4b $sv $sm
sc_set 0x4c $gv $gm
sc_set 0x4d $dvv $dvm

# --- Wake and poweron

# Wake-up device by I2C write into P0_R2 using internal AREG  
# 02 81
sc_set 0x02 0x81 $nomask

# Enable Input Ch-1 to Ch-4 by I2C write into P0_R115  
# 73 F0  
sc_set 0x73 0xF0 $nomask

# Enable ASI Output Ch-1 to Ch-4 slots by I2C write into P0_R116  
# 74 F0
sc_set 0x74 0xF0 $nomask
#sc_set 0x1e 0x82 $nomask

#ASI General Config
#bin2hex 01110000   #look at page 65 
#sc_set 0x07 $r $nomask

#ASI channels 1 to 4, look at page 66 to 68
bin2hex 01111111 #ASI registers mask, as specified in datasheet
asi_m=$r

int2hex 0 0 #configure to TDM slot 0
sc_set 0x0b $r $asi_m

int2hex 1 0 #configure to TDM slot 1
sc_set 0x0c $r $asi_m

int2hex 2 0 #configure to TDM slot 3
sc_set 0x0d $r $asi_m

int2hex 3 0 #configure to TDM slot 4
sc_set 0x0e $r $asi_m

#AGC Configuration
#int2hex 2 4 #desired output signal at -10dB
#outs=$r
#int2hex 7 0 #max gain configures for 30dB
#mxg=$r
#agc=$((outs+mxg))
#sc_set 0x70 $agc $nomask
#echo "$mxg, $outs"
#printf "0x%X\n" $agc

#DSP? >> worked?!?
#sc_set 0x6c 48 $nomask

#Clock Configuration
sc_set 0x15 0x67 $nomask
#sc_set 0x04 0x40 $nomask

#M Divider En/Dis
#sc_set 0x1f 0xc0 $nomask

# Power-up ADC, MICBIAS and PLL by I2C write into P0_R117  
bin2hex 01100100 # look at page 97
pwrv=$r
bin2hex 11111100
pwrm=$r
sc_set 0x75 $pwrv $pwrm
#sc_set 0x75 0xE0 $nomask #old
