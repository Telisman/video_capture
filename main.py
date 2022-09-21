import cv2
# open dnn
net =cv2.dnn.readNet("dnn_model/yolov4-tiny.weights","dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size = (320,320),scale = 1/255)

# Set camera
cap = cv2.VideoCapture(0)
while True:

    # Get frame
    rat, frame = cap.read()



    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) == ord("q"):
        break