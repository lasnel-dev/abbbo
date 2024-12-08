import serial
import time
import cv2

arduino = serial.Serial('COM3', 9600)

time.sleep(2)

print("Connected to Arduino...")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap_height = 500
cap_width = 500

while True:
    ret, img = cap.read()
    face = face_cascade.detectMultiScale(img, 1.3)

    for (x, y, w, h) in face:
        cv2.rectangle(img,(x,y), (x+w,y+h), (0, 255, 0), 3)

        #
        # arr = {y: y + h, x: x + w}
        # print("----------------")
        # print("----------------")
        # print(arr)
        # print('X: %d      | Y:%d' % (x,y))
        # print('x+w %d       | y+h^ %d' % (x+w, y +h))
        #
        # xx = int(x + (x + h))/2
        # yy = int(y + (y + w))/2
        # center = (xx, yy)
        # print("Center of Rectangle: ", center)
        #
        # data = "X{0:d}Y{1:d}Z".format(xx, yy)
        # arduino.write(data)

    cv2.imshow('Stream', img)
    key = cv2.waitKey(20)
    if key == 27:
        print("Stop Streaming")
        break