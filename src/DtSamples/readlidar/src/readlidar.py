#!/usr/bin/python

import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
from dtmessage.msg import simple_dist

from numpy import inf

class worker:

    def __init__(self):
        rospy.Subscriber('/scan',LaserScan,self.callback_scan)

        # -- "Different topics with float32" --
        #self.pubLeftDist = rospy.Publisher('/readlidar/left_dist', Float32,queue_size=10)
        #self.pubCenterDist = rospy.Publisher('/readlidar/center_dist', Float32,queue_size=10)
        #self.pubRightDist = rospy.Publisher('/readlidar/right_dist', Float32,queue_size=10)
        # -- "Different topics with float32" --

        # -- "Different topics with custom msg" --
        self.pub = rospy.Publisher('/readlidar',simple_dist,queue_size=10)
        # -- "Different topics with custom msg" --

        print("racecar_readlidar is running")
        rospy.spin()

    def callback_scan(self,data):
        left = min(data.ranges[90:150])
        center = min(data.ranges[150:230])
        right = min(data.ranges[230:270])

        if(left == inf):
            left = 18;
        if(center == inf):
            center = 18;
        if(right == inf):
            right = 18;

        # -- "Different topics with float32" --
        #self.pubLeftDist.publish(left)
        #self.pubCenterDist.publish(center)
        #self.pubRightDist.publish(right)
        # -- "Different topics with float32" --

        # -- "Different topics with custom msg" --
        data = simple_dist()
        data.left = left
        data.center = center
        data.right = right
        self.pub.publish(data)
        # -- "Different topics with custom msg" --


if __name__ == '__main__':
    try:
        rospy.init_node('racecar_readlidar',anonymous=True)
        w = worker()
    except rospy.ROSInterruptException: pass
