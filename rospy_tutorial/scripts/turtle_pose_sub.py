#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose


def callback(data):
    rospy.loginfo("Turtle position %s", data.x, data.y)


def poser():
    rospy.init_node('poser', anonymous=True)
    rospy.Subscriber("/turtle1/pose", Pose, callback)
    rospy.spin()


if __name__ == '__main__':
    poser()
