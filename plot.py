from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plot
import numpy as np

fig = plot.figure()
ax = fig.gca(projection='3d')

s = 0.05  
X = np.arange(-2, 2.+s, s)   
Y = np.arange(-2, 3.+s, s)   
    

X, Y = np.meshgrid(X, Y)


Z =1*(Y-((5.1/(4*(22/7)**2))*X**2)+((5/(22/7))*X)-6)**2+10*(1-(1/(8*(22/7))))*np.cos(X)+10 
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
         linewidth=0, antialiased=False)  #Try coolwarm vs jet

 
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plot.show()