# ROVER
ROVER package consist of basic navigation stack and slam packages,to control and move a rocker bogie based 6 wheel configuration indoors.


![rover 1](https://user-images.githubusercontent.com/60263608/131965500-0b2e144c-e649-4110-acc6-ee3781702648.jpg)
## Installation

```bash
cd ~/catkin_ws/src
git clone https://github.com/siddarth09/rover.git
git clone https://github.com/siddarth09/rover_description.git
cd ..
catkin_make
```
Note:
> Please change the catkin_ws to your custom rosworkspace name 

## TELE-OPERATION
The teleop keys are customised according to the robot configuration ie; the hardware bot, you can make changes to the friction between wheels or increase the max speed so the wheels of your bo motors can move faster

```bash
roslaunch rover teleop_key.launch
```

The above command can be used to run the teleop node in your pc 

## WORLD SIMULATION

This robot world can be simulated in Gazebo for testing various problems, the house contains three rooms with one narrow passage to check robot navigation in such conditions

To run the house simulation 
```bash
roslaunch rover rover_house.launch
```

## SLAM 
Simultaneous localization and mapping (SLAM) is the computational problem of constructing or updating a map of an unknown environment while simultaneously keeping track of an agent's location within it. Here we are using frontier mapping, gmapping, Hector-slam packages to map the given environment for navigation purposes

To run Gmapping package
``` bash
roslaunch rover gmapping.launch
```
To run Karto-SLAM package
```bash
roslaunch rover karto_slam.launch
```
To run Hector-slam package

Note:
>Please make sure your lidar ros package is publishing /scan topic 


``` bash
roslaunch rover hector_slam.launch
```
if there's any error pertaining to your map, check if you have connected your LiDAR properly.

## NAVIGATION STACK

Navigation stack is an important for autonomous navigation, ROS has builtin packages which helps you setup the entire navigation stack very easily and fine tune the
path planning algorithms accordingly. 

- GLOBAL COSTMAP:
  In the global costmap is everything the robot knows from previous visits and stored knowledge e.g. the map
  
- LOCAL COSTMAP:
 In the local costmap is everything that can be known from the current position with the sensors right know
 
Here ROS comes with default DWA or **DYNAMIC WINDOW APPROACH** which uses Dijkastra's algorithm to find the shortest path to the given X,Y coordinates

To run the navigation stack 

```bash
roslaunch rover navigation.launch map_file:=
```
#### MAKE SURE YOU HAVE MAPPED YOU ENVIRONMENT PROPERLY and SPECIFY THE MAP LOCATION AT MAP_FILE ARGUMENT 

## MAPVIZ 

Mapviz is a graphical user interface for gps based navigation. 
Installation:
```bash
cd ~/catkin_ws/src
git clone https://github.com/swri-robotics/mapviz.git
cd ..
catkin_make
```
To run the mapviz package
```bash
roslaunch rover mapviz.launch 
```
NOTE:
>If you want to change the latitude and longitude, you can go to google maps and get your coordinates


![DAY 89](https://user-images.githubusercontent.com/60263608/135597335-25901068-eda2-492b-8cde-9ea412dec134.JPG)


