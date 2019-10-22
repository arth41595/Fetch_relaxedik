#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from use_Relaxedik.msg import EEPoseGoals
from use_Relaxedik.msg import JointAngles
from geometry_msgs.msg import Pose, PoseStamped
import roslaunch
import time
from moveit_python import MoveGroupInterface, PlanningSceneInterface

move_delay = 0.5

class teleop(object):
	def __init__(self):
		self.lastpose = Pose()
		self.lasttime = time.time()
		self.need_plan = True
		self.move_group = MoveGroupInterface("arm_with_torso", "base_link")

	def callback_rosbridge(self,data):		
		if data.pose != self.lastpose:
			self.lastpose = data.pose
			self.lasttime = time.time()
			self.need_plan = True

	def check_pose_updates(self):
		if(not(self.need_plan and time.time() - self.lasttime > move_delay)):
			return
		self.need_plan = False
		pose_goal = self.lastpose
		gripper_frame = 'wrist_roll_link'
		gripper_pose_stamped = PoseStamped()
		gripper_pose_stamped.header.frame_id = 'base_link'
		gripper_pose_stamped.header.stamp = rospy.Time.now()
		gripper_pose_stamped.pose = pose_goal
		self.move_group.moveToPose(gripper_pose_stamped,gripper_frame)			
		print ('Moved To New Pose')

if __name__ == '__main__':
	rospy.init_node('teleop',anonymous=True)
	teleop = teleop()
	rospy.Subscriber("/goal_state", PoseStamped, teleop.callback_rosbridge)
	r = rospy.Rate(100)
	while not rospy.is_shutdown():
		teleop.check_pose_updates()
		r.sleep()
		rospy.spinOnce()
	
    
	
				

