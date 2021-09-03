#! /usr/bin/python

import rospy
import time
import math
import tf
import roslib

def brodcaster(x,y,z,w):
    rospy.init_node('frame_a_to_frame_b_brodcaster_node',anonymous=False)
    time.sleep(0.5)
    bc=tf.TransformBroadcaster()
    
        # we need to brodcast translation,rotation and time
    quaternion=tf.transformations.quaternion_from_euler(x,y,z)
    translation=(0,0,0)
    Time=rospy.Time.now()

    bc.sendTransform(translation,quaternion,Time,"base_link","scan")

if __name__=="__main__":
    brodcaster(0.0,0.0,0.0,0.0)