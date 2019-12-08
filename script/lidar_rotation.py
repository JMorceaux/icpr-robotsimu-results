#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
   
def talker():
    pub = rospy.Publisher('/laser_velocity_controller/command', Float64, queue_size=10)
    rospy.init_node('lidar_rotation', anonymous=True)
    rate = rospy.Rate(1) # 10hz

    while not rospy.is_shutdown():
        velocity = 100
        pub.publish(velocity)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
