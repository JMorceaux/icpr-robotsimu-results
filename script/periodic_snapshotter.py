#!/usr/bin/env python
# license removed for brevity
import rospy

import roslib
roslib.load_manifest('laser_assembler')

from sensor_msgs.msg import PointCloud
from laser_assembler.srv import *
import time

def talker():
    pub = rospy.Publisher('/periodic_snapshotter', PointCloud, queue_size=10)
    rospy.init_node('periodic_snapshotter', anonymous=True)
    #rate = rospy.Rate(0.2) # 10hz
    time_before = rospy.Time(0,0)

    while not rospy.is_shutdown():
        rospy.wait_for_service("assemble_scans")

        try:
            clouds = rospy.ServiceProxy('assemble_scans', AssembleScans)
            resp = clouds(time_before,rospy.get_rostime())

	    time_before = rospy.get_rostime()


            pub.publish(resp.cloud)
        except:
            print("t'es nuul bobby")
        time.sleep(5)
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
