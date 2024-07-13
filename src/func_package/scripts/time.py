import rospy


def get_time():
    """获取当前时间"""
    rospy.init_node("node_time")
    time = rospy.Time.now()
    # 转成当前时刻
    rospy.loginfo("当前时刻:%.2f", time.to_sec())
    rospy.loginfo("当前时刻:%d", time.secs)


def set_time():
    """
    设置指定时刻
    """
    time_1 = rospy.Time(100.1)  # 离1970过去100秒。
    tim2 = rospy.Time(100, 321231123)  # 第二个参数指的是秒

    rospy.loginfo("指定时刻：%.2f", time_1.to_sec())
    rospy.loginfo("指定时刻：%.2f", tim2.to_sec())


def get_obj_time():
    """从某个时间值获取时间对喜爱嗯"""
    time3 = rospy.Time.from_sec(210.12)
    rospy.loginfo("指定时刻3：%.2f", time3.to_sec())


def set_duration_time():
    """程序执行时停顿5秒"""
    pass


if __name__ == "__main__":
    get_time()
    set_time()
    get_obj_time()
