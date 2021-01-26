rosnode list
roscore
. devel/setup.bash
ls /dev/tty* or ./tty.sh
roslaunch dynamixel_tutorials main.launch 
	roslaunch dynamixel tutorials controller_manager.launch usb:=/dev/ttyUSB1

# Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001
roslaunch rplidar_ros rplidar_s1.launch usb:=/dev/ttyUSB0

rostopic pub /pan_controller/command std_msgs/Float64 "data: 0.68" -1

## old fiile - roslaunch my_dynamixel_motor tf_imu_actuator.launch

# publish tf from actuator to laser 
roslaunch my_dynamixel_motor tf_main.launch

# convert laser to point cloud
roslaunch laserscan_to_pointcloud2_conversion laserscan_to_pointcloud2_default.launch

// to check feedback
rostopic echo /pan_controller/state -n1

rviz -d src/my_dynamixel_motor/config.rviz

px4_sim
add sensor to URDF ... add sensor to Px4 ..  

