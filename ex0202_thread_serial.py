import threading
import serial
import time

connected = False
port = '/dev/cu.usbmodem0006835879461'
baud = 115200

serial_port = serial.Serial(port, baud, timeout=0)

def read_from_port(ser):

    while ser.is_open != True:
        print("Serial can't open")
        time.sleep(2)

    while True:
        msg = ser.readline()

        if len(msg.strip()) != 0 :
            print(msg)
        #     dataLog = msg.split(',')
        #     if dataLog[0] == "A" and len(dataLog) > 3:
        #         #plot_acc(int(dataLog[1]), int(dataLog[2]) ,int(dataLog[3]), int(dataLog[4]) )
        #         print(int(dataLog[1]))    
        time.sleep(0.04)
        if stop_threads: 
            break
    
stop_threads = False

thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()

value = input("Please enter to exit:\n")
stop_threads = True