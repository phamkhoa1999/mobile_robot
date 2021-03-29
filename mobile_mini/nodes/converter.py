#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

SCALE_FACTOR_VEL  =  0.01
SCALE_FACTOR_ANG  =  0.0625

#What do you want to do
#Read pose from /turtle1/pos
#archieve /turtle1/cmd_vel
vx = 0
vy = 0
vth = 0
vel_pub_msg = Twist()
vel_pub = rospy.Publisher('/cmd_vel',Twist,queue_size= 10)

#define Subscriber
def callback(vel_sub_msg):
    global vx,vth
    global vel_pub_msg
    global vel_pub

    if (vel_sub_msg.linear.x < 0):
        vx = 0
    else:
        vx = vel_sub_msg.linear.x * SCALE_FACTOR_VEL
    vth = vel_sub_msg.angular.z * SCALE_FACTOR_ANG

    vel_pub_msg.linear.x = vx
    vel_pub_msg.angular.z = vth
    vel_pub.publish(vel_pub_msg)


#define Publisher
def subpub():
    rospy.init_node('converter',anonymous=True)
    rospy.Subscriber('/turtle1/cmd_vel',Twist,callback)

    vel_pub_msg.linear.y = 0
    vel_pub_msg.linear.z = 0

    vel_pub_msg.angular.x = 0
    vel_pub_msg.angular.y = 0
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rate.sleep()
    # rospy.spin()

if __name__ == '__main__':
    try:
        subpub()
    except rospy.ROSInterruptException:
        pass

        


     