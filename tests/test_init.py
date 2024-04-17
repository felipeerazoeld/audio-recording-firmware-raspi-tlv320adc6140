import sys
sys.path.append("/home/root/WS/audio-recording-firmware-raspi-tlv320adc6140/")
import TLV320ADC
adc1 = TLV320ADC.TLV320ADC()
import autorecord as ar
ar.setup_adc(adc1,30.0,27.0)
