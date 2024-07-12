#! /usr/env python3

import rospy

from srv_func_package.srv import AddInts,AddIntsRequest,AddIntsResponse
"""
    1.server;
    2.import srv;
    3.init ros node;
    4.create server obj;
    5.logic(call);
    6.spin();
"""


def do_nums(request):
    num1 = request.num1
    num2=request.num2
    sum = num1+num2
    response = AddIntsResponse()
    response.sum=sum
    rospy.loginfo("server : num1=%d,num2=%d,sum=%d",num1,num2,sum)
    return response


if __name__=='__main__':
    rospy.init_node("node_server_py")
    server = rospy.Service(name="topic",service_class=AddInts,handler=do_nums)
    rospy.loginfo("server started")
    rospy.spin()