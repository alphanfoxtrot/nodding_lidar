#! /usr/bin/env python

import rospy
from dynamixel_msgs.msg import JointState
from geometry_msgs.msg import TransformStamped
import tf2_ros
import tf_conversions

def main():
    rospy.init_node("actuator_laser_tf_pub_node")
    def state_cb(msg):
        # msg = JointState()
        # add condition for checking if value is available
        t = TransformStamped()
        t.header.stamp = rospy.Time.now()
        t.header.frame_id = "actuator"
        t.child_frame_id = "laser"
        t.transform.translation.x = 0.00029 # 29.74 mm = 0.00029m
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0002002
        
        q = tf_conversions.transformations.quaternion_from_euler(0, msg.current_pos, 0)

        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]
        br.sendTransform(t)
        print('braodcasting tf')





    sub = rospy.Subscriber("/pan_controller/state", JointState, state_cb)
    br = tf2_ros.TransformBroadcaster()
    print("node started")
    rospy.spin()

if __name__ == "__main__":
    main()
