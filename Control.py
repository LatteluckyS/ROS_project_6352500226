#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy
import time

def Move_right(req):
    print("Moved right")
    return EmptyResponse()

def Move_left(req):
    print("Moved left")
    return EmptyResponse()

def Move_up(req):
    print("Moved up")
    return EmptyResponse()

def Move_down(req):
    print("Moved down")
    return EmptyResponse()

def Stop(req):
    print("Stoped")
    return EmptyResponse()

def Home(req):
    rospy.init_node('Home')
    print("Arrived home...")
    return EmptyResponse()

def Auto(req):
    rospy.init_node('Auto_move')
    print("Using auto move")
    return EmptyResponse()

def Move_control():
    rospy.init_node('Move_control')
    s = rospy.Service('go_right', Empty , Move_right)
    s = rospy.Service('go_left', Empty , Move_left)
    s = rospy.Service('go_up', Empty , Move_up)
    s = rospy.Service('go_down', Empty , Move_down)
    s = rospy.Service('stop', Empty , Stop)
    s = rospy.Service('go_home', Empty , Home)
    s = rospy.Service('auto', Empty , Auto)
    print("moving...")
    time.sleep(1000)
    rospy.spin()

if __name__ == "__main__":
    Move_control()