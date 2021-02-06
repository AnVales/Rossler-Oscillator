##First we load some packages.
from numpy import *
from matplotlib import *
from scipy import *
from pylab import figure, show, setp
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import scipy.io as sio
from scipy.signal import find_peaks

#We define a function which is going to be the recursive function.
def num_rossler(x1_n, y1_n, z1_n, x2_n, y2_n, z2_n, h, a, b, cz, k):
    x1_n1=x1_n+h*(-y1_n-z1_n+k*(x2_n-x1_n)) # dx/dt = x1 + h*( - y1 - z1 + k (x2 - x1 ))
    y1_n1=y1_n+h*(x1_n+a*y1_n)
    z1_n1=z1_n+h*(b+z1_n*(x1_n-c))   

    x2_n1=x2_n+h*(-y2_n-z2_n+k*(x1_n-x2_n))
    y2_n1=y2_n+h*(x2_n+a*y2_n)
    z2_n1=z2_n+h*(b+z2_n*(x2_n-c))   

    return x1_n1, y1_n1, z1_n1, x2_n1, y2_n1, z2_n1

#Now we prepare some variables
#First the parameters
a=0.2
b=0.3
c=5.2
k=0.1

#Them the time interval and the step size
t_ini=0
t_fin=32*pi
h=0.0001
numsteps=int((t_fin-t_ini)/h)

#using this parameters we build the time.
t=numpy.linspace(t_ini,t_fin,numsteps)
#And the vectors for the solutions
x1=numpy.zeros(numsteps)
y1=numpy.zeros(numsteps)
z1=numpy.zeros(numsteps)

x2=numpy.zeros(numsteps)
y2=numpy.zeros(numsteps)
z2=numpy.zeros(numsteps)

#We set the initial conditions
x1[0]=0
y1[0]=0
z1[0]=0

x2[0]=0
y2[0]=0
z2[0]=0

#This is the main loop where we use the recursive system to obtain the solution
for k in range(x1.size-1):
    #We use the previous point to generate the new point using the recursion
    [x1[k+1],y1[k+1],z1[k+1],x2[k+1],y2[k+1],z2[k+1]]=num_rossler(x1[k],y1[k],z1[k],x2[k],y2[k],z2[k],t[k+1]-t[k],a,b,c,k)

#Now that we have the solution in vectors t,x,y,z is time to plot them.

#We create a figure and 4 axes on it. 3 of the axes are going to be 2D and the fourth one is a 3D plot.
fig = figure()
ax1 = fig.add_axes([0.30, 0.7, 0.4, 0.2])
ax3 = fig.add_axes([0.05, 0.1, 0.4, 0.5],projection='3d')
ax4 = fig.add_axes([0.55, 0.1, 0.4, 0.5],projection='3d')

#And we add vectors to each plot
ax1.plot(t, x1,color='red',lw=1,label='x1(t)')
ax1.set_xlabel('t')
ax1.set_ylabel('x(t)')
ax1.legend()
ax1.axis((t_ini,t_fin,min(x1),max(x1)))


ax1.plot(t, x2,color='green',lw=1,label='x2(t)')
ax1.set_xlabel('t')
ax1.set_ylabel('x(t)')
ax1.legend()
ax1.axis((t_ini,t_fin,min(x2),max(x2)))

ax4.plot(x2, y2,z2,color='green',lw=1)
ax4.set_xlabel('x2(t)')
ax4.set_ylabel('y2(t)')
ax4.set_zlabel('z2(t)')

ax3.plot(x1, y1,z1,color='red',lw=1)
ax3.set_xlabel('x1(t)')
ax3.set_ylabel('y1(t)')
ax3.set_zlabel('z1(t)')
# When finished we show the figure with all the plots.
show()

# find peaks
peakslistx1=[] #list containing the indexes of each trajectory's peaks
peakslistx1, _ = find_peaks(x1)

peakslistx2=[] #list containing the indexes of each trajectory's peaks
peakslistx2, _ = find_peaks(x2)

# obtenemos los tiempos
tx1_values=[]
for i in peakslistx1:
    t_value=t[i]
    tx1_values.append(t_value)

tx2_values=[]
for i in peakslistx2:
    t_value=t[i]
    tx2_values.append(t_value)

# diferencia de fase
periodo=[]

for i in range(len(tx1_values)):
    if i+1<len(tx1_values):
        dif=-tx1_values[i]+tx1_values[i+1]
        periodo.append(dif)

# diferencia tiempos
dif_tx_list=[]
for tx1, tx2 in zip(tx1_values, tx2_values):
    dif_tx=tx2-tx1
    dif_tx_list.append(dif_tx)

print(numpy.mean(periodo))

# eq=2*numpy.pi*t/T
phases=[]
for dif_tx, periodoi in zip(dif_tx_list, periodo):
    dif_ph=2*numpy.pi*dif_tx/periodoi
    phases.append(dif_ph)

print(phases)