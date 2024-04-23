#!/usr/bin/python3
import sys
import json
# Opening JSON file
f = open('./conf/settings.json')
data = json.load(f)
f.close()
#
sys.path.append(str(data['GLOBAL']['path_append']))

import pyaudio

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
    try:
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, "-", p.get_device_info_by_host_api_device_index(0, i).get('name'))
        if str(p.get_device_info_by_host_api_device_index(0, i).get('name'))=="TI USB Audio 2.0: - (hw:0,0)":
            #dev_str=str(p.get_device_info_by_host_api_device_index(0, i).get('name'))
            #print(dev_str.split())
            with open('./conf/settings.json', 'r+') as f:
                data = json.load(f)
                data['ADC']['INPUT_DEV_ID'] = str(i) 
                f.seek(0)
                json.dump(data, f, indent=4)
                data = json.load(f)
                f.truncate()
                f.close()
    except Exception as e:
       print("*E: "+str(e))

import time
timestr = time.strftime("%Y%m%d-%H%M%S")
#print(timestr)

import wave

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt24  # 16 bits per sample paFloat32
channels = 4
fs = 192000  # Record at 44100 samples per second
seconds = 3
filename = str(data["GLOBAL"]["path_append"])+"/tests/"+str(data["ADC"]["FILEPATH"])+"/"+"sample_"+str(timestr)+".wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording :'+filename)

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input_device_index=int(data['ADC']['INPUT_DEV_ID']), #TBD: This come from previously printed list Should be a automatic method to get this value
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 


stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

