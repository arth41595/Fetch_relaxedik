#!/usr/bin/env python
import rospy
from use_Relaxedik.msg import EEPoseGoals
from geometry_msgs.msg import Pose
import roslaunch
import time

#Talk
def talker():
    ee_pose_goals_pub = rospy.Publisher('/relaxed_ik/ee_pose_goals', EEPoseGoals, queue_size=3)
    rospy.init_node('publish_test', anonymous=True)
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():
		ee_pose_goals = EEPoseGoals()
		ee_pose_goals.header.seq = 0
		p = Pose()
		p.position.x = -0.5
		p.position.y = 0.4
		p.position.z = -0.3
		p.orientation.w = 0.707
		p.orientation.x = 0
		p.orientation.y = 0.707
		p.orientation.z = 0
		ee_pose_goals.ee_poses.append(p)
		ee_pose_goals_pub.publish(ee_pose_goals)
		rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

