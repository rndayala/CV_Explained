# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:27:47 2020

@author: rdayala
"""

import numpy as np
import cv2

image = cv2.imread('rose.jpg')
cv2.imshow("Original", image)

result = image.copy()

image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# lower boundary RED color range values
lower1 = np.array([0, 100, 20])
upper1 = np.array([10, 255, 255])

# upper boundary RED color range values
lower2 = np.array([160,100,20])
upper2 = np.array([179,255,255])

lower_mask = cv2.inRange(image, lower1, upper1)
upper_mask = cv2.inRange(image, lower2, upper2)

full_mask = lower_mask + upper_mask;

result = cv2.bitwise_and(result, result, mask=full_mask)

cv2.imshow('mask', full_mask)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()