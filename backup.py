"""
Justin Garrity
11/5/20
Version 1
Description
"""

# Importing Libaries
import cv2
import numpy


# Start Video Capture
cap = cv2.VideoCapture(0)


cv2.namedWindow("Original")
cv2.namedWindow("C1Filter")
cv2.namedWindow("C2Filter")
cv2.namedWindow("C3Filter")
cv2.namedWindow("Final")
cv2.namedWindow("C1Trackbars")
cv2.namedWindow("C2Trackbars")
cv2.namedWindow("C3Trackbars")

cv2.resizeWindow("C1Trackbars", 480, 500)
cv2.resizeWindow("C2Trackbars", 480, 500)
cv2.resizeWindow("C3Trackbars", 480, 500)


cv2.createTrackbar("C1BlueMin", "C1Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C1BlueMax", "C1Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C1GreenMin", "C1Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C1GreenMax", "C1Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C1RedMin", "C1Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C1RedMax", "C1Trackbars", 0, 255, lambda x: None)

cv2.createTrackbar("C2BlueMin", "C2Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C2BlueMax", "C2Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C2GreenMin", "C2Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C2GreenMax", "C2Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C2RedMin", "C2Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C2RedMax", "C2Trackbars", 0, 255, lambda x: None)

cv2.createTrackbar("C3BlueMin", "C3Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C3BlueMax", "C3Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C3GreenMin", "C3Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C3GreenMax", "C3Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C3RedMin", "C3Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C3RedMax", "C3Trackbars", 0, 255, lambda x: None)

key_pressed = 1

while key_pressed != 27:
    ret, frame = cap.read()

    C1BMin = cv2.getTrackbarPos("C1BlueMin", "C1Trackbars")
    C1BMax = cv2.getTrackbarPos("C1BlueMax", "C1Trackbars")
    C1GMin = cv2.getTrackbarPos("C1GreenMin", "C1Trackbars")
    C1GMax = cv2.getTrackbarPos("C1GreenMax", "C1Trackbars")
    C1RMin = cv2.getTrackbarPos("C1RedMin", "C1Trackbars")
    C1RMax = cv2.getTrackbarPos("C1RedMax", "C1Trackbars")

    C2BMin = cv2.getTrackbarPos("C2BlueMin", "C2Trackbars")
    C2BMax = cv2.getTrackbarPos("C2BlueMax", "C2Trackbars")
    C2GMin = cv2.getTrackbarPos("C2GreenMin", "C2Trackbars")
    C2GMax = cv2.getTrackbarPos("C2GreenMax", "C2Trackbars")
    C2RMin = cv2.getTrackbarPos("C2RedMin", "C2Trackbars")
    C2RMax = cv2.getTrackbarPos("C2RedMax", "C2Trackbars")

    C3BMin = cv2.getTrackbarPos("C3BlueMin", "C3Trackbars")
    C3BMax = cv2.getTrackbarPos("C3BlueMax", "C3Trackbars")
    C3GMin = cv2.getTrackbarPos("C3GreenMin", "C3Trackbars")
    C3GMax = cv2.getTrackbarPos("C3GreenMax", "C3Trackbars")
    C3RMin = cv2.getTrackbarPos("C3RedMin", "C3Trackbars")
    C3RMax = cv2.getTrackbarPos("C3RedMax", "C3Trackbars")

    lowerC1 = [C1BMin, C1GMin, C1RMin]
    upperC1 = [C1BMax, C1GMax, C1RMax]
    lowerC2 = [C2BMin, C2GMin, C2RMin]
    upperC2 = [C2BMax, C2GMax, C2RMax]
    lowerC3 = [C3BMin, C3GMin, C3RMin]
    upperC3 = [C3BMax, C3GMax, C3RMax]

    lowerC1 = numpy.array(lowerC1, dtype="uint8")
    upperC1 = numpy.array(upperC1, dtype="uint8")
    lowerC2 = numpy.array(lowerC2, dtype="uint8")
    upperC2 = numpy.array(upperC2, dtype="uint8")
    lowerC3 = numpy.array(lowerC3, dtype="uint8")
    upperC3 = numpy.array(upperC3, dtype="uint8")

    C1Mask = cv2.inRange(frame, lowerC1, upperC1)
    C2Mask = cv2.inRange(frame, lowerC2, upperC2)
    C3Mask = cv2.inRange(frame, lowerC3, upperC3)

    filteredC1 = cv2.bitwise_or(ret, frame, mask=C1Mask)
    filteredC2 = cv2.bitwise_or(frame, frame, mask=C2Mask)
    filteredC3 = cv2.bitwise_or(frame, frame, mask=C3Mask)

    combined = cv2.bitwise_or(filteredC1, filteredC2)
    combined = cv2.bitwise_or(combined, filteredC3)

    cv2.imshow("Original", frame)
    cv2.imshow("C1Filter", filteredC1)
    cv2.imshow("C2Filter", filteredC2)
    cv2.imshow("C3Filter", filteredC3)
    cv2.imshow("Final", combined)

    keypressed = cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
