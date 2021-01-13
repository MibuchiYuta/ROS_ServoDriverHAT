#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def main():
    rospy.init_node ('deg_change')
    pub = rospy.Publisher('pulse', Int32, queue_size=1)

    deg = 0
    pulse = 0
    #rate = rospy.Rate(0.5)
    while not rospy.is_shutdown():
        deg = int(input('deg ='))
        pulse = int(deg * 470 / 180 + 100)
        print(pulse)
        pub.publish(pulse)
        #rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:pass
