#Take a photo with raspberry pi camera in python
#!/usr/bin/env python

from picamera import PiCamera
from time import sleep

#use the picamera module to control the camera
camera = PiCamera()
#set the max image resolution and framerate
camera.resolution = (2592, 1944)
camera.framerate = 15

#This turns on the camera and allows it to begin to focus
camera.start_preview()
camera.brightness = 70
#wait for 5 sec. Enough time to give it focus and then take the picture
sleep(5)
#save the picture to the following directory
#camera.capture('/home/pi/Desktop/image.jpg')

#To add a loop to take 5 pictures in a row:
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)

camera.stop_preview()  

#pi@raspberrypi:/tmp/picture.jpg ~/Downloads/
#transfers the image to your downloads folder

#sudo apt-get install -y build-essential tk-dev 
# libncurses5-dev libncursesw5-dev libreadline6-dev 
# libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev 
# libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev 
# libffi-dev 