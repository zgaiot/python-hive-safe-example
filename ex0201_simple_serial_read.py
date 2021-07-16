#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:01:23 2020

@author: w.wiyarungmail.com
"""

import serial
import time

ser = serial.Serial('/dev/cu.usbmodem0006835879461', 115200, timeout=0,parity=serial.PARITY_EVEN, rtscts=0)  # open serial port
print(ser.name)         # check which port was really used

print(ser.is_open)

while True:    
    #print("Read::")
    line = ser.readline()
    if len(line.strip()) != 0 :
        print(line)    
    
    time.sleep(0.035)
    
ser.close()    
print("END")
