##########################################################
##############Lorentz System Solution#####################
##########################################################
#This program solves the coupled ODE of the Lorentz system
#We define f,g and h as x',y' and z' resp...
def f(x,y,z):
	return sigma*(y-x)
def g(x,y,z):
	return -x*z+r*x-y
def h(x,y,z):
	return x*y-b*z
#We choose a set of parameters
sigma=10.
b=8./3.
r=25.
# And initial conditions
x=0.
y=1.
z=0.
#We use the simplest way to integrate the equations
dt=0.01
X,Y,Z=[],[],[]
for i in range (10000):
    X.append(x)
    Y.append(y)
    Z.append(z)
    x0=x+dt*f(x,y,z)
    y0=y+dt*g(x,y,z)
    z0=z+dt*h(x,y,z)
    x,y,z=x0,y0,z0
#We save the results
import numpy as np
np.savetxt('Lorentz.dat',np.array([X,Y,Z]).T)
