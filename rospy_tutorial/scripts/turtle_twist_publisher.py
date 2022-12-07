#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


def turtle_twist_publisher():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('turtle_pose_publisher', anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        twist = Twist()
        # Turtle movement in 2D and is governed by
        #   1 linear component (x-component)
        #   1 angular component (z-component)
        twist.linear.x = 1.0
        twist.angular.z = 1.0
        rospy.loginfo(twist)
        pub.publish(twist)
        rate.sleep()


def turtle_twist_publisher_spiral():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('turtle_pose_publisher', anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    linear = 0.1

    for i in range(300):
        linear += 0.01
        twist = Twist()
        twist.linear.x = linear
        twist.angular.z = 1.0
        rospy.loginfo(twist)
        pub.publish(twist)
        rate.sleep()


if __name__ == '__main__':
    try:
        turtle_twist_publisher()
    except rospy.ROSInterruptException:
        pass
