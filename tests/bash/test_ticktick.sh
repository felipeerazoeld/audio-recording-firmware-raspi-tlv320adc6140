#!/bin/bash

. ticktick.sh

DATA=`cat settings.json`
tickParse "$DATA"

echo ``HW["i2c_bus"]``
echo ``HW["adc_addr"]``
echo ``ADC["CHANNELS"]``
echo ``ADC["RATE"]``
echo ``ADC["FORMAT"]``
echo ``ADC["DURATION"]``
echo ``ADC["FILEPATH"]``
echo ``ADC["DEVICE"]``