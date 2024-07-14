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


def call_back():
    rospy.loginfo("节点正在被关闭")


def pub():
    # init_node(name：设置节点名称,argv：封装节点调用时传递的参数,anonymous：为节点名称生成随机数据，解决节点名重名)
    rospy.init_node("node_selfdefine_pub")  # 在master中注册节点

    # Publisher()中的参数latch 为True时，发布方会保存最后一条消息，并且新的订阅者连接到发布方时，那么将最后一条消息发布给订阅者。
    pub = rospy.Publisher(name="topic_self_define", data_class=person, queue_size=10)

    self_define_data = person()
    self_define_data.name = "self_define_data_name"
    self_define_data.age = 18
    self_define_data.height = 190.1
    rate = rospy.Rate(1)
    count = 0
    while not rospy.is_shutdown():
        count += 1
        if count <= 10:
            pub.publish(self_define_data)
            rospy.loginfo(
                "pub self data: %s,%d,%f",
                self_define_data.name,
                self_define_data.age,
                self_define_data.height,
            )
        else:
            rospy.on_shutdown(call_back)
            rospy.signal_shutdown("关闭节点")
        rate.sleep()


if __name__ == "__main__":
    pub()
