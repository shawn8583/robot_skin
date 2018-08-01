#!/usr/bin/env python

# This script uses the functions got from curve fitting and outputs approximate value of N(newton) while the adc_publisher_node publishes value in range (0,1024]

import rospy
from robot_skin.msg import FloatArray

# define fitting functions
def y1(x):
    y1 = (3.28e+05)*(x**(-1.995)) + (-0.313)
    return y1

def y2(x):
    y2 = (2.707e+06)*x**(-2.439) + (0.09573)
    return y2

def y3(x):
    y3 = (2.488e+05)*x**(-2.037) + (-0.02024)
    return y3

def y4(x):
    y4 = (1.179e+06)*x**(-2.275) + (-0.142)
    return y4

def y5(x):
    y5 = (1.225e+06)*x**(-2.269) + (0.1806)
    return y5

def y6(x):
    y6 = (2.863e+04)*x**(-1.603) + (-0.3887)
    return y6

def y7(x):
    y7 = (1.94e+06)*x**(-2.344) + (-0.07228)
    return y7

def y8(x):
    y8 = (4.25e+05)*x**(-2.088) + (0.008193)
    return y8

def y9(x):
    y9 = (2.008e+06)*x**(-2.403) + (0.2517)
    return y9

def y10(x):
    y10 = (1.958e+06)*x**(-2.368)
    return y10

def y11(x):
    y11 = (158) / (x - 137.5)
    return y11

def y12(x):
    y12 = (4888)*x**(-1.267) + (-0.9634)
    return y12

# convert values to Newton
def callback(data):
    #rospy.loginfo('data.data')
    print data.data
    n1 = y1(data.data[0])
    n2 = y2(data.data[1])
    n3 = y1(data.data[2])
    n4 = y1(data.data[3])
    n5 = y1(data.data[4])
    n6 = y1(data.data[5])
    n7 = y1(data.data[6])
    n8 = y1(data.data[7])
    n9 = y1(data.data[8])
    n10 = y1(data.data[9])
    n11 = y1(data.data[10])
    n12 = y1(data.data[11])
    print(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/arduino/ADC", FloatArray, callback) 
    # This declares that this node subscribes to the /arduino/ADC topic which is of type FloatArray.msg. 
    # *When new messages are received, callback is invoked with the message as the first argument.
    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped

if __name__ == '__main__':
    listener()


# Reference: https://www.ncnynl.com/archives/201611/1059.html
#            http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber(python)
#            https://cloud.tencent.com/developer/ask/31510  # summary of printing multiple stuff in python
