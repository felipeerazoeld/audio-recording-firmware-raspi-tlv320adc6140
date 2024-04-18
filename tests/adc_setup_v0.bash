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

#sc_set() {
#    i2cset -f -y -m $3 $i2cbus $i2caddr $1 $2
#    sleep 0.002
#}

# SW Reset
sc_set 0x01 0x01 0x01
sleep 0.02

# Get wake status
i2cget -f -y $i2cbus $i2caddr 0x02

# DSP Config
bin2hex 00000000
v=$r #
bin2hex 11111000
m=$r #
sc_set 0x6C $v $m

# ---- Configure channels

# Configure the desired channel gain setting before powering up the ADC channel and do not change this setting while the ADC is powered on. The programmable range supported for each channel gain is from 0 dB to 42 dB in steps of 1 dB.

bin2hex 00110000
sv=$r # channel settings value
bin2hex 11111101
sm=$r # channel settings mask

int2hex 42 2 # int representing gain in dB, shift left 2
gv=$r # channel gain value
bin2hex 11111100
gm=$r # channel gain mask

echo "$gv & $gm"

# CH1
# Settings
sc_set 0x3C $sv $sm
# Gain
# 3D A8
# 42db = 42 = 101010 = 2A << 2 = A8
# write only 6 bits from 1-7 (-m 0xFC = 11111100)
sc_set 0x3D $gv $gm

# CH2
sc_set 0x41 $sv $sm
sc_set 0x42 $gv $gm

# CH3
sc_set 0x46 $sv $sm
sc_set 0x47 $gv $gm

# CH4
sc_set 0x4b $sv $sm
sc_set 0x4c $gv $gm


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


# Power-up ADC, MICBIAS and PLL by I2C write into P0_R117  
# 75 E0
sc_set 0x75 0xE0 $nomask

