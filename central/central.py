#!/usr/bin/env python
import rospy
import time
import numpy as np
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float32
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def central():
	rospy.init_node('central', anonymous=True)
	
	# read from line tracking sensor
	print("Subscribing to /line_dists")
	sub1 = rospy.Subscriber("/line_dists", Float32MultiArray, callback)
	
	# read from gps sensor
	print("Subscribing to /gps_readings")
	sub2 = rospy.Subscriber('/gps_readings',String,callback)

	while not rospy.is_shutdown():
		        pub = rospy.Publisher('/basic_string',String, queue_size=1)
        		r = rospy.Rate(10) # 10Hz
			pub.publish('Sending (fake) data')
			rospy.sleep(0.1)

if __name__ == '__main__':
	print("Starting central")
	central()

# "To make a node both a publisher and a subscriber, you need to
# define both a publisher object and a subscriber object AND a 
# callback for the subscriber object"

