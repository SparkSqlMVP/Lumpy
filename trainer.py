import os
import cv2
from PIL import Image
import numpy as np
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'sample pics'
def get_image(path):
    image_paths = [os.path.join(path,f) for f in os.listdir(path )]
    ID = []
    face = []
    for image_path in image_paths:
        face_img = Image.open(image_path).convert('L')
        faceNp = np.array(face_img,'uint8')
        id = int(os.path.split(image_path)[-1].split('.')[1])
        ID.append(id)
        face.append(faceNp)
        cv2.imshow('trainer',faceNp)
        cv2.waitKey(100)
    return np.array(ID) , face

ids, faces = get_image(path)

recognizer.train(faces,ids)
recognizer.save('recognizer/trainer.yml')
cv2.destroyAllWindows()