#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose


def callback(data):
    rospy.loginfo(data)


def turtle_pose_subscriber():
    rospy.init_node('turtle_pose_subscriber', anonymous=True)
    rospy.Subscriber('turtle1/pose', Pose, callback)
    rospy.spin()


if __name__ == '__main__':
    turtle_pose_subscriber()
