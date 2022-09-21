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


    # Object detecion
    class_ids, score, bboxes = model.detect(frame)
    for class_ids,score, bbox in zip(class_ids,score,bboxes):
        (x,y,w,h) = bbox
        print(x,y,w,h)
        cv2.putText(frame, str(class_ids), (x,y - 10), cv2.FONT_HERSHEY_PLAIN, 1,(200,0,50),2 )
        cv2.rectangle(frame,(x,y),(x+w, y+h),(200,0,50),3)


    print("class ids", class_ids)
    print("score", score)
    print("bboxes", bboxes)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) == ord("q"):
        break