#!/usr/bin/env python

import rospy
import random as rm
import numpy as np
from std_msgs.msg import Float32, Float64MultiArray, MultiArrayDimension
from geometry_msgs.msg import Twist, Pose2D
from nav_msgs.msg import Odometry
from tf.transformations import quaternion_from_euler
from mini_challenge_1.srv import *
from mini_challenge_2.srv import *
import rospkg
import os
import json

class OdometryNode():
    
    def __init__(self, initial_x = 0.0, initial_y = 0.0, initial_theta = 0.0):
        
        # ______________ init node publishers, subscribers and services ______________
        rospy.init_node('odometry')        
        self.wr_sub = rospy.Subscriber('/wr', Float32, self.puzzlebot_wr_callback)
        self.wl_sub = rospy.Subscriber('/wl', Float32, self.puzzlebot_wl_callback)        
        self.puzzlebot_odom_pub = rospy.Publisher('/odom/ghost', Odometry, queue_size=1)        
        self.reset_puzzlebot_service_result = rospy.Service("reset_odometry", ResetOdometry, self.reset_odometry)        
        
        # ______________ fill in publisher messages ______________
        self.initial_x, self.initial_y, self.initial_theta = (initial_x, initial_y, initial_theta)        
        self.puzzlebot_estimated_pose = Odometry()        
        self.fill_odometry_header()        
        self.puzzlebot_estimated_pose.pose.pose.position.x, self.puzzlebot_estimated_pose.pose.pose.position.y = (self.initial_x, self.initial_y)        
        self.puzzlebot_estimated_rot = self.initial_theta   
        self.first_time_with_w = True     
        
        # ______________ init nav variables ______________
        self.puzzlebot_estimated_rot_quaternion = None
        self.last_sampling_time = None        
        self.puzzlebot_wheel_rad = 0.057 # radius
        self.puzzlebot_wheel_to_wheel_dist = 0.192 # length
        self.puzzlebot_wr = None
        self.puzzlebot_wl = None
        self.v = 0.0
        self.w = 0.0

        # ______________ init rate ______________
        self.rate = rospy.Rate(20.0)            

    def reset_odometry(self, req):
        self.puzzlebot_estimated_pose = Odometry()                
        self.fill_odometry_header()
        self.puzzlebot_estimated_pose.pose.pose.position.x, self.puzzlebot_estimated_pose.pose.pose.position.y = (self.initial_x, self.initial_y)        
        self.puzzlebot_estimated_rot = self.initial_theta
        self.puzzlebot_estimated_rot_quaternion = None
        self.last_sampling_time = None
        self.puzzlebot_wr = None
        self.puzzlebot_wl = None
        self.v = 0.0
        self.w = 0.0           
        self.first_time_with_w = True     

        rospy.loginfo("ODOMETRY RESET")        
        return ResetOdometryResponse(True)

    def puzzlebot_wr_callback(self, msg):
        self.puzzlebot_wr = msg.data        

    def puzzlebot_wl_callback(self, msg):
        self.puzzlebot_wl = msg.data         

    def fill_odometry_header(self):
        self.puzzlebot_estimated_pose.header.stamp = rospy.Time.now()
        self.puzzlebot_estimated_pose.header.frame_id = "map"
        self.puzzlebot_estimated_pose.child_frame_id = "base_link_ghost"

    def main(self):
        while not rospy.is_shutdown():
            if  self.puzzlebot_wr is not None and self.puzzlebot_wl is not None:
                if self.first_time_with_w:
                    self.first_time_with_w = False
                    self.last_sampling_time = rospy.get_time()                    
                    rospy.loginfo("Odometry initialized")
                else:
                    current_time = rospy.get_time()
                    delta_t = (current_time - self.last_sampling_time)
                    self.fill_odometry_header()
                    
                    # _________ wheels' odometry ______________
                    #publicadores nuevos? v y w
                    self.v = (self.puzzlebot_wheel_rad/2)*self.puzzlebot_wr + (self.puzzlebot_wheel_rad/2)*self.puzzlebot_wl
                    self.w = (self.puzzlebot_wheel_rad/self.puzzlebot_wheel_to_wheel_dist)*self.puzzlebot_wr - (self.puzzlebot_wheel_rad/self.puzzlebot_wheel_to_wheel_dist)*self.puzzlebot_wl
                    # _________ end of wheels' odometry ______________


                    # _________ filling puzzlebot state data ______________
                    self.puzzlebot_estimated_pose.pose.pose.position.x += self.v*(np.cos(self.puzzlebot_estimated_rot))*delta_t
                    self.puzzlebot_estimated_pose.pose.pose.position.y += self.v*(np.sin(self.puzzlebot_estimated_rot))*delta_t
                    self.puzzlebot_estimated_rot += self.w*delta_t
                    self.puzzlebot_estimated_rot_quaternion = quaternion_from_euler(0.0, 0.0, self.puzzlebot_estimated_rot)
                    self.puzzlebot_estimated_pose.pose.pose.orientation.x = self.puzzlebot_estimated_rot_quaternion[0]
                    self.puzzlebot_estimated_pose.pose.pose.orientation.y = self.puzzlebot_estimated_rot_quaternion[1]
                    self.puzzlebot_estimated_pose.pose.pose.orientation.z = self.puzzlebot_estimated_rot_quaternion[2]
                    self.puzzlebot_estimated_pose.pose.pose.orientation.w = self.puzzlebot_estimated_rot_quaternion[3]
                    # _________ end of filling puzzlebot pose data ______________

                    self.last_sampling_time = current_time                    
            self.puzzlebot_odom_pub.publish(self.puzzlebot_estimated_pose)
            self.rate.sleep()

if __name__ == '__main__':
    instance = OdometryNode()
    instance.main()
