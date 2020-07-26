from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

ax = fig.add_subplot(111,projection = "3d")

X,Y,Z = np.array([1,5,1]),np.array([1,5,7]),np.array([[8,3,1]])

ax.plot_wireframe(X,Y,Z)

plt.show()