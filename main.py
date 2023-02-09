import cv2
import os
import time
import uuid

IMAGES_PATH = 'Tensorflow/workspace/images/collectedimages'
labels = ['hello', 'thanks', 'yes']
number_imgs = 15

for label in labels:
    dir_path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    cap = cv2.VideoCapture(0)
    print("Collecting Images for {}".format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
