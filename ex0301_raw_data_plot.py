import threading
import serial
import time
import datetime as dt
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

ts = [t for t in range(125)]
acc_x = [i for i in range(125)]
acc_y = [i for i in range(125)]
acc_z = [i for i in range(125)]

port = '/dev/cu.usbmodem0006835879461'
baud = 115200

serial_port = serial.Serial('/dev/cu.usbmodem0006835879461', 115200, timeout=0,parity=serial.PARITY_EVEN, rtscts=0)  # open serial port

def isFloat(S):
    try:
        float(S)
        return True
    except ValueError:
        return False

def read_from_port(ser):
    global acc_x 
    global acc_y    
    global acc_z 
    
    while ser.is_open != True:
        print("Serial can't open")
        time.sleep(2)

    msg_array = []
    msg = ""
    while True:
        buf_msg = ser.read(1)
        
        if len(buf_msg) > 0:
            if buf_msg == b'\n':
                msg_array.append(chr(buf_msg[0]))
                msg = ''.join( msg_array)
                dataLog = msg.split(',')
                #print(dataLog)
                if len(dataLog) > 4 and dataLog[0] == "A":
                    if dataLog[4] == "Z":
                        if isFloat(dataLog[1]) and isFloat(dataLog[2]) and isFloat(dataLog[3]):
                            acc_x.append(float(dataLog[1])/1000)
                            acc_y.append(float(dataLog[2])/1000)    
                            acc_z.append(float(dataLog[3])/1000)
                            acc_x = acc_x[-125:]  
                            acc_y = acc_y[-125:]
                            acc_z = acc_z[-125:]  
                            print("value:" + str(int(dataLog[1])) + "," +  str(int(dataLog[2])) + "," + str(int(dataLog[3])))    
                    
                msg_array.clear()
            else:
                msg_array.append(chr(buf_msg[0]))
            

            
        # msg = str(buf_msg)
        # print(msg)
        # if len(msg.strip()) != 0 :
        #     dataLog = msg.split(',')
        #     print("msg:"+msg+", slot:"+ str(len(dataLog)))
            
        #     #print(dataLog[5])
        #     
        time.sleep(0.0001)
        if stop_threads: 
            break
    
stop_threads = False

thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()

xs = [x for x in range(25)]
ys = [y for y in range(25)]

fig, axes = plt.subplots(nrows=3)

styles = ['r-', 'g-', 'y-', 'm-', 'k-', 'c-']
def plot(ax, style):
    #ax.set_ylim([-2.1,2.1])
    ax.set_ylim([-27,27])
    
    return ax.plot(ts, acc_x, style, animated=True)[0]

lines = [plot(ax, style) for ax, style in zip(axes, styles)]

def animate(i):
    # for j, line in enumerate(lines, start=1):
    #     line.set_ydata(acc_x)
    lines[0].set_ydata(acc_x)
    lines[1].set_ydata(acc_y)
    lines[2].set_ydata(acc_z)
    return lines

# We'd normally specify a reasonable "interval" here...
#ani = animation.FuncAnimation(fig, animate, xrange(1, 200), 
#                              interval=40, blit=True)
ani = animation.FuncAnimation(fig, animate, range(1, 200), 
                              interval=40, blit=True)


plt.show()

#value = input("Please enter to exit:\n")
print("STOPPPPPPPpppppppppppSTOPPPPPPPpppppppppppSTOPPPPPPPpppppppppppSTOPPPPPPPpppppppppppSTOPPPPPPPppppppppppp")
stop_threads = True