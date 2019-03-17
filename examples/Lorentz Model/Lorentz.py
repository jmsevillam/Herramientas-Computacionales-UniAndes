def f(x,y,z):
	return sigma*(y-x)
def g(x,y,z):
	return -x*z+r*x-y
def h(x,y,z):
	return x*y-b*z

sigma=10.
b=8./3.

r=25.

x=0.
y=1.
z=0.

dt=0.01
X,Y,Z=[],[],[]
zph,yph=[],[]
for i in range (10000):
	X.append(x)
	Y.append(y)
	Z.append(z)
	x0=x+dt*f(x,y,z)
	y0=y+dt*g(x,y,z)
	z0=z+dt*h(x,y,z)
	if x*x0<0:
		zph.append(z)
		yph.append(y)
	x=x0
	y=y0
	z=z0
		
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

plt.plot(yph,zph,'.')
plt.show()
plt.plot(X, Y)
plt.show()

plt.plot(Y, Z)

plt.show()
plt.plot(X, Z)
plt.show()

fig = plt.figure()

ax = fig.add_subplot(111,projection='3d')
ax.plot(X, Y, Z)
#ax.scatter(X, Y, Z,c=Z,alpha=0.2)
plt.show()

import numpy as np
np.savetxt('Lorentz.dat',np.array([X,Y,Z]).T)
