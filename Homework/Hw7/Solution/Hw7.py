#!/usr/bin/env python
# coding: utf-8

# # Homework 7. `numpy`
# 
# Here you can find the solution of the homework 7 of the 'Herramientas computacionales' course at uniades (Section 6) [Course](https://github.com/jmsevillam/Herramientas-Computacionales-UniAndes), [Homework](https://github.com/jmsevillam/Herramientas-Computacionales-UniAndes/blob/master/Homework/Hw7/Hw7.pdf).

# As we are going to use `numpy`, we import it to use `numpy.array` structure,

# In[1]:


import numpy as np


# Create an `array` from $0$ to $10$ including the limits,

# In[2]:


x=np.linspace(0,10,1000)


# It has the expected lenght

# In[3]:


len(x)


# We create some noisy signal by adding random numbers to a sine function,

# In[4]:


y=np.sin(x)+(0.4*(np.random.random(len(x))-0.2))


# We use `matplotlib` as auxiliar visualization,

# In[5]:


import matplotlib.pylab as plt


# In[6]:


plt.plot(x,y)
plt.savefig('fig1.pdf')
plt.show()


# We use some of the numpy built-in functions to find the mean, variance, maximum and minimum.

# In[7]:


np.mean(y)


# In[8]:


np.var(y)


# In[9]:


np.max(y)


# In[10]:


np.min(y)


# In order to get the value of $x$ in which $y$ is max, we use the function `numpy.argmax`

# In[11]:


np.argmax(y)


# And we use it to get the x of that cellm

# In[12]:


x[np.argmax(y)]


# We implement two different ways to calculate the variance and average, one is based on the `list` structure  and the other using the `numpy` structure.
# 
# The skewness and Kurtosis functions are made by using the `numpy` structure.

# In[13]:


def variance(x):
    ave=average(x)
    suma=0.
    for i in range(len(x)):
        suma+=(x[i]-ave)**2
    suma/=len(x)
    return suma


# In[14]:


def variance2(x):
    ave=average2(x)
    suma=np.sum((x-ave)**2.)/len(x)
    return suma


# In[15]:


def average(x):
    suma=0.
    for i in range(len(x)):
        suma+=x[i]
    suma=suma/len(x)
    return suma


# In[16]:


def average2(x):
    suma=np.sum(x)/len(x)
    return suma


# In[17]:


def skewness(x):
    ave=average2(x)
    suma=np.sum((x-ave)**3.)/len(x)
    return suma


# In[18]:


def Kurtosis(x):
    ave=average2(x)
    suma=np.sum((x-ave)**4.)/len(x)
    return suma


# We use them,

# In[19]:


get_ipython().run_line_magic('time', '')
average(y)


# In[20]:


get_ipython().run_line_magic('time', '')
average2(y)


# In[21]:


get_ipython().run_line_magic('time', '')
variance(y)


# In[22]:


get_ipython().run_line_magic('time', '')
variance2(y)


# In[23]:


get_ipython().run_line_magic('time', '')
np.var(y)


# In[24]:


skewness(y)


# In[25]:


Kurtosis(y)


# We use again `matplotlib`to see  the _distribution_ of the $y$ points,

# In[26]:


plt.hist(y,bins=25)
plt.savefig('fig2.pdf')
plt.show()


# We perform some transformations on the data,

# In[27]:


y2=np.sort(y)


# In[28]:


plt.plot(x,y)
plt.plot(x,y2)
plt.savefig('fig3.pdf')
plt.show()


# In[29]:


y3=y*y2
plt.plot(x,y)
plt.plot(x,y2)
plt.plot(x,y3)
plt.savefig('fig4.pdf')
plt.show


# And we calculate the percentile 5 and 95

# In[30]:


np.percentile(y3,q=[5,95])

