"""
Justin Garrity
11/5/20
Version 1
Description
"""

# Importing Libaries
import cv2
import numpy
import os.path

cap = cv2.VideoCapture(0)

cv2.namedWindow("Original")
cv2.namedWindow("Filtered C1")
cv2.namedWindow("C1 Controls")

cv2.resizeWindow("C1 Controls", 240, 250)

cv2.createTrackbar("C1 Blue Min", "Original", 0, 255, lambda x: None)
cv2.createTrackbar("C1 Blue Max", "Original", 255, 255, lambda x: None)
cv2.createTrackbar("C1 Green Min", "Original", 0, 255, lambda x: None)
cv2.createTrackbar("C1 Green Max", "Original", 110, 255, lambda x: None)
cv2.createTrackbar("C1 Red Min", "Original", 174, 255, lambda x: None)
cv2.createTrackbar("C1 Red Max", "Original", 255, 255, lambda x: None)

keypressed = 1

while (keypressed != 27):
    ret, frame = cap.read()

    C1b_min = cv2.getTrackbarPos("C1 Blue Min", "Original")
    C1b_max = cv2.getTrackbarPos("C1 Blue Max", "Original")
    C1g_min = cv2.getTrackbarPos("C1 Green Min", "Original")
    C1g_max = cv2.getTrackbarPos("C1 Green Max", "Original")
    C1r_min = cv2.getTrackbarPos("C1 Red Min", "Original")
    C1r_max = cv2.getTrackbarPos("C1 Red Max", "Original")

    lower_C1 = [C1b_min, C1g_min, C1r_min]
    upper_C1 = [C1b_max, C1g_max, C1r_max]

    lower_C1 = numpy.array(lower_C1, dtype="uint8")
    upper_C1 = numpy.array(upper_C1, dtype="uint8")

    """
    paper = numpy.zeros((frame.shape[0],frame.shape[1],frame.shape[2]), numpy.uint8)

    image_height = frame.shape[0]
    image_width = frame.shape[1]
    image_channels = frame.shape[2]
    paper[0:image_height, 0:image_width, 0:image_channels] = frame
    """

    C1Mask = cv2.inRange(frame, lower_C1, upper_C1)

    filtered_C1 = cv2.bitwise_or(frame, frame, mask=C1Mask)

    cv2.imshow("Original", frame)
    cv2.imshow("Filtered C1", filtered_C1)

    keypressed = cv2.waitKey(30)

cap.release()
cv2.destroyAllWindows()