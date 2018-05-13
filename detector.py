import cv2
import mysql.connector
import numpy as np
face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer\\trainer.yml')
def getter(id):
    conn = mysql.connector.connect(host = 'localhost',
                                      database = 'faceDB',
                                      user = 'root',
                                      password='38LRh430')
    cmd = "select * from user_t where user_id="+str(id)
    curr = conn.cursor()
    curr.execute(cmd)
    profile = None

    for row in curr.fetchall():
        profile=row
    conn.close()
    return profile
while (True):
    grab, img = camera.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detect.detectMultiScale(gray_img,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),1)
        id, confidence = recognizer.predict(gray_img[y:y+h,x:x+w])
        profile = getter(id)
        print (profile)
        if(confidence<60):
            cv2.putText(img,profile[1],color=(0,255,0),org=(x,y),fontFace=18,fontScale=2)
        else:
            cv2.putText(img, "unknown", color=(0, 0, 255), org=(x, y), fontFace=18, fontScale=2)
    cv2.imshow("FaceDetector",img)
    if(cv2.waitKey(1)==ord('q')):
        break
camera.release()
cv2.destroyAllWindows()