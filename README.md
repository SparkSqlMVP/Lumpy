# (1) System name Lumpy 1.0
Face Recognition using Haar-Cascade Classifier, OpenCV, and Python

# (2) Requirement
Python 3.5

OpenCV 3.1.0

Numpy

# (3) Tips
1、you need set up "mysql-essential-5.1.73-win32.msi" on your server, because some data i will insert into facedb;

2、set up mysql then python can connect mysql

   c:-> pip install mysql-connector-python-rf
   
   # Verify
   
    $python
    
    Python 2.7.11 (default, Apr 26 2016, 13:18:56)
    
    [GCC 4.1.2 20080704 (Red Hat 4.1.2-54)] on linux2
    
    Type "help", "copyright", "credits" or "license" for more information.
    
    >>> import mysql.connector
    
    >>>


# (4) Outline

This project consist of 4 parts, which are:

1、Create table

   CREATE TABLE user_t (

   id INT,

   NAME VARCHAR(200),

   user_id INT NOT NULL AUTO_INCREMENT,

   ctime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

   PRIMARY KEY (user_id)

   )


2、Creating datasets (mysqlcheck.py)

    Generate user faces images(20) and stored in mysql database;
    
3、Train the model (trainer.py)

    Generate "trainer.yml" file.
    
4、Face Recognition (recognizer.py)



# (5) How to run ?

1、Run in the command line the mysqlCheck.py for taking your face image as datasets. 

   Don't forget to set each person's face to unique ID  

   UserID & UserName 
   
2、Train your datasets by running trainer.py

3、Lastly, run detector.py


# (5) Reading materials

Face Detection using Haar Cascades, link: https://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html

OpenCV Documentation, link: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html


# (5) video

https://www.youtube.com/watch?v=OqHZmc59zZk&index=9&list=PLwf-FOF-JvAfvIwJc-htjZ2tuucf2cwDh&t=0s

![image](https://github.com/SparkSqlMVP/Lumpy/blob/master/face%20recognition.gif)

