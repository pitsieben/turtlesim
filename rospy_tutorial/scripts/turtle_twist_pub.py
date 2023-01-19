#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist


def twister():
    pub_topic_name = '/turtle1/cmd_vel'
    pub = rospy.Publisher(pub_topic_name, Twist, queue_size=10)
    rospy.init_node('Turtle twister', anonymous=True)
    velocity_msg = Twist()
    while not rospy.is_shutdown():
        velocity_msg.linear.x = 0.5
        velocity_msg.linear.y = 0.5
        print(velocity_msg)
        pub.publish(velocity_msg)


if __name__ == '__main__':
    try:
        twister()
    except rospy.ROSInterruptException:
        pass
