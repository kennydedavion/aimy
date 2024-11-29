import socket
from struct import *
import RPi.GPIO as GPIO
import numpy as np

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)   
GPIO.setup(9,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)

# Prepare the UDP connection
UDP_IP = "192.168.0.164"
print ("Receiver IP: ", UDP_IP)
UDP_PORT = 5555
print ("Port: ", UDP_PORT)
sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
#sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
#sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
sock.bind((UDP_IP, UDP_PORT))

# Continuously read from the UDP socket
while True:
    data, addr = sock.recvfrom(1024)
    print (data)

# Output
