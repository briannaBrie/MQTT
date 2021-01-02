#program to builfd a python app, getting messages 
#from Azure IoT hub, taking a picture and uploading
#it to Azure Blob

import os
import cv2
import numpy as np
import datetime

class camera:
    "take a picture and saved it in the static folder"

    def _init_(self):
        #take the first camera
        self.cam=cv2.VideoCapture(0)
        self.timezone =0
        pass

    def TakePicture(self):
        #read a frame
        ret, frame = self.cam.read()
        #where the code is running should be /app
        img_name = os.getcwd() + os.path.normpath("/home/pi/Desktop/image.jpg")
        _, width = frame.shape[:2]
        #create a black image with same width as main image
        img = np.zeros((50, width, 3), np.uint8)
        #write the date
        font =cv2.FONT_HERSHEY_COMPLEX_SMALL
        bottonLeftCornerOfText = (10,25)
        fontScale = 1
        fontColor = (255,255,255)
        lineType = 1
        #format the datetime
        today = datetime.datetime.now() + datetime.timedelta(hours = self.timezone)
        thedate = '{:%Y/%m/%d %H:%M:%S}'.format(today)
        cv2.putText(img, thedate, bottomLeftCornerOfText, 
            font, fontScale, fontColor, lineType)
        #add both images and save the final image
        vis = np.concatenate((frame, img), axis = 0)
        cv2.imwrite(img_name, vis)

    def _enter_(self):
            return self

    def _exit_(self, exc_type, exc_value, traceback):
        #close camera
        self.cam.release()