#! /usr/bin/env python3
import rospy
from std_msgs.msg import String  # pub data type

"""
1.import ;
2.init ros node;
3.create pub ojb;
4.pub logic and pub data;
5.source and rosrun pub.py must be executed in the same terminal!!!!!!!!!!!!!!!!!

"""


def create_pub():
    rospy.init_node("node_pub_py")  # node pub name
    pub = rospy.Publisher(
        name="fang", data_class=String, queue_size=10
    )  # create pub obj
    # data
    msg = String()
    # pub rate
    rate = rospy.Rate(1)

    # count
    count = 0

    # pub data
    rospy.sleep(5)  # sleep for sub all msg and not to lose msg 1-3
    while not rospy.is_shutdown():
        count += 1
        msg.data = "hello"  # add number
        pub.publish(msg)
        rospy.loginfo("pub data: %s", msg.data)
        rate.sleep()


if __name__ == "__main__":
    create_pub()
