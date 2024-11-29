#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def usb_camera_publisher():
    rospy.init_node('usb_camera_publisher', anonymous=True)
    image_pub = rospy.Publisher('usb_camera/image_raw', Image, queue_size=10)
    bridge = CvBridge()

    # Předpokládáme, že proud z USB kamery je k dispozici na `/var/www/cam_pic`
    cap = cv2.VideoCapture("/var/www/cam_pic")

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
        usb_camera_publisher()
    except rospy.ROSInterruptException:
        pass

