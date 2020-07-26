from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

ax = fig.add_subplot(111,projection = "3d")

X,Y,Z = np.array([[1,5,1],[1,1,1]]),np.array([[1,5,7],[1,1,1]]),np.array([[0,0,0],[1,5,1]])

ax.plot_wireframe(X,Y,Z)

plt.show()