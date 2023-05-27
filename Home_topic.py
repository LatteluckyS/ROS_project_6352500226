#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def Home():
    pub = rospy.Publisher('stat_log', String, queue_size=10)
    rospy.init_node('Home', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        Message = "In Home : %s" % rospy.get_time()
        rospy.loginfo(Message)
        pub.publish(Message)
        rate.sleep()

if __name__ == '__main__':
    try:
        Home()
    except rospy.ROSInterruptException:
        pass