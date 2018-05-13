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
   Verify
    $python
    Python 2.7.11 (default, Apr 26 2016, 13:18:56)
    [GCC 4.1.2 20080704 (Red Hat 4.1.2-54)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import mysql.connector
    >>>

# (4) Outline
This project consist of 3 parts, which are:
1、Creating datasets (mysqlcheck.py)
    Generate user faces images(20) and stored in mysql database;
2、Train the model (trainer.py)
    Generate "trainer.yml" file.
3、Face Recognition (recognizer.py)


# (5) How to run ?
1、Run in the command line the mysqlCheck.py for taking your face image as datasets. Don't forget to set each person's face to unique ID  
   UserID & UserName 
2、Train your datasets by running trainer.py
3、Lastly, run detector.py

# (5) Reading materials
   Face Detection using Haar Cascades, link: https://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
   OpenCV Documentation, link: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html
