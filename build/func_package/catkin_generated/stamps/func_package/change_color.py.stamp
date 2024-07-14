import rospy

"""
修改小乌龟gui背景色
"""


def change_color():
    rospy.init_node("node_change_color")
    # 修改背景色
    rospy.set_param(param_name="/turtlesim/background_r", param_value=100)
    rospy.set_param(param_name="/turtlesim/background_g", param_value=50)
    rospy.set_param(param_name="/turtlesim/background_b", param_value=200)


if __name__ == "__main__":
    change_color()
