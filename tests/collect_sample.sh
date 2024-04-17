#!/bin/bash
TS=$(date +%Y%m%d_%H%M%SZ)
#RATE=176400
RATE="192000"
#RATE="48000"
#RATE="96000"
#RATE="44100"
#FORMAT="S24_LE"
#FORMAT="S16_LE"
FORMAT="S32_LE"
DURATION="3" #300 sec 5min
#DURATION="3600" #3600 sec 60min
#DURATION="10" #10sec
#DURATION="60" #60sec, 1min
#DURATION="43200" #12h
#DURATION="86400" #24h
#DURATION="259200" #24h*3 #3 days
#DURATION="604800" #7d
#MAXSIZE = 500000
#CHANNELS="4"
CHANNELS="8"
#
#FILEPATH="/home/ubuntu/bin/focusrite_sound_record"
#FILEPATH="/media/ubuntu/ssd" # ssd FE
#FILEPATH="/media/ubuntu/USDSOUND" #cartao 1
#FILEPATH="/media/ubuntu/D783-02E2" #cartao 2
#FILEPATH="/home/felipeerazo/Downloads/mic_config/" #teste
#FILEPATH=/home/root/WS/mic_config/
FILEPATH=./samples/
FILENAME=${FILEPATH}/sample_${RATE}_${FORMAT}_${DURATION}_CH${CHANNELS}_${TS}
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
DEVICE="hw:3,0,0"

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
#
echo "arecord -D ${DEVICE} -c ${CHANNELS} --vumeter=mono --rate=${RATE} --format=${FORMAT} --duration=${DURATION} ${FILENAME}.wav"

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
