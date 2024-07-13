import rospy


def doMsg(event):
    rospy.loginfo("++++++++++++")
    rospy.loginfo("调用回调函数的时刻：%.2f", event.current_real.to_sec())


def create_time_scheduler():
    """创建定时器"""
    rospy.init_node("time_scheduler node")
    timer = rospy.Timer(rospy.Duration(2), doMsg)  # 创建定时器对象
    rospy.spin()


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
    """从某个时间值获取时间对象"""
    time3 = rospy.Time.from_sec(210.12)
    rospy.loginfo("指定时刻3：%.2f", time3.to_sec())


def set_duration_time():
    """程序执行时停顿5秒"""
    rospy.loginfo("开始休眠")
    dur = rospy.Duration(5)
    rospy.sleep(dur)
    rospy.loginfo("休眠结束")


def get_func_time():
    """
    获取一个时刻； t1
    设置持续时间； du1
    结束时刻； t2=t1+du1
    """
    dur = rospy.Duration(5)
    t1 = rospy.Time.now()
    du1 = rospy.Duration(5)

    t2 = t1 + du1
    rospy.loginfo("开始时刻：%.2f", t1.to_sec())
    rospy.loginfo("结束时刻：%.2f", t2.to_sec())

    du2 = dur + du1
    rospy.loginfo("持续时间：%.2f", du2.to_sec())


def get_dur_time():
    rospy.init_node("laalnode")
    time1 = rospy.Time.now()
    du1 = rospy.Duration(5)
    t = time1 + du1
    rospy.loginfo("开始时刻：%.2f", time1.to_sec())
    rospy.loginfo("结束时刻：%.2f", t.to_sec())


if __name__ == "__main__":
    # get_time()
    # set_time()
    # get_obj_time()
    # set_duration_time()
    # get_func_time()
    # get_dur_time()
    create_time_scheduler()
