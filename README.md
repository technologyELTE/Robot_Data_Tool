# Turtle Sim Practice

First Tutorial
[Turtle Sim Tutorial](https://davesroboshack.com/the-robot-operating-system-ros/ros2-topics/)

Second Turotial
[Gazebo Simulation](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/)

You can simulate your python program with this simulation. You don't need to have a real Turtlebot3 at all time.

# Turtlebot3 Motion Control
1. Clone the repository for getting the current position and orientation of the Turtlebot [Robot_Data_Tool](https://github.com/phuwanat-vg/robot_data_tool.git)
  ** git clone https://github.com/phuwanat-vg/robot_data_tool.git
   
   cd colcon_ws
   
   colcon build**
3. run the package with: **ros2 run robot_data_tool map_pose_provider**
   There is the ros2 topic of **/robot_map_pose/odom** to subscribe the **position** and **quaternian** of the current position of a Turtlebot3
4. Download motion_control.py [download here](https://github.com/technologyELTE/Robot_Data_Tool/blob/main/motion_control.py)
5. write a python program to control the Turtlebot3 Buuger/Waffle to complete the tasks with your own idea

# Check Points
1. Using SLAM technique to scan the environment and save the created map to ".yaml" file
2. Place the robot in any position in the environment and subscribe the current position of the robot
3. Manually control the robot by python programming
4. Automatically control the robot to desired goal point
   
Note: Write the python program to control Turtlebot from the starting point to the goal point
