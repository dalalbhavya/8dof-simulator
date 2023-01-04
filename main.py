import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mplot3d
import numpy as np
import mpl_toolkits.mplot3d.axes3d as axes3d

fig = plt.figure()
ax = plt.axes(projection="3d")

z = [0, 1, 2]
x = [0, 2, 3]
y = [0, 4, 5]

ax.plot(x[:2],y[:2],z[:2], label="link1")
ax.plot(x[1:], y[1:], z[1:], label = "link2")
ax.legend()

plt.show()