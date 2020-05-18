# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:49:16 2020

@author: rdayala
"""

# import the necessary packages
import numpy as np
import cv2
 
# initialize our canvas as a 640x480 (width x height) with 3 channels, 
# Red, Green,and Blue, with a black background
# for NumPy array, we need to pass (rows, columns) format i.e., (height, width)
canvas = np.zeros((480, 640, 3), dtype="uint8")

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()