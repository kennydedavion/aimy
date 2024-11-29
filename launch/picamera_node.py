#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def picamera_publisher():
    rospy.init_node('picamera_publisher', anonymous=True)
    image_pub = rospy.Publisher('picamera/image_raw', Image, queue_size=10)
    bridge = CvBridge()

    cap = cv2.VideoCapture("/var/www/cam_pic_new")  # Nahraď cestou k picamera streamu
    rate = rospy.Rate(10)  # Frekvence publikování

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret:
            image_message = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            image_pub.publish(image_message)
        rate.sleep()

    cap.release()

if __name__ == '__main__':
    try:
        picamera_publisher()
    except rospy.ROSInterruptException:
        pass

