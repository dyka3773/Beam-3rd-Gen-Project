### Install Pleora Gstreamer Plugin on Ubuntu 18.04
1. Follow the steps given in the readme file of the repository https://github.com/joshdoe/gst-plugins-vision/tree/master
2. `modprobe {pleora-src}` (Not sure about the second part , we'll see)

### Start working on the RXSM Communication
1. Try to jumper pins 8 and 10 on the GPIO header
2. With `sudo picocom -b 115200 /dev/ttyTHS1`
3. Type stuff on screen and if they show up it works
4. If everything works, change the permissions of the serial port. `sudo chmod 666 /dev/ttyTHS1` (or `chown dropstar:dropstar /dev/ttyTHS1` it to the user)