import cv2
import numpy as np
import os
import sys

def modify_images(source, target, shape):
    if not os.path.exists(source):
        print(source, 'directory is not existed')
        return

    if not os.path.exists(target):
        os.makedirs(target)

    pic_num = 1
    for img in os.listdir(source):
        print(img)
        img = cv2.imread(source+"/"+img,cv2.IMREAD_GRAYSCALE)
        resized_image = cv2.resize(img,shape)
        cv2.imwrite(target+"/"+str(pic_num)+".jpg",resized_image)
        pic_num += 1

if __name__ == '__main__':
    source = sys.argv[1]
    target = sys.argv[2]
    shape = (int(sys.argv[3]), int(sys.argv[4]))
    modify_images(source,target,shape)
