#!/usr/bin/python3
import sys
import json
# Opening JSON file
f = open('./conf/settings.json')
data = json.load(f)
f.close()
#
sys.path.append(str(data['GLOBAL']['path_append']))
import TLV320ADC
adc1 = TLV320ADC.TLV320ADC()
#
adc1.i2cwrite("ADCX140_SW_RESET"        ,0b00000001)
adc1.i2cread ("ADCX140_SW_RESET"       )
#
adc1.i2cread ("ADCX140_SLEEP_CFG"      )
#
adc1.i2cwrite("ADCX140_DSP_CFG1"       	,0b00001000)
#
adc1.i2cwrite("ADCX140_CH1_CFG0"		,0b00100000)	
#adc1.i2cwrite("ADCX140_CH1_CFG1"		,0b10010000)
adc1.set_analog_gain(1,36)
#adc1.i2cwrite("ADCX140_CH1_CFG2"		,0b11001001)
adc1.set_digital_gain(1,0)
adc1.i2cwrite("ADCX140_CH1_CFG3"		,0b10000000)
#
adc1.i2cwrite("ADCX140_CH2_CFG0"		,0b00100000)
#adc1.i2cwrite("ADCX140_CH2_CFG1"		,0b10010000)
adc1.set_analog_gain(2,36)
#adc1.i2cwrite("ADCX140_CH2_CFG2"		,0b11001001)
adc1.set_digital_gain(2,0)
adc1.i2cwrite("ADCX140_CH2_CFG3"		,0b10000000)
#
adc1.i2cwrite("ADCX140_CH3_CFG0"		,0b00100000)
#adc1.i2cwrite("ADCX140_CH3_CFG1"		,0b10010000)
adc1.set_analog_gain(3,36)
#adc1.i2cwrite("ADCX140_CH3_CFG2"		,0b11001001)
adc1.set_digital_gain(3,0)
adc1.i2cwrite("ADCX140_CH3_CFG3"		,0b10000000)
#
adc1.i2cwrite("ADCX140_CH4_CFG0"		,0b00100000)
#adc1.i2cwrite("ADCX140_CH4_CFG1"		,0b10010000)
adc1.set_analog_gain(4,36)
#adc1.i2cwrite("ADCX140_CH4_CFG2"		,0b11001001)
adc1.set_digital_gain(4,0)
adc1.i2cwrite("ADCX140_CH4_CFG3"		,0b10000000)
#
adc1.i2cread ("ADCX140_CH1_CFG0"		)	
adc1.i2cread ("ADCX140_CH1_CFG1"		)
adc1.i2cread ("ADCX140_CH1_CFG2"		)
adc1.i2cread ("ADCX140_CH1_CFG3"		)
#       read 
adc1.i2cread ("ADCX140_CH2_CFG0"		)
adc1.i2cread ("ADCX140_CH2_CFG0"		)
adc1.i2cread ("ADCX140_CH2_CFG0"		)
adc1.i2cread ("ADCX140_CH2_CFG0"		)
#       read 
adc1.i2cread ("ADCX140_CH3_CFG0"		)
adc1.i2cread ("ADCX140_CH3_CFG0"		)
adc1.i2cread ("ADCX140_CH3_CFG0"		)
adc1.i2cread ("ADCX140_CH3_CFG0"		)
#       read 
adc1.i2cread ("ADCX140_CH4_CFG0"		)
adc1.i2cread ("ADCX140_CH4_CFG0"		)
adc1.i2cread ("ADCX140_CH4_CFG0"		)
adc1.i2cread ("ADCX140_CH4_CFG0"		)
#
adc1.i2cwrite("ADCX140_ASI_STS"			,0b01001000)
adc1.i2cread ("ADCX140_ASI_STS"			)
#
adc1.i2cwrite("ADCX140_SLEEP_CFG"		,0b10000001)
adc1.i2cread ("ADCX140_SLEEP_CFG"		)
#
adc1.i2cwrite("ADCX140_ASI_CFG0"		,0b00110000) #5
adc1.i2cread ("ADCX140_ASI_CFG0"		) #5
#
adc1.i2cwrite("ADCX140_IN_CH_EN"		,0b11110000)
adc1.i2cread ("ADCX140_IN_CH_EN"		)
#
adc1.i2cwrite("ADCX140_ASI_OUT_CH_EN"	,0b11110000)
adc1.i2cread ("ADCX140_ASI_OUT_CH_EN"	)	
#
adc1.i2cwrite("ADCX140_ASI_CH1"         ,0b00000000)
adc1.i2cwrite("ADCX140_ASI_CH2"         ,0b00000001)
adc1.i2cwrite("ADCX140_ASI_CH3"         ,0b00100000)
adc1.i2cwrite("ADCX140_ASI_CH4"         ,0b00100001)
adc1.i2cwrite("ADCX140_ASI_CH5"         ,0b00000100)
adc1.i2cwrite("ADCX140_ASI_CH6"         ,0b00000101)
adc1.i2cwrite("ADCX140_ASI_CH7"         ,0b00000110)
adc1.i2cwrite("ADCX140_ASI_CH8"         ,0b00000111)
#
adc1.i2cread ("ADCX140_ASI_CH1"          )
adc1.i2cread ("ADCX140_ASI_CH2"          )
adc1.i2cread ("ADCX140_ASI_CH3"          )
adc1.i2cread ("ADCX140_ASI_CH4"          )
adc1.i2cread ("ADCX140_ASI_CH5"          )
adc1.i2cread ("ADCX140_ASI_CH6"          )
adc1.i2cread ("ADCX140_ASI_CH7"          )
adc1.i2cread ("ADCX140_ASI_CH8"          )
# 
adc1.i2cwrite("ADCX140_PWR_CFG"			,0b01100100)
adc1.i2cread ("ADCX140_PWR_CFG"	)


