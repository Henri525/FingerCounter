import cv2
from cvzone.HandTrackingModule import HandDetector
import time

detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(1)

while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 0, 0, 0, 0]:
                number = "0"
            if fingerup == [0, 1, 0, 0, 0]:
                number = "1"
            if fingerup == [0, 1, 1, 0, 0]:
                number = "2"
            if fingerup == [0, 1, 1, 1, 0]:
                number = "3"
            if fingerup == [0, 1, 1, 1, 1]:
                number = "4"
            if fingerup == [1, 1, 1, 1, 1]:
                number = "5"


            cv2.putText(img, number, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.3)

video.release()
cv2.destroyAllWindows()