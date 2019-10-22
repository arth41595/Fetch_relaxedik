#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped , Pose

class listener(object):
	def __init__(self):
		self.pose = Pose()

	def callback(self,data):
	    self.pose = data.pose
	    print(self.pose)

if __name__ == '__main__':
	rospy.init_node('listener', anonymous=True)
	listen = listener()
	rospy.Subscriber("/goal_state", PoseStamped, listen.callback)
