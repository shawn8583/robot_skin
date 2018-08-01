#!/usr/bin/env python

# This script uses the functions got from curve fitting and outputs approximate value of N(newton) while the adc_publisher_node publishes value in range (0,1024]

import rospy
from robot_skin.msg import FloatArray

def callback(data):
    rospy.loginfo('data.data')

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/arduino/ADC", FloatArray, callback)
    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped

if __name__ == '__main__':
    listener()


# Reference: https://www.ncnynl.com/archives/201611/1059.html
#            http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber(python)
