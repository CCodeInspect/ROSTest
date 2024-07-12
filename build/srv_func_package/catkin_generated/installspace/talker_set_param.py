#!/usr/bin/env python3


import rospy

"""
add and update

"""

if __name__ =='__main__':
    rospy.init_node("node_set_param")
    #add
    rospy.set_param(param_name="key",param_value="value")
    rospy.set_param(param_name="radius_key",param_value=0.15)
    
    #update
    res = rospy.set_param(param_name="key",param_value="update")
    rospy.loginfo("set successfully : %s ",res)