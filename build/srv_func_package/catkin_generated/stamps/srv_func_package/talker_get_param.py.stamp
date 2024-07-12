#! /usr/bin/env python3

import rospy


"""
param find
"""


if __name__=='__main__':
    rospy.init_node("node_get_param")
    """1.get param"""
    res =rospy.get_param(param_name="key",default="123default")
    res1 =rospy.get_param(param_name="vvvvv",default="123default")

    # rospy.loginfo("res = : %s",res) #exists to return value
    # rospy.loginfo("res1 = : %s",res1) #not exists to return default

    res2 =rospy.get_param_cached(param_name="key",default="123default")
    res3 =rospy.get_param_cached(param_name="vvvvv",default="123default")
    
    # rospy.loginfo("res2 = : %s",res2) #exists to return value
    # rospy.loginfo("res3 = : %s",res3) #not exists to return default

    k = rospy.get_param_names() #return collections
    for i in k:
        rospy.loginfo("name = %s",i)


    flag1 = rospy.has_param("key1")
    if flag1:
        rospy.loginfo("key exists")
    else:
        rospy.loginfo('key not exists')


    res = rospy.search_param(param_name="key") #return key or None if not exists
    rospy.loginfo("res : %s",res)

    
