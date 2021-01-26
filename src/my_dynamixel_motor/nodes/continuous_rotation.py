#! /usr/bin/env python

import rospy 
from std_msgs.msg import Float64
from dynamixel_msgs.msg import JointState

def main():
    rospy.init_node('continuous_rotation_node')
    def state_callback(msg):
        # msg = JointState()
    
        if msg.current_pos > 0.65:
            print(msg.current_pos)

            #rospy.loginfo("pubishing min value")
            value = Float64()
            value.data = -0.68
            pub.publish(value)
        elif msg.current_pos < -0.65:
            rospy.loginfo("pubishing max value")
            value = Float64()
            value.data = 0.68
            pub.publish(value)

    
        print(msg.current_pos)
        

    pub = rospy.Publisher('/pan_controller/command', Float64, queue_size=10)
    sub = rospy.Subscriber('/pan_controller/state', JointState, state_callback)
    rospy.loginfo("node started")
    rospy.spin()

if __name__ == "__main__":
    main()
