# USAGE
# python detect_face.py

# import the necessary packages
import cv2

# load our image and convert it to grayscale
image = cv2.imread("orientation_example.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load the face detector and detect faces in the image
# we will be using pre-trained classifer 'haarcascade_frontalface_default.xml'
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# scaleFactor=1.05 -- means reduce the image by 5% at each level
rects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=9,
	minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

# loop over the faces and draw a rectangle surrounding each
# draw bounding boxes
for (x, y, w, h) in rects:
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# show the detected faces
cv2.imshow("Faces", image)
cv2.waitKey(0)
