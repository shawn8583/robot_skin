#!/usr/bin/python
#
# Publish ADC data over ROS.
#
# Visualize data of a 2D form in rqt_plot( in this case a 12 tectile pixels array made for M):
# $ rqt_plot /arduino/ADC/data[0] /arduino/ADC/data[1] /arduino/ADC/data[2] /arduino/ADC/data[3] /arduino/ADC/data[4] /arduino/ADC/data[5] /arduino/ADC/data[6] /arduino/ADC/data[7] /arduino/ADC/data[8]#  /arduino/ADC/data[9] /arduino/ADC/data[10] /arduino/ADC/data[11]
#
#
#


import serial

import roslib; roslib.load_manifest('robot_skin')
import rospy
from robot_skin.msg import FloatArray


def setup_serial(dev_name, baudrate):
    try:
        serial_dev = serial.Serial(dev_name, timeout=1.)
        if(serial_dev == None):
            raise RuntimeError("robotis_servo: Serial port not found!\n")

        serial_dev.setBaudrate(baudrate)
        serial_dev.setParity('N')
        serial_dev.setStopbits(1)
        #serial_dev.open()

        serial_dev.flushOutput()
        serial_dev.flushInput()
        return serial_dev

    except (serial.serialutil.SerialException), e:
        raise RuntimeError("robotis_servo: Something Wrong!\n")

def get_adc_data(serial_dev, num_adc_inputs):
    ln = serial_dev.readline()
    l = map(int, ln.split(','))
    if len(l) != num_adc_inputs:
        rospy.logwarn('Something fishy with the serial port.')
        serial_dev.flush()
        l = get_adc_data(serial_dev, num_adc_inputs)
    return l


if __name__ == '__main__':

    dev_name = '/dev/ttyACM0'

    baudrate = 115200

    serial_dev = setup_serial(dev_name, baudrate)

    pub = rospy.Publisher('/arduino/ADC', FloatArray)
    rospy.init_node('adc_publisher_node')

    for i in range(10):
        ln = serial_dev.readline()

    rospy.loginfo('Started publishing ADC data')

    while not rospy.is_shutdown():
        fa = FloatArray()
        fa.header.stamp = rospy.Time.now()
        fa.data = get_adc_data(serial_dev, 16)
        pub.publish(fa)

    serial_dev.close()


