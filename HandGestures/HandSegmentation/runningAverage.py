# Ref link - https://cvexplained.wordpress.com/2020/04/17/running-average-model-background-subtraction/

# organize imports 
import cv2 
import numpy as np 
  
# capture frames from a camera 
cap = cv2.VideoCapture(0) 
  
# read the frames from the camera 
_, img = cap.read() 
  
# modify the data type 
# setting to 32-bit floating point 
# initializing output images
averageValue1 = np.float32(img) 
averageValue2 = np.float32(img)

# loop runs if capturing has been initialized.  
while(1): 
    # reads frames from a camera  
    (grabbed, img) = cap.read()

    # using the cv2.accumulateWeighted() function 
    # that updates the running average 
    # cv2.accumulateWeighted(srcImage, outputImage, alphaValue)
    # higher alpha value - it updates faster...
    cv2.accumulateWeighted(img, averageValue1, 0.1)
    cv2.accumulateWeighted(img, averageValue2, 0.01)
      
    # converting the matrix elements to absolute values  
    # and converting the result back to 8-bit.  
    runningAverage1 = cv2.convertScaleAbs(averageValue1)
    runningAverage2 = cv2.convertScaleAbs(averageValue2)

    # Show two output windows 
    # the input / original frames window 
    cv2.imshow('InputWindow', img) 
  
    # the window showing output of alpha value 0.5 
    cv2.imshow('RunningAverage1', runningAverage1) 
    # the window showing output of alpha value 0.05
    cv2.imshow('RunningAverage2', runningAverage2)

    # Wait for 'Esc' key to stop the program  
    k = cv2.waitKey(30) & 0xff
    if k == 27:  
        break
  
# Close the window  
cap.release()  
    
# De-allocate any associated memory usage  
cv2.destroyAllWindows() 
