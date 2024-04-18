from smbus import SMBus
import json
# Opening JSON file
f = open('settings.json')
data = json.load(f)
f.close()
#
i2c = SMBus(int(data['HW']['i2c_bus']))
adc_i2c_address = int( data['HW']['adc_addr'],0)
debug=bool(data['HW']['debug'])
#
mp = {
	"ADCX140_PAGE_SELECT" 		: 0x00,
	"ADCX140_SW_RESET" 			: 0x01,
	"ADCX140_SLEEP_CFG" 		: 0x02,
	"ADCX140_SHDN_CFG" 			: 0x05,
	"ADCX140_ASI_CFG0" 			: 0x07,
	"ADCX140_ASI_CFG1" 			: 0x08,
	"ADCX140_ASI_CFG2" 			: 0x09,
	"ADCX140_ASI_CH1" 			: 0x0b,
	"ADCX140_ASI_CH2" 			: 0x0c,
	"ADCX140_ASI_CH3" 			: 0x0d,
	"ADCX140_ASI_CH4" 			: 0x0e,
	"ADCX140_ASI_CH5" 			: 0x0f,
	"ADCX140_ASI_CH6" 			: 0x10,
	"ADCX140_ASI_CH7" 			: 0x11,
	"ADCX140_ASI_CH8" 			: 0x12,
	"ADCX140_MST_CFG0" 			: 0x13,
	"ADCX140_MST_CFG1" 			: 0x14,
	"ADCX140_ASI_STS" 			: 0x15,
	"ADCX140_CLK_SRC" 			: 0x16,
	"ADCX140_PDMCLK_CFG" 		: 0x1f,
	"ADCX140_PDM_CFG" 			: 0x20,
	"ADCX140_GPIO_CFG0" 		: 0x21,
	"ADCX140_GPO_CFG0" 			: 0x22,
	"ADCX140_GPO_CFG1"			: 0x23,
	"ADCX140_GPO_CFG2"			: 0x24,
	"ADCX140_GPO_CFG3"			: 0x25,
	"ADCX140_GPO_VAL" 			: 0x29,
	"ADCX140_GPIO_MON" 			: 0x2a,
	"ADCX140_GPI_CFG0" 			: 0x2b,
	"ADCX140_GPI_CFG1" 			: 0x2c,
	"ADCX140_GPI_MON" 			: 0x2f,
	"ADCX140_INT_CFG" 			: 0x32,
	"ADCX140_INT_MASK0" 		: 0x33,
	"ADCX140_INT_LTCH0" 		: 0x36,
	"ADCX140_BIAS_CFG"			: 0x3b,
	"ADCX140_CH1_CFG0"			: 0x3c,
	"ADCX140_CH1_CFG1"			: 0x3d,
	"ADCX140_CH1_CFG2"			: 0x3e,
	"ADCX140_CH1_CFG3"			: 0x3f,
	"ADCX140_CH1_CFG4"			: 0x40,
	"ADCX140_CH2_CFG0"			: 0x41,
	"ADCX140_CH2_CFG1"			: 0x42,
	"ADCX140_CH2_CFG2"			: 0x43,
	"ADCX140_CH2_CFG3"			: 0x44,
	"ADCX140_CH2_CFG4"			: 0x45,
	"ADCX140_CH3_CFG0"			: 0x46,
	"ADCX140_CH3_CFG1"			: 0x47,
	"ADCX140_CH3_CFG2"			: 0x48,
	"ADCX140_CH3_CFG3"			: 0x49,
	"ADCX140_CH3_CFG4"			: 0x4a,
	"ADCX140_CH4_CFG0"			: 0x4b,
	"ADCX140_CH4_CFG1"			: 0x4c,
	"ADCX140_CH4_CFG2"			: 0x4d,
	"ADCX140_CH4_CFG3"			: 0x4e,
	"ADCX140_CH4_CFG4"			: 0x4f,
	"ADCX140_CH5_CFG2"			: 0x52,
	"ADCX140_CH5_CFG3"			: 0x53,
	"ADCX140_CH5_CFG4"			: 0x54,
	"ADCX140_CH6_CFG2"			: 0x57,
	"ADCX140_CH6_CFG3"			: 0x58,
	"ADCX140_CH6_CFG4"			: 0x59,
	"ADCX140_CH7_CFG2"			: 0x5c,
	"ADCX140_CH7_CFG3"			: 0x5d,
	"ADCX140_CH7_CFG4"			: 0x5e,
	"ADCX140_CH8_CFG2"			: 0x61,
	"ADCX140_CH8_CFG3"			: 0x62,
	"ADCX140_CH8_CFG4"			: 0x63,
	"ADCX140_DSP_CFG0"			: 0x6b,
	"ADCX140_DSP_CFG1"			: 0x6c,
	"ADCX140_DRE_CFG0"			: 0x6d,
	"ADCX140_AGC_CFG0"			: 0x70,
	"ADCX140_IN_CH_EN"			: 0x73,
	"ADCX140_ASI_OUT_CH_EN" 	: 0x74,
	"ADCX140_PWR_CFG" 			: 0x75,
	"ADCX140_DEV_STS0" 			: 0x76,
	"ADCX140_DEV_STS1" 			: 0x77
}

# reverse the mp dictionary
rmp = {v:k for k, v in mp.items()}
i2c_current=dict()
i2c_mod=dict()
#
def addr_txt(num):
    return(rmp[num])
    

