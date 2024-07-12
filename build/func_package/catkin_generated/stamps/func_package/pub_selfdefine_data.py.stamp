#! /usr/bin/env python3

import rospy
from func_package.msg import person

"""
define pub ->>self define msg

1.import ;
2.init ros node;
3.create pub obj;
4.create pub logic and pub msg;

"""


if __name__=='__main__':
    rospy.init_node("node_selfdefine")
    pub = rospy.Publisher(name="topic_self_define",data_class=person,queue_size=10)
    self_define_data = person()
    self_define_data.name="self_define_data_name"
    self_define_data.age=18
    self_define_data.height=190.1
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(self_define_data)
        rate.sleep()
        rospy.loginfo("pub self data: %s,%d,%f",self_define_data.name,self_define_data.age,self_define_data.height)
        