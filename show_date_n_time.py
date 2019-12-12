import cv2
import datetime

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

w = str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()

    if ret != True: break

    datet = str(datetime.datetime.now())
    cv2.putText(frame, datet, (10, 20), font, 0.5, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