def bin8(dec_num):
    return("0b"+f"{dec_num:08b}")


def addr(st):
    return(mp[st])


def i2cread(ad):
    #handle ints or string addresses by turning ints to strings
    if isinstance(ad,int):
        ad=addr_txt(ad)
    msg = i2c.read_byte_data(adc_i2c_address, addr(ad))
    if debug:
        print("RD Addr:\t",ad,"\t\t\tis ",addr(ad),"(", hex(addr(ad)),")","-> read",msg,"\t\t<", hex(msg),"\t\t> <",bin8(msg),">")
    return msg


i2cread("ADCX140_PAGE_SELECT" 			) #1

i2cread("ADCX140_SW_RESET"				) #2

i2cread("ADCX140_SLEEP_CFG" 			) #3

i2cread("ADCX140_SHDN_CFG" 				) #4

i2cread("ADCX140_ASI_CFG0" 				) #5
i2cread("ADCX140_ASI_CFG1" 				) #6
i2cread("ADCX140_ASI_CFG2" 				) #7

i2cread("ADCX140_ASI_CH1" 				) #8
i2cread("ADCX140_ASI_CH2" 				) #9
i2cread("ADCX140_ASI_CH3" 				) #10
i2cread("ADCX140_ASI_CH4" 				) #11
i2cread("ADCX140_ASI_CH5" 				) #12
i2cread("ADCX140_ASI_CH6" 				) #13
i2cread("ADCX140_ASI_CH7" 				) #14
i2cread("ADCX140_ASI_CH8" 				) #15

i2cread("ADCX140_MST_CFG0" 				) #16
i2cread("ADCX140_MST_CFG1" 				) #17

i2cread("ADCX140_ASI_STS" 				) #18

i2cread("ADCX140_CLK_SRC" 				) #19

i2cread("ADCX140_PDMCLK_CFG" 			) #20

i2cread("ADCX140_PDM_CFG" 				) #21

i2cread("ADCX140_GPIO_CFG0" 			) #22

i2cread("ADCX140_GPO_CFG0" 				) #23
i2cread("ADCX140_GPO_CFG1"				) #24
i2cread("ADCX140_GPO_CFG2"				) #25
i2cread("ADCX140_GPO_CFG3"				) #26

i2cread("ADCX140_GPO_VAL" 				) #27

i2cread("ADCX140_GPIO_MON" 				) #28

i2cread("ADCX140_GPI_CFG0" 				) #29
i2cread("ADCX140_GPI_CFG1" 				) #30

i2cread("ADCX140_GPI_MON" 				) #31

i2cread("ADCX140_INT_CFG" 				) #32

i2cread("ADCX140_INT_MASK0" 			) #33

i2cread("ADCX140_INT_LTCH0" 			) #34
i2cread("ADCX140_INT_LTCH0"                     ) #34 readed two time to clear interrrupt flags

i2cread("ADCX140_BIAS_CFG"				) #35

i2cread("ADCX140_CH1_CFG0"				) #36
i2cread("ADCX140_CH1_CFG1"				) #37
i2cread("ADCX140_CH1_CFG2"				) #38
i2cread("ADCX140_CH1_CFG3"				) #39
i2cread("ADCX140_CH1_CFG4"				) #40

i2cread("ADCX140_CH2_CFG0"				) #41
i2cread("ADCX140_CH2_CFG1"				) #42
i2cread("ADCX140_CH2_CFG2"				) #43
i2cread("ADCX140_CH2_CFG3"				) #44
i2cread("ADCX140_CH2_CFG4"				) #45

i2cread("ADCX140_CH3_CFG0"				) #46
i2cread("ADCX140_CH3_CFG1"				) #47
i2cread("ADCX140_CH3_CFG2"				) #48
i2cread("ADCX140_CH3_CFG3"				) #49
i2cread("ADCX140_CH3_CFG4"				) #50

i2cread("ADCX140_CH4_CFG0"				) #51
i2cread("ADCX140_CH4_CFG1"				) #52
i2cread("ADCX140_CH4_CFG2"				) #53
i2cread("ADCX140_CH4_CFG3"				) #54
i2cread("ADCX140_CH4_CFG4"				) #55

i2cread("ADCX140_CH5_CFG2"				) #56
i2cread("ADCX140_CH5_CFG3"				) #57
i2cread("ADCX140_CH5_CFG4"				) #58

i2cread("ADCX140_CH6_CFG2"				) #59
i2cread("ADCX140_CH6_CFG3"				) #60
i2cread("ADCX140_CH6_CFG4"				) #61

i2cread("ADCX140_CH7_CFG2"				) #62
i2cread("ADCX140_CH7_CFG3"				) #63
i2cread("ADCX140_CH7_CFG4"				) #64

i2cread("ADCX140_CH8_CFG2"				) #65
i2cread("ADCX140_CH8_CFG3"				) #66
i2cread("ADCX140_CH8_CFG4"				) #67

i2cread("ADCX140_DSP_CFG0"				) #68
i2cread("ADCX140_DSP_CFG1"				) #69

i2cread("ADCX140_DRE_CFG0"				) #70

i2cread("ADCX140_AGC_CFG0"				) #71

i2cread("ADCX140_IN_CH_EN"				) #72

i2cread("ADCX140_ASI_OUT_CH_EN" 		) #73

i2cread("ADCX140_PWR_CFG" 				) #74

i2cread("ADCX140_DEV_STS0" 				) #75
i2cread("ADCX140_DEV_STS1" 				) #76
