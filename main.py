import cv2

cap = cv2.VideoCapture(0)

while True:
    rat, frame = cap.read()
    cv2.imshow("Frame",frame)
    cv2.waitKey(1)