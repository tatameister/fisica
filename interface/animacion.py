from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

fig = plt.figure()
ax = p3.Axes3D(fig)

def gen(n):
    theta = 0
    e = 2.718281
    a = 0.5
    an1 = 45
    an2 = 30

    while theta > -25*np.pi:
        x = a * (e ** (np.sin(an1) * (1 / np.tan(an2) * theta))) * np.cos(theta)
        y = a * (e ** (np.sin(an1) * (1 / np.tan(an2) * theta))) * np.sin(theta)
        z = a * (e ** (np.sin(an1) * (1 / np.tan(an2) * theta))) * (1 / np.tan(an1))
        yield np.array([x, y, z])
        theta += -8*np.pi/n

def update(num, data, line):
    line.set_data(data[:2, :num])
    line.set_3d_properties(data[2, :num])

N = 150
data = np.array(list(gen(N))).T
line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])


ax.set_xlim3d([-10.0, 10.0])
ax.set_xlabel('X')

ax.set_ylim3d([-10.0, 10.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 10.0])
ax.set_zlabel('Z')

ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=1000/N, blit=False)

plt.show()