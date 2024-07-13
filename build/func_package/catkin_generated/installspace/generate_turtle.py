#！ /use/bin/env python3

"""
通过命令生成多个小乌龟
本质就是调用生成小乌龟的服务

0.获取服务的话题：rosservice list -> 返回 /spawn


1.通过话题获取消息类型字段Type：rosservice info /spawn

Node: /turtle1
URI: rosrpc://ROSnoetic:56323
Type: turtlesim/Spawn 
Args: x y theta name

2.通过Type获取消息格式： rosservice info [Type]

3.返回的消息格式就是响应结果

float32 x
float32 y
float32 theta
string name
---
string name


"""


import rospy
from turtlesim.srv import Spawn,SpawnRequest,SpawnResponse

if __name__=='__main__':
    rospy.init_node("node_client_python")
    client=rospy.ServiceProxy(name='/spawn',service_class=Spawn)
    
    #请求数据
    request = SpawnRequest()
    request.x=1.0
    request.y=2.22
    request.theta=59.1
    request.name="turtle_pauline"

    client.wait_for_service() #等待服务端
    try:
        response =client.call(request)
        rospy.loginfo("生成乌龟的名字叫：%s",response.name)
    except Exception as e:
        rospy.logerr("请求处理异常，请检查请求参数")