#!/usr/bin/env python
import rospy
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import cv2
import time
from camera import RSD435

def measure_walloutlet(sensor, outlet_cascade, fps):
    img = sensor.color_image()
    H,W = sensor.image_size()

    # detect outles in gray image
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (3,3), 0)
    outlets = outlet_cascade.detectMultiScale(gray, 1.1, 20, minSize=(10,10))

    text_horizontal = 0
    for (x,y,w,h) in outlets:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        u = int(x + 0.5*w)
        v = int(y + 0.5*h)
        point3d = sensor.point3d(u,v)
        # print(point3d)
        # update the FPS counter
        fps.update()
        fps.stop()
        # information will be displayed on the frame
        info = [
            ("FPS", "{:.2f}".format(fps.fps())),
            ("x", "{:.2f}".format(point3d[0])),
            ("y", "{:.2f}".format(point3d[1])),
            ("z", "{:.2f}".format(point3d[2]))
        ]

        # loop over the info tuples and draw them on our frame
        for (i, (k, v)) in enumerate(info):
            text = "{}: {}".format(k, v)
            cv2.putText(img, text, (10 + text_horizontal*100, H - ((i * 20) + 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        text_horizontal += 1

    cv2.namedWindow("wall outlet measurement")
    img = cv2.resize(img, None, fx=1.5, fy=1.5)
    cv2.imshow('wall outlet measurement',img)
    cv2.waitKey(3)

if __name__ == '__main__':
    rospy.init_node("measure_walloutlet", anonymous=True, log_level=rospy.INFO)
    sensor = RSD435()
    outlet_cascade = cv2.CascadeClassifier('../classifier_usa/cascade.xml')
    fps = FPS().start()
    rate = rospy.Rate(10)
    try:
        while not rospy.is_shutdown():
            if sensor.ready():
                measure_walloutlet(sensor,outlet_cascade,fps)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
    cv2.destroyAllWindows()
