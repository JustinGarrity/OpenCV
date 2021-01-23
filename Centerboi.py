"""
Justin Garrity
11/17/20
Version 5
Description: This program is designed to detect three colors and filter out the rest using HSV color secem
"""

# Importing Libaries
import cv2
import numpy


# Start Video Capture
cap = cv2.VideoCapture(0)

# creates 6 windows
cv2.namedWindow("Original")
cv2.namedWindow("C1Filter")
cv2.namedWindow("C2Filter")
cv2.namedWindow("C3Filter")
cv2.namedWindow("Final")
cv2.namedWindow("Trackbars")

# Resizes Windows so they fit on the screen
cv2.resizeWindow("Trackbars", 400, 800)
cv2.resizeWindow("C1Filter", 240,250)
cv2.resizeWindow("C2Filter", 240,250)
cv2.resizeWindow("C3Filter", 240,250)

# Creates all 6 trackbars per color to have a total 18 trackers
# Is by default set to detect red
cv2.createTrackbar("C1HueMin", "Trackbars", 0, 180, lambda x: None)
cv2.createTrackbar("C1HueMax", "Trackbars", 255, 180, lambda x: None)
cv2.createTrackbar("C1SaturationMin", "Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C1SaturationMax", "Trackbars", 110, 255, lambda x: None)
cv2.createTrackbar("C1ValueMin", "Trackbars", 174, 255, lambda x: None)
cv2.createTrackbar("C1ValueMax", "Trackbars", 255, 255, lambda x: None)

# Is by default set to detect blue
cv2.createTrackbar("C2HueMin", "Trackbars", 116, 180, lambda x: None)
cv2.createTrackbar("C2HueMax", "Trackbars", 255, 180, lambda x: None)
cv2.createTrackbar("C2SaturationMin", "Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C2SaturationMax", "Trackbars", 110, 255, lambda x: None)
cv2.createTrackbar("C2ValueMin", "Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C2ValueMax", "Trackbars", 204, 255, lambda x: None)

# Is by default set to detect green
cv2.createTrackbar("C3HueMin", "Trackbars", 0, 180, lambda x: None)
cv2.createTrackbar("C3HueMax", "Trackbars", 255, 180, lambda x: None)
cv2.createTrackbar("C3SaturationMin", "Trackbars", 199, 255, lambda x: None)
cv2.createTrackbar("C3SaturationMax", "Trackbars", 255, 255, lambda x: None)
cv2.createTrackbar("C3ValueMin", "Trackbars", 0, 255, lambda x: None)
cv2.createTrackbar("C3ValueMax", "Trackbars", 190, 255, lambda x: None)

