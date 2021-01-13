#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def main():
    rospy.init_node ('deg_change')
    pub = rospy.Publisher('pulse', Int32, queue_size=1)

    deg = 0
    pulse = 0
    while not rospy.is_shutdown():
        deg = input('deg =')
        pulse = deg * 470 / 180 + 100
        print pulse
        pub.publish(pulse)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass