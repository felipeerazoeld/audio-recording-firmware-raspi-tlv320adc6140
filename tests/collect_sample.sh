#!/bin/sh

. ticktick.sh
DATA=`cat settings.json`
tickParse "$DATA"

i2caddr=``HW["adc_addr"]``
i2cbus=``HW["i2c_bus"]``

TS=$(date +%Y%m%d_%H%M%SZ)

RATE=``ADC["RATE"]``
FORMAT=``ADC["FORMAT"]``
DURATION=``ADC["DURATION"]`` #10sec
#MAXSIZE = 500000
CHANNELS=``ADC["CHANNELS"]``
FILEPATH=``ADC["FILEPATH"]``
FILENAME=${FILEPATH}/sample_${RATE}_${FORMAT}_${DURATION}_CH${CHANNELS}_${TS}
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

#LOGFILE=${SCRIPT_DIR}/log/${RATE}_${FORMAT}_${DURATION}_CH${CHANNELS}_${TS}.log
#if [[ ! -e ${LOGFILE} ]]; then
#    echo "touching $LOGFILE"
#    touch ${LOGFILE}
#fi

#
#FILESIZE=$(stat -c%s "$FILENAME")
#if (( FILESIZE > MAXSIZE)); then
#    echo "nope"
#else
#    echo "fine"
#fi
DEVICE=``ADC["DEVICE"]``
#
arecord -D ${DEVICE} -c ${CHANNELS} --vumeter=mono --rate=${RATE} --format=${FORMAT} --duration=${DURATION} ${FILENAME}.wav
#FILESIZE=$(stat -c%s "$FILENAME.wav")
#FILESIZE_MB=$(( $( stat -c '%s' $FILENAME.wav ) / 1024 / 1024 ))
#echo ""
#echo "*I: wav file size: ${FILESIZE_MB} MB with ${DURATION} seconds" >> ${LOGFILE}
START=`date +%s.%N`
#MD5_N=`md5sum ${FILENAME}.wav`
#echo "*I: calculated md5 number: ${MD5_N}" >> ${LOGFILE}
#echo ${MD5_N} > ${FILENAME}.md5
#zip ${FILENAME}.wav.zip ${FILENAME}*.wav 
#${FILENAME}.md5 
#rm ${FILENAME}*.wav 
#${FILENAME}.md5
END=`date +%s.%N`
RUNTIME=$( echo "$END - $START" | bc -l )
#ZIPFILESIZE=$(stat -c%s "$FILENAME.wav.zip")
#ZIPFILESIZE_MB=$(( $( stat -c '%s' $FILENAME.wav.zip ) / 1024 / 1024 ))
#echo "*I: zipped wav filesize: ${ZIPFILESIZE_MB} MB" >> ${LOGFILE}
#echo "*I: time used to create zip and delete wave file ${RUNTIME} seconds" >> ${LOGFILE}
#
#python3 plot_fft.py ${filename}.wav 
echo $?
