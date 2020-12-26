#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys
import rospy
import signal
import numpy as np
from std_msgs.msg import Float32MultiArray

def signal_handler(signal, frame): # ctrl + c -> exit program
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

class linetracking():
    def __init__(self):
        rospy.init_node('linetracking', anonymous=True)
        self.pub = rospy.Publisher('/line_dists',Float32MultiArray, queue_size=1)
        self.r = rospy.Rate(10) # 10Hz

    def data_sender(self,readings):
        msg = Float32MultiArray()
        msg.data=readings
	print(msg.data)
        self.pub.publish(msg)

# set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(7, GPIO.IN)
GPIO.setup(1, GPIO.IN)

sensor=linetracking()
time.sleep(0.5)
print ('----------------------------linetracking start-------------------------------')
try :
    while True :
	L11 =GPIO.input(5)
        L12 =GPIO.input(6)
	L13 =GPIO.input(13)
	L14 =GPIO.input(19)
	L15 =GPIO.input(26)
	L21 =GPIO.input(24)
        L22 =GPIO.input(25)
	L23 =GPIO.input(8)
	L24 =GPIO.input(7)
	L25 =GPIO.input(1)
	L1 = np.array([1,L11,L12,L13,L14,L15]) 
	L2 = np.array([2,L21,L22,L23,L24,L25])

	sensor.data_sender(L1)
	sensor.data_sender(L2)

	sensor.r.sleep()
	

except (KeyboardInterrupt, SystemExit):
    GPIO.cleanup()
    sys.exit(0)
except:
    GPIO.cleanup()