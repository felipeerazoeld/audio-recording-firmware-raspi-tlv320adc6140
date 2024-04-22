Requeriments:
in X86 arch, 
sudo apt-get install python3-pyaudio
pip3 install smbus

and is desired:
sudo apt install alsa-utils

#To set i2c bus persmission non-root users:
#https://askubuntu.com/questions/1273700/enable-spi-and-i2c-on-ubuntu-20-04-raspberry-pi
#sudo chmod a+rw /dev/i2c-*
sudo nano /etc/udev/rules.d/99-com.rules
SUBSYSTEM=="ic2-dev", GROUP="i2c", MODE="0666"

