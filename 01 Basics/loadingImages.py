# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:20:55 2020

@author: rdayala
"""

# Loading images using OpenCV
# using cv2.imread() function
# https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56
# https://note.nkmk.me/en/python-opencv-imread-imwrite/

# import the necessary packages
import argparse
import cv2
  
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
 
# load the image and show some basic information on it
image = cv2.imread(args["image"])
 
print("Color Image shape :", image.shape)
print("width: %d pixels" % (image.shape[1]))
print("height: %d pixels" % (image.shape[0]))
print("Color image Channels: %d" % (image.shape[2]))

# load the image in Gray-scale format
gray = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)
print("Gray Image shape :", gray.shape)
print("width: %d pixels" % (gray.shape[1]))
print("height: %d pixels" % (gray.shape[0]))
  
# show the image and wait for a keypress
cv2.imshow("Color Image", image)
cv2.imshow("Gray Image", gray)
cv2.waitKey(0)
