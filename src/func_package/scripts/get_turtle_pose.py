#! /usr/bin/env python3 

import rospy
from turtlesim.msg import Pose

"""
sub and output turtle pos2

1.import;
2,init ros node';
3.create sub obj;
4.recall;
5.spin();

"""

def do_pose(pose:Pose):
    rospy.loginfo("python sub-> wugui pose: location:(%.2f,%.2f),forward:%.2f,linear:%.2f,angular:%.2f",Pose.x,Pose.y,Pose.theta,Pose.linear_velocity,Pose.angular_velocity)

if __name__=='__main__':
    rospy.init_node("sub_post_p")
    sub =rospy.Subscriber(name="/turtle1/pose",data_class=Pose,callback=do_pose,queue_size=100)
    rospy.spin()
