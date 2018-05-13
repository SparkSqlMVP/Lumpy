import mysql
from mysql.connector import Error
import cv2
face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)
def connect(id,name):
    try:
        conn= mysql.connector.connect(host = '127.0.0.1',
                                      database = 'faceDB',
                                      user = 'root',
                                      password='38LRh430')
        curr = conn.cursor()
        cmd = "select * from user_t where id = "+str(id)

        values = str(id)+", \'"+str(name)+"'"
        cmd = "insert into user_t(id,name) values (" + values + ")"
        curr.execute(cmd)
        conn.commit()
    except Error as e :
        print(e)
    finally:
        conn.close()
id = input("enter your id: ")
name = input("enter name for id " + str(id) + " ")
connect(id=id,name=name)
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
import trainer