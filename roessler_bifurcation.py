import numpy as _N
import matplotlib.pyplot as _plt

N    = 2000000   #  of numerical iterations
burn =   80000   #  wait until hitting attractor

x1 = _N.zeros(N)   #  store Roessler attractor for 1 value of c
y1 = _N.zeros(N)
z1 = _N.zeros(N)

x2 = _N.zeros(N)   #  store Roessler attractor for 1 value of c
y2 = _N.zeros(N)
z2 = _N.zeros(N)

dt= 0.001     #  size of time steps

#  Roessler params held fixed
a = 0.2
b = 0.3
k = 0.1

cSteps = 60   #  how many values of c to sample
cs     = _N.linspace(2.5, 5.5, cSteps)
zVCs   = []  #  list of list of xValues at crossing

for c in cs:  # c from 5, 10 in 50 steps
    zValAtCross = []   #  List of values of x when y crosses threshold
    x1[0] = _N.random.rand()
    y1[0] = _N.random.rand()
    z1[0] = _N.random.rand()

    x2[0] = _N.random.rand()
    y2[0] = _N.random.rand()
    z2[0] = _N.random.rand()

    #  Newton's method.  Simple
    for n in range(1, N):
        x1[n] = (-y1[n-1] - z1[n-1])*dt  + x1[n-1] + k*(x2[n-1] - x1[n-1])
        y1[n] = (x1[n-1] + a*y1[n-1])*dt + y1[n-1]
        z1[n] = (b + z1[n-1]*(x1[n-1] - c))*dt + z1[n-1]

        x2[n] = (-y2[n-1] - z2[n-1])*dt  + x2[n-1]+ k*(- x2[n-1] + x1[n-1])
        y2[n] = (x2[n-1] + a*y2[n-1])*dt + y2[n-1]
        z2[n] = (b + z2[n-1]*(x2[n-1] - c))*dt + z2[n-1]
        
        if (n > burn) and ((y1[n] > 0) and (y1[n-1] < 0)):   #  burn in
            r = (0 - y1[n-1]) / (y1[n] - y1[n-1])
            zValAtCross.append(z1[n-1] + r*(z1[n] - z1[n-1]))

    zVCs.append(_N.array(zValAtCross))
    #  _plt.plot(x, y)   #   Just plot the attractor

ic  = 0

fig = _plt.figure(figsize=(6, 2*4))
fig.add_subplot(2, 1, 1)
for c in cs:  # c from 5, 10 in 50 steps
    cValAtCross = _N.ones(len(zVCs[ic])) * c    # for pairs (c, xValAtCross[n]) 
    _plt.scatter(cValAtCross, zVCs[ic], s=1)
    ic += 1

_plt.xlabel("c")
_plt.ylabel("z")
fig.add_subplot(2, 1, 2)
#  plot attractor at final value of c
_plt.plot(z1[burn:], x1[burn:])
_plt.xlabel("z")
_plt.ylabel("x")
_plt.savefig("roessler_bifurcation")
_plt.close()