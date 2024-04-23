#Requeriments:
#in X86 arch, 
sudo apt-get install python3-pip python3-pyaudio python3-smbus git i2c-tools

#and is desired:
sudo apt install alsa-utils

#In some SO like debian this command is needed to access i2c bus:
sudo modprobe i2c-dev
#to make the modprobe permanent add the command to /etc/modules file as showed in
#https://superuser.com/questions/759426/smbus-i2c-on-a-pcie-bus
#If need disable sound cards interfaces use : https://superuser.com/questions/675787/disable-a-linux-sound-card

#To set i2c bus persmission non-root users:
#https://askubuntu.com/questions/1273700/enable-spi-and-i2c-on-ubuntu-20-04-raspberry-pi
#sudo chmod a+rw /dev/i2c-*
sudo nano /etc/udev/rules.d/99-com.rules
SUBSYSTEM=="ic2-dev", GROUP="i2c", MODE="0666"

