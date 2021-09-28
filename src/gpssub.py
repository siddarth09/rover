#! /usr/bin/python

import rospy 
from sensor_msgs.msg import NavSatFix, NavSatStatus
from nav_msgs.msg import Odometry
from math import *
from geometry_msgs.msg import Point



lat=0.0
long=0.0

def gps_callback(msg):
    global lat,long 
    lat=msg.latitude
    long=msg.longitude
    
    

def mdeflat(lat0):
    lat0rad=radians(lat0)
    return (111132.09 - 566.05*cos(2.0*lat0rad)
            +1.20*cos(4.0*lat0rad)-0.002*cos(6.0*lat0rad))

def mdeflong(long0):
    lat0rad=radians(long0)
    return (1111415.13*cos(lat0rad)
            -94.55*cos(3.0*lat0rad)-0.12*cos(5.0*lat0rad))
def get_cartesian(lat=None,lon=None):
    lat, lon = radians(lat), radians(lon)
    R = 6371 # radius of the earth
    x = R * cos(lat) * cos(lon)
    y = R * cos(lat) * sin(lon)
    z = R *sin(lat)
    return x,y,z

def latlongtoxy():
    global lat,long
    lat0=lat
    long0=long
    pose=Point()
    pub=rospy.Publisher('gps/conversion',Point,queue_size=10)
    rate=rospy.Rate(20)
    while not rospy.is_shutdown():
        print("==============================\n")
        #print("LATITUDE:",lat)
        #print("LONGITUDE:",long)
        #x= (long-long0)*mdeflong(long0)
        #y=(lat-lat0)*mdeflat(lat0)
        #print("X:",x)
        #print("Y:",y)
        x,y,z=get_cartesian(lat,long)
        pose.x=x
        pose.y=y
        pose.z=z
        rospy.loginfo(pose)
        pub.publish(pose)
        rate.sleep()
        






if __name__=="__main__":
    rospy.init_node("gps_node")
    rospy.Subscriber('gps/fix',NavSatFix,gps_callback)
    latlongtoxy()
    rospy.spin()


