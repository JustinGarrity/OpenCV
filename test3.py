import cv2
import numpy

cv2.namedWindow("unchanged image")
cv2.namedWindow("COVER1")
cv2.namedWindow("Color-1-Trackbars")

# red
cv2.createTrackbar('COLOR1rmin', 'Color-1-Trackbars', 201, 255, lambda x: None)
cv2.createTrackbar('COLOR1rmax', 'Color-1-Trackbars', 255, 255, lambda x: None)

cv2.createTrackbar('COLOR1gmin', 'Color-1-Trackbars', 63, 255, lambda x: None)
cv2.createTrackbar('COLOR1gmax', 'Color-1-Trackbars', 255, 255, lambda x: None)

cv2.createTrackbar('COLOR1bmin', 'Color-1-Trackbars', 56, 255, lambda x: None)
cv2.createTrackbar('COLOR1bmax', 'Color-1-Trackbars', 255, 255, lambda x: None)

cap = cv2.VideoCapture(0)

keypress = 1

# in while loop
while (keypress != 27):
    ret, frame = cap.read()

    color1rmin = cv2.getTrackbarPos('COLOR1rmin', 'Color-1-trackbars')
    color1rmax = cv2.getTrackbarPos('COLOR1rmax', 'Color-1-trackbars')
    color1gmin = cv2.getTrackbarPos('COLOR1gmin', 'Color-1-trackbars')
    color1gmax = cv2.getTrackbarPos('COLOR1gmax', 'Color-1-trackbars')
    color1bmin = cv2.getTrackbarPos('COLOR1bmin', 'Color-1-trackbars')
    color1bmax = cv2.getTrackbarPos('COLOR1bmax', 'Color-1-trackbars')

    minimumcolor1 = [color1rmin, color1gmin, color1bmin]
    maximumcolor1 = [color1rmax, color1gmax, color1bmax]

    minimumcolor1 = numpy.array(minimumcolor1, dtype="uint8")
    maximumcolor1 = numpy.array(maximumcolor1, dtype="uint8")

    maskcolor1 = cv2.inRange(frame, minimumcolor1, maximumcolor1)

    cover1 = cv2.bitwise_or(frame, frame, mask=maskcolor1)

    cv2.imshow("unchanged image", frame)
    cv2.imshow("COVER1", cover1)

    # milliseconds to wait
    keypress = cv2.waitKey(1)

# out of while loop
cap.release()
cv2.destroyAllWindows()







