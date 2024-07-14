#! /usr/bin/env python3


import rospy
from geometry_msgs.msg import Twist

"""
1.pub msg;
2.topic: /turtle1/cmd_vel;
3.msg:geometry_msgs/Twist;
4.import ;
5.init node;
6.create pub obj;
7.data and pub msg;

"""


def pub_turtle():
    rospy.init_node("node_circle")
    pub_turtle = rospy.Publisher(
        name="/turtle1/cmd_vel", data_class=Twist, queue_size=10
    )

    rate = rospy.Rate(5)
    twist = Twist()
    twist.linear.x = 1
    twist.linear.y = 0
    twist.linear.z = 0

    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = 1

    while not rospy.is_shutdown():
        pub_turtle.publish(twist)
        rate.sleep()
        rospy.loginfo("gui gui start~")


if __name__ == "__main__":
    pub_turtle()
