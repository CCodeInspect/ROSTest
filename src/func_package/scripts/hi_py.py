#! /usr/bin/env python
import rospy


def hi():
    rospy.init_node("firstnode")
    rospy.loginfo("py start~~")
    rospy.loginfo("py end ~~")


if __name__ == "__main__":
    hi()
