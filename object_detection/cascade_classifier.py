import numpy as np
import cv2
import sys

model_cascade = 0

def image_classfy(source):
    src = cv2.imread(source,cv2.IMREAD_COLOR)
    img = cv2.imread(source,cv2.IMREAD_GRAYSCALE)
    objs = model_cascade.detectMultiScale(img,1.3,3)# scale, neigbor)
    for (x,y,w,h) in objs:
        cv2.rectangle(src,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('img',src)
    while 1:
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

if __name__ == '__main__':
    cascade_file = sys.argv[2]
    model_cascade = cv2.CascadeClassifier(cascade_file)
    source = sys.argv[1]
    image_classfy(source)
    cv2.destroyAllWindows()
