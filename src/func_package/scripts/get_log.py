import rospy, os, sys


# path = os.path.abspath(".")
sys.path.insert(0, "/home/vboxuser/demo_2/src/func_package/scripts")

import abc_vv


def get_log():
    rospy.logdebug("debug.........")
    rospy.loginfo("info........")
    rospy.logwarn("warn.........")
    rospy.logerr("err............")
    rospy.logfatal("fatal.........")
    rospy.loginfo("num_bb: %d", num_bb)


if __name__ == "__main__":
    get_log()
