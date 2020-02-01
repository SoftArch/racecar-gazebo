#!/usr/bin/python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

class worker:

    def __init__(self):

        self.bridge = CvBridge()
        rospy.Subscriber('/camera/zed/rgb/image_rect_color',Image,self.callback_SaveImage)
        rospy.spin()

    def callback_SaveImage(self,data):
        print('save calisti')
        cv2_img = self.bridge.imgmsg_to_cv2(data, "bgr8")
        cv2.imwrite('camera_image.jpeg', cv2_img)


if __name__ == '__main__':
    try:
        rospy.init_node('racecar_readimage',anonymous=True)
        w = worker()
    except rospy.ROSInterruptException: pass
