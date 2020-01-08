#!/usr/bin/python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDriveStamped

class worker:

    def __init__(self):
        self.msg = AckermannDriveStamped()
        #self.msg.drive.acceleration = 1
        #self.msg.drive.jerk = 1
        #self.msg.drive.steering_angle_velocity = 1
        self.speed = 0
        self.angle = 0
        self.od = 0.5

        rospy.Subscriber('/scan',LaserScan,self.callback_laser)

        self.pub = rospy.Publisher('/vesc/high_level/ackermann_cmd_mux/output', AckermannDriveStamped,queue_size=1)

        #while not rospy.is_shutdown():
        #    self.msg.drive.speed = self.speed
        #    self.msg.drive.acceleration = 1
        #    self.msg.drive.jerk = 1
        #    self.msg.drive.steering_angle = self.angle
        #    self.msg.drive.steering_angle_velocity = 1
        #    pub.publish(self.msg)
        self.msg.drive.speed = self.speed
        self.msg.drive.steering_angle = self.angle
        self.pub.publish(self.msg)
        rospy.spin()

    def callback_laser(self,data):
        print(min(data.ranges[175:185]))
        if min(data.ranges[90:270]) < self.od:
            self.speed = -0.5
            self.angle = 1
            self.od = 1
        else:
            self.angle = 0
            self.speed = 0.5
            self.od = 0.5

        self.msg.drive.speed = self.speed
        self.msg.drive.steering_angle = self.angle
        self.pub.publish(self.msg)


if __name__ == '__main__':
    try:
        rospy.init_node('racecar_driver',anonymous=True)
        w = worker()
    except rospy.ROSInterruptException: pass
