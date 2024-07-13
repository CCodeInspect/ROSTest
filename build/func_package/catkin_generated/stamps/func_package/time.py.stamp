import rospy



def get_time():
    """获取当前时间"""
    rospy.init_node("node_time")
    time = rospy.Time.now()
    #转成当前时刻
    rospy.loginfo("当前时刻:%.2f",time.to_sec())
    rospy.loginfo("当前时刻:%d",time.secs)


def set_time():
    """
    设置指定时刻
    """
    time_1=rospy.Time(100)#离1970过去100秒。
    rospy.loginfo("距离1970逝去 %2f",time_1)
    tim2 =rospy.Time(100,32123123123)#第二个参数指的是秒
    rospy.loginfo("距离1970逝去 %d",tim2)





if __name__=='__main__':
    get_time()
    set_time()
    
