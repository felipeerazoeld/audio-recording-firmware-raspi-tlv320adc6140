from smbus import SMBus
i2c = SMBus(4)
adc_i2c_address = 0x4c
debug=True

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

def addr_txt(num):
    return(rmp[num])
    
def bin8(dec_num):
    return "0b"+f"{dec_num:08b}"

def addr(st):
    return(mp[st])
    
def i2cwrite(ad, msg):
    #handle ints or string addresses by turning ints to strings
    if isinstance(ad,int):
        ad=addr_txt(ad)

    if debug:
        print("WR Addr:\t",ad,"\t\t\tis ",addr(ad),"(", hex(addr(ad)),")","-> read",msg,"\t\t<", hex(msg),"\t\t> <",bin8(msg),">")
   
    #if not debug:
    i2c.write_byte_data(adc_i2c_address, addr(ad), msg)
    i2c_current[ad]=msg
    if ad in i2c_mod:
        del i2c_mod[ad]
        
    return

i2cwrite("ADCX140_PAGE_SELECT"		,0b00000000) #1

i2cwrite("ADCX140_SW_RESET"			,0b00000000) #2

i2cwrite("ADCX140_SLEEP_CFG"		,0b10000001) #3

i2cwrite("ADCX140_SHDN_CFG"			,0b00000101) #4

i2cwrite("ADCX140_ASI_CFG0"			,0b00110000) #5
i2cwrite("ADCX140_ASI_CFG1"			,0b00000000) #6
i2cwrite("ADCX140_ASI_CFG2"			,0b00000000) #7

i2cwrite("ADCX140_ASI_CH1"			,0b00000000) #8
i2cwrite("ADCX140_ASI_CH2"			,0b00000001) #9
i2cwrite("ADCX140_ASI_CH3"			,0b00000010) #10
i2cwrite("ADCX140_ASI_CH4"			,0b00000011) #11
i2cwrite("ADCX140_ASI_CH5"			,0b00000100) #12
i2cwrite("ADCX140_ASI_CH6"			,0b00000101) #13
i2cwrite("ADCX140_ASI_CH7"			,0b00000110) #14
i2cwrite("ADCX140_ASI_CH8"			,0b00000111) #15

i2cwrite("ADCX140_MST_CFG0"			,0b00000010) #16
i2cwrite("ADCX140_MST_CFG1"			,0b01001000) #17

i2cwrite("ADCX140_ASI_STS"			,0b01100100) #18

i2cwrite("ADCX140_CLK_SRC"			,0b00010000) #19

i2cwrite("ADCX140_PDMCLK_CFG"		,0b01000000) #20

i2cwrite("ADCX140_PDM_CFG"			,0b00000000) #21

i2cwrite("ADCX140_GPIO_CFG0"		,0b00100010) #22

i2cwrite("ADCX140_GPO_CFG0"			,0b00000000) #23
i2cwrite("ADCX140_GPO_CFG1"			,0b00000000) #24
i2cwrite("ADCX140_GPO_CFG2"			,0b00000000) #25
i2cwrite("ADCX140_GPO_CFG3"			,0b00000000) #26

i2cwrite("ADCX140_GPO_VAL"			,0b00000000) #27

i2cwrite("ADCX140_GPIO_MON"			,0b00000000) #28

i2cwrite("ADCX140_GPI_CFG0"			,0b00000000) #29
i2cwrite("ADCX140_GPI_CFG1"			,0b00000000) #30

i2cwrite("ADCX140_GPI_MON"			,0b00000000) #31

i2cwrite("ADCX140_INT_CFG"			,0b00000000) #32

i2cwrite("ADCX140_INT_MASK0"		,0b11111111) #33

i2cwrite("ADCX140_INT_LTCH0"		,0b11000000) #34

i2cwrite("ADCX140_BIAS_CFG"			,0b00000000) #35

i2cwrite("ADCX140_CH1_CFG0"			,0b00100000) #36
i2cwrite("ADCX140_CH1_CFG1"			,0b10001100) #37
i2cwrite("ADCX140_CH1_CFG2"			,0b11001101) #38
i2cwrite("ADCX140_CH1_CFG3"			,0b10000000) #39
i2cwrite("ADCX140_CH1_CFG4"			,0b00000000) #40

i2cwrite("ADCX140_CH2_CFG0"			,0b00100000) #41
i2cwrite("ADCX140_CH2_CFG1"			,0b10001100) #42
i2cwrite("ADCX140_CH2_CFG2"			,0b11001101) #43
i2cwrite("ADCX140_CH2_CFG3"			,0b10000000) #44
i2cwrite("ADCX140_CH2_CFG4"			,0b00000000) #45

i2cwrite("ADCX140_CH3_CFG0"			,0b00100000) #46
i2cwrite("ADCX140_CH3_CFG1"			,0b10001100) #47
i2cwrite("ADCX140_CH3_CFG2"			,0b11001101) #48
i2cwrite("ADCX140_CH3_CFG3"			,0b10000000) #49
i2cwrite("ADCX140_CH3_CFG4"			,0b00000000) #50

i2cwrite("ADCX140_CH4_CFG0"			,0b00100000) #51
i2cwrite("ADCX140_CH4_CFG1"			,0b10001100) #52
i2cwrite("ADCX140_CH4_CFG2"			,0b11001101) #53
i2cwrite("ADCX140_CH4_CFG3"			,0b10000000) #54
i2cwrite("ADCX140_CH4_CFG4"			,0b00000000) #55

i2cwrite("ADCX140_CH5_CFG2"			,0b11001001) #56
i2cwrite("ADCX140_CH5_CFG3"			,0b10000000) #57
i2cwrite("ADCX140_CH5_CFG4"			,0b00000000) #58

i2cwrite("ADCX140_CH6_CFG2"			,0b11001001) #59
i2cwrite("ADCX140_CH6_CFG3"			,0b10000000) #60
i2cwrite("ADCX140_CH6_CFG4"			,0b00000000) #61

i2cwrite("ADCX140_CH7_CFG2"			,0b11001001) #62
i2cwrite("ADCX140_CH7_CFG3"			,0b10000000) #63
i2cwrite("ADCX140_CH7_CFG4"			,0b00000000) #64

i2cwrite("ADCX140_CH8_CFG2"			,0b11001001) #65
i2cwrite("ADCX140_CH8_CFG3"			,0b10000000) #66
i2cwrite("ADCX140_CH8_CFG4"			,0b00000000) #67

i2cwrite("ADCX140_DSP_CFG0"			,0b00000001) #68
i2cwrite("ADCX140_DSP_CFG1"			,0b00001000) #69

i2cwrite("ADCX140_DRE_CFG0"			,0b01111011) #70

i2cwrite("ADCX140_AGC_CFG0"			,0b11100111) #71

i2cwrite("ADCX140_IN_CH_EN"			,0b11110000) #72

i2cwrite("ADCX140_ASI_OUT_CH_EN"	,0b11110000) #73

i2cwrite("ADCX140_PWR_CFG"			,0b01100100) #74

i2cwrite("ADCX140_DEV_STS0"			,0b11110000) #75
i2cwrite("ADCX140_DEV_STS1"			,0b11100000) #76                                               
                                                   
                                                   
