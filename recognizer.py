import cv2
import numpy as np
import mysql.connector
from mysql.connector import Error

face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)
id = input("enter your id: ")
name = input("enter name for id "+str(id)+" ")
def insertDb(id,name):

        cmd = 'select * from user_t WHERE id='+str(id)+";"
        print(cmd)
        conn = mysql.connector.connect(host = 'localhost',
                                          database = 'faceDB',
                                          user = 'root',
                                          password='38LRh430')

        cur = conn.cursor()
        cur.execute(cmd)
        is_user = 0;
        for user in cur:
            is_user=1;
        values = (id, name)
        cmd1='update user_t set name =' + "\'" + name + "'" + " where id = " + str(id)
        print(cmd1)
        cmd = cmd1
        if is_user==1:
            cmd=('update user_t set name ='+"\'"+name+"'"+" where id = "+str(id))

        else:
            cmd = "insert into user_t values (" + values + ")"

        cur.execute(cmd)
        conn.commit()
        conn.close()
insertDb(id,name)
sampleNum=0
while (True):
    grab, img = camera.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detect.detectMultiScale(gray_img,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),1)
        cv2.imwrite('sample pics/user.'+str(id)+'.'+str(sampleNum)+'.jpg',gray_img[y:y+h,x:x+w])
        sampleNum+=1
        cv2.waitKey(10)
    cv2.imshow("FaceDetector",img)
    cv2.waitKey(1)
    if(sampleNum>20):
        break
camera.release()
cv2.destroyAllWindows()
print(faces)