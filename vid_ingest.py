import cv2
import time

stream_url = "rtsp://172.18.10.248:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif"

cap = cv2.VideoCapture(stream_url)

while True:
    ret, frame = cap.read()

    if not ret:
        print(" Cannot read frame")
        time.sleep(1)
        continue

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()