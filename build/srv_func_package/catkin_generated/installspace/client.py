#! /usr/bin/env python3

import rospy
from srv_func_package.srv import AddInts,AddIntsRequest,AddIntsResponse
import sys
"""
client 

1.import;
2.init ros node;
3.create client;
4.data and send
5.response
"""

if __name__=='__main__':
    #judge len(params)==3
    if len(sys.argv)!=3:
        rospy.logerr("error: len(parms) must be 3")
        sys.exit(1)


    rospy.init_node("node_client")
    client=rospy.ServiceProxy(name="topic",service_class=AddInts)
    rospy.loginfo("client created !!")
    # client.wait_for_service() #wait server connect
    rospy.wait_for_service(service="topic") #equal to line 25,but need to topic
    response=client.call(int(sys.argv[1]),int(sys.argv[2])) #num1 = sys.argv[1],#num2=sys.argv[2],filename=sys.argv[0]
    rospy.loginfo("response: %d",response.sum)