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
def do_msg(msg):
    """pub msg
    func call
    """
    rospy.loginfo("sub data: %s",msg.data)



if __name__=='__main__':
    rospy.init_node("node_sub_py")
    sub =rospy.Subscriber(callback=do_msg,name="fang",data_class=String,queue_size=10)
    rospy.spin() #func call must be used 