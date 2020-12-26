#!/usr/bin/env python
 
import serial
import time
import sys
import rospy
import signal
from std_msgs.msg import String

def signal_handler(signal, frame): # ctrl + c -> exit program
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

class gps():
    def __init__(self):
        rospy.init_node('gps', anonymous=True)
        self.pub = rospy.Publisher('/gps_readings',Float32, queue_size=1)
        self.r = rospy.Rate(10) # 10Hz

    def data_sender(self,readings):
        msg = String()
        msg.data=readings
	print(msg.data)
        self.pub.publish(msg)

# set up port, initial print statements
port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
port.write('AT'+'\r\n')            
time.sleep(.1)
port.write('AT+CGNSPWR=1'+'\r\n')            
time.sleep(0.1)
port.write('AT+CGNSURC=2'+'\r\n') 

sensor = gps()
time.sleep(0.5)

print ('---------------------------GPS start----------------------------------')

try :
    while True :
	rcv = port.read(200)
	# print (rcv)
	sensor.data_sender(rcv);
	sensor.r.sleep()

except (KeyboardInterrupt, SystemExit):
    sys.exit(0)

   