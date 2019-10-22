#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from use_Relaxedik.msg import EEPoseGoals
from use_Relaxedik.msg import JointAngles
from geometry_msgs.msg import Pose, PoseStamped
import roslaunch
import time
from moveit_python import MoveGroupInterface, PlanningSceneInterface


def callback_posegoal(data):
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
		print ('Moved To New Pose')

def callback_rosbridge(data):
		global pose
		pose = data.pose
		pose.orientation.w = 0.707
		pose.orientation.x = 0
		pose.orientation.y = 0.707
		pose.orientation.z = 0
		rospy.loginfo('New Pose received',pose)
    
if __name__ == '__main__':
	rospy.init_node('teleop',anonymous=True)
	rate = rospy.Rate(1)
	publisher_to_relaxed = rospy.Publisher('/relaxed_ik/ee_pose_goals', EEPoseGoals, queue_size=3)
	

	while not rospy.is_shutdown():
		pose = Pose()
		rospy.Subscriber("/goal_state", PoseStamped, callback_rosbridge)
		ee_pose_goal = EEPoseGoals()
		ee_pose_goal.header.seq = 0
		ee_pose_goal.ee_poses.append(pose)
		publisher_to_relaxed.publish(ee_pose_goal)

		rospy.Subscriber("/relaxed_ik/joint_angle_solutions", JointAngles, callback_posegoal)
		rate.sleep()

