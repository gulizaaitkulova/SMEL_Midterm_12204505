# Fleet Management
This the code for the ROS2 Fleet management project. The project allows to make a connection between client and server using ROS2.

In order to run the project, please download the "dynamic_fleet_management" and "fleet_action_interfaces" packages into your ROS2 workspace. Then you need to build the packages using the following commands

colcon build --packages-select dynamic_fleet_management
colcon build --packages-select fleet_action_interfaces

sourcing
source install/setup.bash

running the server in one terminal
ros2 run dynamic_fleet_management server

running the client in one terminal
ros2 run dynamic_fleet_management client

![Alt text](photo_2023-10-21_07-30-57.jpg)
