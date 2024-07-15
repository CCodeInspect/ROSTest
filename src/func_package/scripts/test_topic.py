import pytest, rospy
from std_msgs.msg import String
from pub import create_pub
from sub import create_self_sub_subscribe


def test_pub_and_sub():
    pub = create_pub()
    sub = create_self_sub_subscribe()
    rospy.sleep(1)

    assert res == "hello"
