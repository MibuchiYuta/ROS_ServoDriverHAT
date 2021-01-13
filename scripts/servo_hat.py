#!/usr/bin/env python3

import rospy
import Adafruit_PCA9685

from std_msgs.msg import Int32

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

def main(pulse):
    servo_num = 0
    print('pulse =',pulse.data)
    while servo_num <= 15 :
        pwm.set_pwm(servo_num,0,pulse.data)
        servo_num += 1
    
if __name__ == '__main__': 
    rospy.init_node('pulse_out')
    sub = rospy.Subscriber('pulse', Int32, main) 
    rospy.spin()
