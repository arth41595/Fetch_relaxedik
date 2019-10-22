#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from use_Relaxedik.msg import EEPoseGoals
from use_Relaxedik.msg import JointAngles
from geometry_msgs.msg import Pose
import roslaunch
import time
from moveit_python import MoveGroupInterface, PlanningSceneInterface

#Listen
def callback(data):
	joint_names = ["torso_lift_joint", "shoulder_pan_joint",
	               "shoulder_lift_joint", "upperarm_roll_joint",
	               "elbow_flex_joint", "forearm_roll_joint",
	               "wrist_flex_joint", "wrist_roll_joint"]
	move_group = MoveGroupInterface("arm_with_torso", "base_link")
	pose = [0,0,0,0,0,0,0,0]
	pose_data = data.angles
	for i in range(len(pose_data)):
		pose[i] = pose_data[i].data
	rospy.loginfo(rospy.get_caller_id() + " I heard %s", pose)
	
	move_group.moveToJointPosition(joint_names,pose,wait=True)
	print 'Moved To New Pose'
    
def listener():
	rospy.init_node('get_orientation',anonymous=True)
	
	

	rospy.Subscriber("/relaxed_ik/joint_angle_solutions", JointAngles, callback)

	rospy.spin()

if __name__ == '__main__':
    listener()

