import cv2

cap = cv2.VideoCapture(0)


cv2.namedWindow("First Image")




while(True):
    ret, frame = cap.read()
    cv2.imshow("First Image", frame)

    key_pressed = cv2.waitKey(1)
    if key_pressed == 27:
        cap.release()
        cv2.destroyAllWindows()
        break

"""
import cv2

cap = cv2.VideoCapture(0)


cv2.namedWindow("First Image")



keypressed = 1
while keypressed != 27:
    ret, frame = cap.read()
    cv2.imshow("First Image", frame)
    keypressed = cv2.waitkey(30)


cap.release()
cv2.destroyAllWindows()
"""