This package contains files to run relaxedIK, a neural network based IK solver for the Fetch robot.
# Running the RelaxedIK Solver

The command to launch the relaxedik node is:

roslaunch relaxed_ik relaxed_ik.launch

This will launch the barebones relaxedIK node which returns the required joint configuration space for the pose you desire. It will not move the robot to the pose you require.

To use the node, publish the desired pose to the topic “ /relaxed_ik/ee_pose_goals”. You will need to use a custom message type to publish to this topic called EEPoseGoals, the contents of which are given below.

Note: you likely will also need to have run the command "roslaunch fetch_moveit_config move_group.launch" in order to use the solutions produced by RelaxedIK and turn them into actual robot movements.
# Using RelaxedIK with Local Motion User Interfaces

In order to facilitate generating the correct Relaxed_IK solutions based on local motion commands, run the script "rosrun control_nodes relaxedik_vel_control.py".

Note: as of 5/2020, this script is very much a work in progress. However, it currently can enable control via joystick or general input of Twist commands. Until this is cleaned up, contact Connor for questions about using it. 
