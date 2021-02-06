######################################################################################################################################

#################### SINGLE OSCILLATOR ROSSLER OSCILLATORS ###########################################################################

######################################################################################################################################

# https://thebrickinthesky.wordpress.com/2013/02/23/maths-with-python-2-rossler-system/

#First we load some packages.
from numpy import *
from matplotlib import *
from scipy import *
from pylab import figure, show, setp
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#We define a function which is going to be the recursive function.
def num_rossler(x_n,y_n,z_n,h,a,b,c):
    x_n1=x_n+h*(-y_n-z_n)
    y_n1=y_n+h*(x_n+a*y_n)
    z_n1=z_n+h*(b+z_n*(x_n-c))   
    return x_n1,y_n1,z_n1

#Now we prepare some variables
#First the parameters
a=0.2
b=0.3
c=5.2 # c=(3, 4, 4.5 ,5.2)

#Them the time interval and the step size
t_ini=0
t_fin=32*pi
h=0.001
numsteps=int((t_fin-t_ini)/h)

#using this parameters we build the time.
t=numpy.linspace(t_ini,t_fin,numsteps)
#And the vectors for the solutions
x=numpy.zeros(numsteps)
y=numpy.zeros(numsteps)
z=numpy.zeros(numsteps)

#We set the initial conditions
x[0]=0
y[0]=0
z[0]=0

#This is the main loop where we use the recursive system to obtain the solution
for k in range(x.size-1):
    #We use the previous point to generate the new point using the recursion
    [x[k+1],y[k+1],z[k+1]]=num_rossler(x[k],y[k],z[k],t[k+1]-t[k],a,b,c)

#Now that we have the solution in vectors t,x,y,z is time to plot them.

#We create a figure and 4 axes on it. 3 of the axes are going to be 2D and the fourth one is a 3D plot.

fig = figure()
ax1 = fig.add_axes([0.1, 0.7, 0.4, 0.2])
ax2 = fig.add_axes([0.1, 0.4, 0.4, 0.2])
ax3 = fig.add_axes([0.1, 0.1, 0.4, 0.2])
ax4 = fig.add_axes([0.55, 0.25, 0.35, 0.5],projection='3d')

# And we add vectors to each plot
ax1.plot(t, x,color='red',lw=1,label='x(t)')
ax1.set_xlabel('t')
ax1.set_ylabel('x(t)')
ax1.legend()
ax1.axis((t_ini,t_fin,min(x),max(x)))

ax2.plot(t, y,color='green',lw=1,label='y(t)')
ax2.set_xlabel('t')
ax2.set_ylabel('y(t)')
ax2.legend()
ax2.axis((t_ini,t_fin,min(y),max(y)))

ax3.plot(t, z,color='blue',lw=1,label='z(t)')
ax3.set_xlabel('t')
ax3.set_ylabel('z(t)')
ax3.legend()
ax3.axis((t_ini,t_fin,min(z),max(z)))

ax4.plot(x, y,z,color='black',lw=1,label='Evolution(t)')
ax4.set_xlabel('x(t)')
ax4.set_ylabel('y(t)')
ax4.set_zlabel('z(t)')
ax4.set_title('Rossler Attractor with c=5.2')
# When finished we show the figure with all the plots.
show()

# Program 08a: The Rossler chaotic attractor. See Fig. 8.10(a).
# In this case, iteration is used to solve the ODEs.

# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# def Rossler(x, y, z, c, a=0.2, b=3): # c=(3, 4, 4.5 ,5.2)
#     x_dot = -y - z
#     y_dot = x + a*y
#     z_dot = b + x*z - c*z
#     return (x_dot, y_dot, z_dot)

# # dt = 0.01 
# # step_count = 50000
# dc = 0.0005  # parameter step size
# c = np.arange(2.9, 6, dc)  # parameter range
# # c=(3, 4, 4.5, 5.2) # parameter range
# dt = 0.001             # time step
# t = np.arange(0,10,dt) # time range

# #initialize solution arrays
# xs = np.empty(len(t) + 1)
# ys = np.empty(len(t) + 1)
# zs = np.empty(len(t) + 1)

# # The initial conditions
# xs[0], ys[0], zs[0] = (1.0, 1.0, 1.0)

# # Save the plot points coordinates and plot the with a single call to plt.plot
# # instead of plotting them one at a time, as it's much more efficient
# z_maxes = []
# c_maxes = []
# z_mins = []
# c_mins = []

# # Iterate
# for C in c:
#     # Print something to show everything is running
#     print(f"{C=:.2f}")
#     for i in range(len(t)):

#         #approximate numerical solutions to system
#         x_dot, y_dot, z_dot = Rossler(xs[i], ys[i], zs[i], C)
#         xs[i+1] = xs[i] + (x_dot * dt)
#         ys[i+1] = ys[i] + (y_dot * dt)
#         zs[i+1] = zs[i] + (z_dot * dt)

#     # calculate and save the peak values of the z solution
#     for i in range(1, len(zs) - 1):
#         # save the local maxima
#         if zs[i - 1] < zs[i] and zs[i] > zs[i + 1]:
#             c_maxes.append(C)
#             z_maxes.append(zs[i])
#         # save the local minima
#         elif zs[i - 1] > zs[i] and zs[i] < zs[i + 1]:
#             c_mins.append(C)
#             z_mins.append(zs[i])

#         # "use final values from one run as initial conditions for the next to stay near the attractor"
#         xs[0], ys[0], zs[0] = xs[i], ys[i], zs[i]

# plt.scatter(c_maxes, z_maxes, color="black", s=0.5, alpha=0.2)
# plt.scatter(c_mins, z_mins, color="red", s=0.5, alpha=0.2)
# plt.title("Biffurcation diagram of Rössler attractor")
# plt.xlabel("c")
# plt.ylabel("z")

# plt.show()



# fig = plt.figure()
# ax = Axes3D(fig)

# ax.plot(xs, ys, zs, lw=0.5)
# ax.set_xlabel('x', fontsize=15)
# ax.set_ylabel('y', fontsize=15)
# ax.set_zlabel('z', fontsize=15)
# plt.tick_params(labelsize=15)
# ax.set_title('Rossler Attractor with c=3', fontsize=15)

# plt.show()

# This is a simple code to solve Rössler equation system in python and plot solutions.
# Made by Héctor Corte-León leo_corte@yahoo.es on 23/02/2013
# The numerical method used is first order forward Euler method.
