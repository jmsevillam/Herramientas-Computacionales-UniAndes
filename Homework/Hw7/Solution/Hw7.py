#!/usr/bin/env python
# coding: utf-8
# # Homework 7. `numpy`
# 
# Here you can find the solution of the homework 7 of the 'Herramientas computacionales' course at uniades (Section 6) [Course](https://github.com/jmsevillam/Herramientas-Computacionales-UniAndes), [Homework](https://github.com/jmsevillam/Herramientas-Computacionales-UniAndes/blob/master/Homework/Hw7/Hw7.pdf).
# As we are going to use `numpy`, we import it to use `numpy.array` structure,
import numpy as np
# Create an `array` from $0$ to $10$ including the limits,
x=np.linspace(0,10,1000)
# It has the expected lenght
print(len(x))
# We create some noisy signal by adding random numbers to a sine function,
y=np.sin(x)+(0.4*(np.random.random(len(x))-0.2))
# We use `matplotlib` as auxiliar visualization,
import matplotlib.pylab as plt
plt.plot(x,y)
plt.savefig('fig1.pdf')
plt.show()
# We use some of the numpy built-in functions to find the mean, variance, maximum and minimum.
print(np.mean(y))
print(np.var(y))
print(np.max(y))
print(np.min(y))
# In order to get the value of $x$ in which $y$ is max, we use the function `numpy.argmax`
print(np.argmax(y))
# And we use it to get the x of that cellm
print(x[np.argmax(y)])
# We implement two different ways to calculate the variance and average, one is based on the `list` structure  and the other using the `numpy` structure.
# 
# The skewness and Kurtosis functions are made by using the `numpy` structure.
def variance(x):
    ave=average(x)
    suma=0.
    for i in range(len(x)):
        suma+=(x[i]-ave)**2
    suma/=len(x)
    return suma
def variance2(x):
    ave=average2(x)
    suma=np.sum((x-ave)**2.)/len(x)
    return suma
def average(x):
    suma=0.
    for i in range(len(x)):
        suma+=x[i]
    suma=suma/len(x)
    return suma
def average2(x):
    suma=np.sum(x)/len(x)
    return suma
def skewness(x):
    ave=average2(x)
    suma=np.sum((x-ave)**3.)/len(x)
    return suma
def Kurtosis(x):
    ave=average2(x)
    suma=np.sum((x-ave)**4.)/len(x)
    return suma
# We use them,
print(average(y))
print(average2(y))
print(variance(y))
print(variance2(y))
print(np.var(y))
print(skewness(y))
print(Kurtosis(y))
# We use again `matplotlib`to see  the _distribution_ of the $y$ points,
plt.hist(y,bins=25)
plt.savefig('fig2.pdf')
plt.show()
# We perform some transformations on the data,
y2=np.sort(y)
plt.plot(x,y)
plt.plot(x,y2)
plt.savefig('fig3.pdf')
plt.show()

y3=y*y2
plt.plot(x,y)
plt.plot(x,y2)
plt.plot(x,y3)
plt.savefig('fig4.pdf')
plt.show

# And we calculate the percentile 5 and 95
np.percentile(y3,q=[5,95])

