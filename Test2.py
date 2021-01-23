"""
Justin Garrity
11/5/20
Version 3
Description: This program is designed to detect one color and filter out the rest
"""

# Importing Libaries
import cv2
import numpy

# Captures Video Feed
cap = cv2.VideoCapture(0)

# Creates 2 windows
cv2.namedWindow("Combined")
cv2.namedWindow("C1Filtered")

# Resizes Window so it fits on the screen
cv2.resizeWindow("Original", 240, 250)

# Creates all 6 trackbars for the colors
# Is by default set to detect red
cv2.createTrackbar("C1BlueMin", "Combined", 0, 255, lambda x: None)
cv2.createTrackbar("C1BlueMax", "Combined", 255, 255, lambda x: None)
cv2.createTrackbar("C1GreenMin", "Combined", 0, 255, lambda x: None)
cv2.createTrackbar("C1GreenMax", "Combined", 110, 255, lambda x: None)
cv2.createTrackbar("C1RedMin", "Combined", 174, 255, lambda x: None)
cv2.createTrackbar("C1RedMax", "Combined", 255, 255, lambda x: None)

keypressed = 1
# While loop will run while keypressed doesn't equal escape
while (keypressed != 27):
    # Stores Video capture
    ret, frame = cap.read()

    # Saves the position of the trackbars and there values
    C1BMin = cv2.getTrackbarPos("C1BlueMin", "Combined")
    C1BMax = cv2.getTrackbarPos("C1BlueMax", "Combined")
    C1GMin = cv2.getTrackbarPos("C1GreenMin", "Combined")
    C1GMax = cv2.getTrackbarPos("C1GreenMax", "Combined")
    C1RMin = cv2.getTrackbarPos("C1RedMin", "Combined")
    C1RMax = cv2.getTrackbarPos("C1RedMax", "Combined")

    # Creates a low and high limit for the color
    lowC1 = [C1BMin, C1GMin, C1RMin]
    highC1 = [C1BMax, C1GMax, C1RMax]

    # turns them into numpy arrays
    lowC1 = numpy.array(lowC1, dtype="uint8")
    highC1 = numpy.array(highC1, dtype="uint8")

    # combines into mask which will hide what is higher than highC1 and lower than lowC1
    C1Mask = cv2.inRange(frame, lowC1, highC1)

    # Creates into final product
    fC1 = cv2.bitwise_or(frame, frame, mask=C1Mask)

    # Shows the data of the combined and filteered image
    cv2.imshow("Combined", frame)
    cv2.imshow("C1Filtered", fC1)

    # Will destory when escape is pressed
    keypressed = cv2.waitKey(30)

cap.release()
cv2.destroyAllWindows()
