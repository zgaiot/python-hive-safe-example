import datetime as dt
import serial
import time
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
xs = [x for x in range(25)]
ys = [y for y in range(25)]

x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)

fig, axes = plt.subplots(nrows=6)

styles = ['r-', 'g-', 'y-', 'm-', 'k-', 'c-']
def plot(ax, style):
    return ax.plot(x, y, style, animated=True)[0]
lines = [plot(ax, style) for ax, style in zip(axes, styles)]

def animate(i):
    for j, line in enumerate(lines, start=1):
        line.set_ydata(np.sin(j*x + i/10.0))
    return lines

# We'd normally specify a reasonable "interval" here...
ani = animation.FuncAnimation(fig, animate, xrange(1, 200), 
                              interval=1, blit=True)

plt.show()
