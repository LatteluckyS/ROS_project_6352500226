#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy
import random
import time

command = ['go_left','go_right','go_up','go_down']

def auto_trigger():
    rospy.wait_for_service('auto')
    rospy.init_node('Auto_move')
    try:
        for c in range(10) : 
            sending = random.choice(command)
            passing = rospy.ServiceProxy(sending , Empty )
            print("Generating random command")
            resp1 = passing()
            time.sleep(1)
        passing = rospy.ServiceProxy('stop' , Empty)
        print("Finishing up auto mode")
        resp1 = passing()
        print("Done")
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    auto_trigger()