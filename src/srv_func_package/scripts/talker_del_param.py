#! /usr/env python3


import rospy



if __name__=='__main__':
    rospy.init_node("node_del")
    try:

        rospy.delete_param(param_name="key")
        rospy.loginfo("del successfully!")
    except Exception as e:
        rospy.loginfo("del obj does not exists!!please add obj!!")