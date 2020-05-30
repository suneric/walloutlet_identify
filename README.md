# walloutlet_identify
identify walloutlet with RGB-D camera and iRobot

## Hardware
- iRobot Create 2
- Jetson TX 2
- Inter RealSense D435

## Prerequisite
- [Flush Linux to Jetson TX 2 (Linux-4.9.140-tegra)](https://docs.nvidia.com/sdk-manager/install-with-sdkm-jetson/index.html) 
- [Install ROS (melodic) on Jetson](http://wiki.ros.org/melodic/Installation/Ubuntu)
- [Install RealSense SDK 2.0 on Jetson](https://www.jetsonhacks.com/2018/04/25/now-cuda-intel-realsense-d400-cameras-nvidia-jetson-tx/)
- [Install RealSense ROS Package on Jetson](https://github.com/IntelRealSense/realsense-ros)
- [Install Autonomy Driver ROS Package on Jetson](https://github.com/AutonomyLab/create_autonomy)
- [ROS Network Setup](http://wiki.ros.org/ROS/NetworkSetup)

## Play
- Clone "walloutlet_autonomy" package to Jetson TX2 and start command `roslaunch walloutlet_autonomy setup.launch`
- Clone "walloutlet_measure" to ROS host machine and start command `python /walloutlet_measure/scripts/measure_walloutlet_ros.py`
- [Install teleop_twist_keyboard](http://wiki.ros.org/teleop_twist_keyboard) on ROS host machine and start commond `rosrun teleop_twist_keyboard teleop_twist_keyboard.launch` 
