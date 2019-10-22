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
class moveRobot(object):
	def __init__(self):
		self.move_delay = 0.2
		self.lastpose = []
		self.lasttime = time.time()
		self.need_plan = True
		self.joint_names = ["torso_lift_joint", "shoulder_pan_joint",
		           "shoulder_lift_joint", "upperarm_roll_joint",
		           "elbow_flex_joint", "forearm_roll_joint",
		           "wrist_flex_joint", "wrist_roll_joint"]
		self.move_group = MoveGroupInterface("arm_with_torso", "base_link")

	def callback(self,data):
		if data.angles != self.lastpose:
			self.lastpose = data.angles
			self.lasttime = time.time()
			self.need_plan = True

	def check_pose_updates(self):
		if(not(self.need_plan and time.time() - self.lasttime > self.move_delay)):
			return
		self.need_plan = False
		pose = [0,0,0,0,0,0,0,0]
		pose_data = self.lastpose
		for i in range(len(pose_data)):
			pose[i] = pose_data[i].data
		rospy.loginfo(rospy.get_caller_id() + " I heard %s", pose)		
		self.move_group.moveToJointPosition(self.joint_names,pose,wait=True)
		print 'Moved To New Pose'


if __name__ == '__main__':
	rospy.init_node('moveRobot',anonymous=True)
	motion = moveRobot()	
	rospy.Subscriber("/relaxed_ik/joint_angle_solutions", JointAngles, motion.callback)
	r = rospy.Rate(100)
	while not rospy.is_shutdown():
		motion.check_pose_updates()
		r.sleep()

