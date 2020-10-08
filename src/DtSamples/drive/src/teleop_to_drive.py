#!/usr/bin/python

'''
This example includes transferring routing commands recevied from the turtlesim_teleop_key node to racecar.

First run turtlesim teleop. "rosrun tutlesim turtlesim_teleop_key".
Then run teleop_to_drive.py. "rosrun drive teleop_to_drive.py"
'''

import rospy
from geometry_msgs.msg import Twist
from ackermann_msgs.msg import AckermannDriveStamped

class worker:

    def __init__(self):
        self.speed = 0
        self.angle = 0
        self.od = 0.5

        rospy.Subscriber('/turtle1/cmd_vel',Twist,self.callback_laser)

        self.pub = rospy.Publisher('/vesc/high_level/ackermann_cmd_mux/input/nav_0', AckermannDriveStamped,queue_size=3)

        rate = rospy.Rate(20)

        while not rospy.is_shutdown():
            self.msg = AckermannDriveStamped()
            self.msg.drive.speed = self.speed;
            self.msg.drive.acceleration = 1;
            self.msg.drive.jerk = 1;
            self.msg.drive.steering_angle = self.angle;
            self.msg.drive.steering_angle_velocity = 1;
            self.pub.publish(self.msg)

            print(self.speed)
            print(self.angle)

            rate.sleep()
        rospy.spin()

    def callback_laser(self,data):
        '''Twist
            linear
            x: 2  | up arrow   | forward
            x: -2 | down arrow | back

            angular
            z: 2  | left arrow  | left
            z: -2 | right arrow | right
        '''
        if data.linear.x == 2 :     # forward
            if self.speed < 0:          # moving back
                self.speed = 0              # stop
            else:                       # not moving or moving forward
                self.speed = 0.5            # go forward
        elif data.linear.x == -2:   # back
            if self.speed > 0:          # moving forward
                self.speed = 0              # stop
            else:                       # not moving or moving back
                self.speed = -0.5           # go back

        if data.angular.z == 2:     # left
            if self.angle == 0:         # steering angle is zero
                self.angle = 1              # turn left
            elif self.angle < 0:        # steering angle is on the right
                self.angle = 0              # reset steering angle
        elif data.angular.z == -2:  # right
            if self.angle == 0:         # steering angle is zero
                self.angle = -1             # turn right
            elif self.angle > 0:        # steering angle is on the left
                self.angle = 0              # steering angle is zero

if __name__ == '__main__':
    try:
        rospy.init_node('racecar_driver',anonymous=True)
        w = worker()
    except rospy.ROSInterruptException: pass
