"""
Justin Garrity
10/29/20
Description: will capture image of the user
"""
#imported libreies
import cv2

# store the video capture into a variable
cap = cv2.VideoCapture(0)

# will create window for the image
cv2.namedWindow("First Image")

# read the video
ret, frame = cap.read()

#shows the image
cv2.imshow("First Image", frame)

key_pressed = cv2.waitKey(1)

#if esacpe key pressed then exit program
if key_pressed == 27:
    cap.release()
    cv2.destroyAllWindows()