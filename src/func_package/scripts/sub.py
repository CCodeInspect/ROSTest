#! /usr/bin/env python3
import rospy
from std_msgs.msg import String

"""
sub
1.import;
2.init sub node;
3.create sub obj;
4.back call to solve data;
5.spin();

"""

res = None


def do_msg(msg):
    """
    pub msg
    func call
    """
    rospy.loginfo("sub data: %s", msg.data)
    res = msg.data


def create_self_sub_subscribe():
    rospy.init_node("node_sub_py")
    sub = rospy.Subscriber()
    rospy.spin()  # func call must be used


if __name__ == "__main__":
    create_self_sub_subscribe()
