# Turtle Sim Practice
[Turtle Sim Tutorial](https://davesroboshack.com/the-robot-operating-system-ros/ros2-topics/)

You can simulate your python program with this simulation. You don't need to have a real Turtlebot3 at all time.

# Turtlebot3 Motion Control
1. Clone the repository for getting the current position and orientation of the Turtlebot [Robot_Data_Tool](https://github.com/phuwanat-vg/robot_data_tool.git)
2. run the package with: ros2 run robot_data_tool map_pose_provider
3. Download motion_control.py [download here](https://github.com/technologyELTE/Robot_Data_Tool/blob/main/motion_control.py)
4. write a python program to control the Turtlebot3 Buuger/Waffle to complete the tasks with your own idea

# Taks
1. Using SLAM technique to scan the environment
2. Save the created map to ".yaml" file
3. Place the robot in any position in the environment
4. Manually or Automatic control the robot to desired starting point
5. Determine the goal point
6. Write the python program to control Turtlebot from the starting point to the goal point
7. There will be an unknown obstacle between line of sight, the turtlebot should avoid the obstacle until it reaches the goal 
