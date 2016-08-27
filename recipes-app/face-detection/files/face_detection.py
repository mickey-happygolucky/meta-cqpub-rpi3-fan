import numpy as np
import cv2 
import RPi.GPIO as GPIO

class StatusManager:
    def __init__(self):
        self._flag = False
        self._prev = False
        self._font_type = cv2.FONT_HERSHEY_PLAIN
        self._motor_in1 = 20
        self._motor_in2 = 21
        GPIO.setup(self._motor_in1, GPIO.OUT)
        GPIO.setup(self._motor_in2, GPIO.OUT)
        GPIO.output(self._motor_in2, False)

    def draw(self, img):
        if self._flag == True:
            cv2.putText(img, 'On', (0, 80), self._font_type, 3, (0,0,255), 3)
        else:
            cv2.putText(img, 'Off', (0, 80), self._font_type, 3, (0,0,255), 3)

    def set(self, onoff):
        if (self._prev != onoff):
            self._flag = onoff
            GPIO.output(self._motor_in2, onoff)
        self._prev = onoff

def mosaic(img):
    h, w = img.shape[0], img.shape[1]
    img = cv2.resize(img, (w/10, h/10))
    img = cv2.resize(img, (w, h), interpolation=cv2.INTER_NEAREST)
    return img

if __name__ == "__main__":

    GPIO.setmode(GPIO.BCM)
    face_cascade = cv2.CascadeClassifier(
        '/usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')

    cap = cv2.VideoCapture(0)
    status = StatusManager()

    while(True):
        _,img = cap.read()
        status.draw(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        height, width = gray.shape[0], gray.shape[1]
        gray = cv2.resize(gray, (width/2, height/2))
        faces = face_cascade.detectMultiScale(gray, 
                                              scaleFactor=1.1, minNeighbors=3,
                                              minSize=(30, 30), maxSize=(150,150), 
                                              flags = cv2.CASCADE_SCALE_IMAGE)

        if len(faces):
            status.set(True)
        else:
            status.set(False)

        for (x,y,w,h) in faces:
            cx,cy,cw,ch = x*2,y*2,w*2,h*2 # c means color
            cv2.rectangle(img,(cx,cy),(cx+cw,cy+ch), (255,0,0),2)
            roi = img[cy:cy+ch, cx:cx+cw]
            img[cy:cy+ch, cx:cx+cw] = mosaic(roi)

        cv2.imshow('face detection', img)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