key_pressed = 1
# While loop will run while keypressed doesn't equal escape
while key_pressed != 27:
    ret, frame = cap.read()
    # using the HSV color sceme
    HSVimage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # Saves the position of the trackbars and there values for color 1
    C1HMin = cv2.getTrackbarPos("C1HueMin", "Trackbars")
    C1HMax = cv2.getTrackbarPos("C1HueMax", "Trackbars")
    C1SMin = cv2.getTrackbarPos("C1SaturationMin", "Trackbars")
    C1SMax = cv2.getTrackbarPos("C1SaturationMax", "Trackbars")
    C1VMin = cv2.getTrackbarPos("C1ValueMin", "Trackbars")
    C1VMax = cv2.getTrackbarPos("C1ValueMax", "Trackbars")

    # Saves the position of the trackbars and there values for color 2
    C2HMin = cv2.getTrackbarPos("C2HueMin", "Trackbars")
    C2HMax = cv2.getTrackbarPos("C2HueMax", "Trackbars")
    C2SMin = cv2.getTrackbarPos("C2SaturationMin", "Trackbars")
    C2SMax = cv2.getTrackbarPos("C2SaturationMax", "Trackbars")
    C2VMin = cv2.getTrackbarPos("C2ValueMin", "Trackbars")
    C2VMax = cv2.getTrackbarPos("C2ValueMax", "Trackbars")

    # Saves the position of the trackbars and there values for color 3
    C3HMin = cv2.getTrackbarPos("C3HueMin", "Trackbars")
    C3HMax = cv2.getTrackbarPos("C3HueMax", "Trackbars")
    C3SMin = cv2.getTrackbarPos("C3SaturationMin", "Trackbars")
    C3SMax = cv2.getTrackbarPos("C3SaturationMax", "Trackbars")
    C3VMin = cv2.getTrackbarPos("C3ValueMin", "Trackbars")
    C3VMax = cv2.getTrackbarPos("C3ValueMax", "Trackbars")

    # Creates a low and high limit for color 1
    lowerC1 = [C1HMin, C1SMin, C1VMin]
    upperC1 = [C1HMax, C1SMax, C1VMax]
    # Creates a low and high limit for color 2
    lowerC2 = [C2HMin, C2SMin, C2VMin]
    upperC2 = [C2HMax, C2SMax, C2VMax]
    # Creates a low and high limit for color 3
    lowerC3 = [C3HMin, C3SMin, C3VMin]
    upperC3 = [C3HMax, C3SMax, C3VMax]

    # turns them into numpy arrays
    lowerC1 = numpy.array(lowerC1, dtype="uint8")
    upperC1 = numpy.array(upperC1, dtype="uint8")
    lowerC2 = numpy.array(lowerC2, dtype="uint8")
    upperC2 = numpy.array(upperC2, dtype="uint8")
    lowerC3 = numpy.array(lowerC3, dtype="uint8")
    upperC3 = numpy.array(upperC3, dtype="uint8")

    # combines into mask which will hide what is higher than highC1 and lower than lowC1
    C1Mask = cv2.inRange(HSVimage, lowerC1, upperC1)
    # combines into mask which will hide what is higher than highC2 and lower than lowC2
    C2Mask = cv2.inRange(HSVimage, lowerC2, upperC2)
    # combines into mask which will hide what is higher than highC3 and lower than lowC3
    C3Mask = cv2.inRange(HSVimage, lowerC3, upperC3)



    # Creates into final filtered product
    filteredC1 = cv2.bitwise_and(frame, frame, mask=C1Mask)
    filteredC2 = cv2.bitwise_and(frame, frame, mask=C2Mask)
    filteredC3 = cv2.bitwise_and(frame, frame, mask=C3Mask)

    """filteredC1Grayscale = cv2.cvtColor(filteredC1, cv2.COLOR_BGR2GRAY)

    moments_C1 = cv2.moments(filteredC1Grayscale)

    if moments_C1["m00"] ==0:
        centroid_x_C1 = 1
        centroid_y_C1 = 1
    else:
        centroid_x_C1 = moments_C1["m10"]/moments_C1["m00"]
        centroid_y_C1 = moments_C1["m01"] / moments_C1["m00"]
    cv2.circle(filteredC1,(int(centroid_x_C1),int(centroid_y_C1)), 5, (255,255,255), -1)
"""
    filtered_1_grayscale = cv2.cvtColor(filteredC1, cv2.COLOR_BGR2GRAY)
    moments_1 = cv2.moments(filtered_1_grayscale)



    if moments_1["m00"] == 0:
        centroid_x_1 = 1
        centroid_y_1 = 1
    else:
        centroid_x_1 = moments_1["m10"]/ moments_1["m00"]
        centroid_y_1 = moments_1["m01"]/ moments_1["m00"]
    cv2.circle(filteredC1,(int(centroid_x_1), int(centroid_y_1)), 5,
               (255,255,255), -1)
    # combines al the filtered togethor to image
    combined = cv2.bitwise_or(filteredC1, filteredC2)
    combined = cv2.bitwise_or(combined, filteredC3)

    # Shows the data of the original, combined and filteered image
    cv2.imshow("Original", frame)
    cv2.imshow("C1Filter", filteredC1)
    cv2.imshow("C2Filter", filteredC2)
    cv2.imshow("C3Filter", filteredC3)
    cv2.imshow("Final", combined)

    # Will destory when escape is pressed
    keypressed = cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
