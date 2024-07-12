# ! /usr/bin/env python3


import rospy
from func_package.msg import person

def do_call(person):
    rospy.loginfo("sub data: %s,%d,%f",person.name,person.age,person.height)


if __name__=='__main__':
    """sub"""
    rospy.init_node("node_selfdefine_sub")
    sub = rospy.Subscriber(name="topic_self_define",data_class=person,queue_size=10,callback=do_call)
    rospy.spin() #notic fun call
