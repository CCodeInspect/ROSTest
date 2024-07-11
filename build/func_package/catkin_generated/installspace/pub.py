#! /usr/bin/env python3
import rospy
from std_msgs.msg import String #pub data type

"""
1.import ;
2.init ros node;
3.create pub ojb;
4.pub logic and pub data;

"""


if __name__=='__main__':
    rospy.init_node("node_pub") #node pub name    
    pub= rospy.Publisher(name="fang",data_class=String,queue_size=10)#create pub obj
    #data
    msg=String()

    #pub data
    while not rospy.is_shutdown():
        msg.data="hello"
        pub.publish(msg)


