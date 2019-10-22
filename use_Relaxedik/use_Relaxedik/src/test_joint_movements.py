#!/usr/bin/env python

import rospy
import time
from moveit_msgs.msg import MoveItErrorCodes

from moveit_python import MoveGroupInterface, PlanningSceneInterface

if __name__== '__main__':
	rospy.init_node('test_movement')
	move_group = MoveGroupInterface("arm_with_torso",'base_link')
	joint_names = ["torso_lift_joint", "shoulder_pan_joint",
                   "shoulder_lift_joint", "upperarm_roll_joint",
                   "elbow_flex_joint", "forearm_roll_joint",
                   "wrist_flex_joint", "wrist_roll_joint"]
	temp_pose = [[1],[2]]
	temp_pose[0] = [0.133, 0.8, 0.75, 0.0, -2.0, 0.0, 2.0, 0.0]
	temp_pose[1] = [0.133, -0.8, -0.75, 0.0, 2.0, 0.0, -2.0, 0.0]
	move_group = MoveGroupInterface("arm_with_torso", "base_link")
	joint_names = ["torso_lift_joint", "shoulder_pan_joint",
	               "shoulder_lift_joint", "upperarm_roll_joint",
	               "elbow_flex_joint", "forearm_roll_joint",
	               "wrist_flex_joint", "wrist_roll_joint"]
	for pose in temp_pose:
		move_group.moveToJointPosition(joint_names,pose,wait=True)
		move_group.get_move_action().wait_for_result()
		print 'Moved to pose'
	move_group.get_move_action().cancel_all_goals()
