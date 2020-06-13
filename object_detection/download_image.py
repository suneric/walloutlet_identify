#
import urllib
import cv2
import numpy as np
import os
import socket
import sys

socket.setdefaulttimeout(90) # in second

# download image from image-net.org and resize it in to specific shape
def store_raw_images(neg_img_link, start_index):
    neg_image_urls = urllib.urlopen(neg_img_link).read().decode('utf-8')
    if not os.path.exists('neg'):
        os.makedirs('neg')

    pic_num = start_index
    print('name download image starting from', pic_num)
    for i in neg_image_urls.split('\n'):
        print(pic_num, i)
        try:
            urllib.urlretrieve(i,"neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img,(100,100))
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    start_index = int(sys.argv[1])
    # structure: url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04341686'
    # creation: url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03183080'
    # animal beings url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n01905661'
    url = sys.argv[2]
    store_raw_images(url,start_index)
