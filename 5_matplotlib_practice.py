# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 22:28:18 2018

@author: NAVEEN AGGARWAL
"""
#%%
import matplotlib.pyplot as plt 
plt.plot([1,2,3,4,5]) 
plt.ylabel('some significant numbers') 
plt.show() 
#%%
import numpy as np 
import matplotlib.pyplot as plt 
# evenly sampled time at .2 intervals 
t = np.arange(0., 5., 0.2) 
# red dashes, blue squares and green triangles 
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') 
plt.axis([0, 6, 0, 150]) # x and y range of axis 
plt.show() 
#%%
import numpy as np 
import matplotlib.pyplot as plt 
def f(t): 
    return np.exp(-t) * np.cos(2*np.pi*t) 
t1 = np.arange(0.0, 5.0, 0.1) 
t2 = np.arange(0.0, 5.0, 0.02) 
plt.figure(1) # Called implicitly
# for multiple figures 
plt.subplot(211) # 2 rows, 1 column, 1st plot 
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k') 
plt.subplot(212) # 2 rows, 1 column, 2nd plot 
plt.plot(t2, np.cos(2*np.pi*t2), 'r--') 
plt.show() 
#%%
import numpy as np 
import matplotlib.pyplot as plt 
mu, sigma = 100, 15 
x = mu + sigma * np.random.randn(10000) 
# the histogram of the data 
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75) 
plt.xlabel('Smarts') 
plt.ylabel('Probability') 
plt.title('Histogram of IQ') 
plt.text(60, .025, '$\mu=100,\ \sigma=15$', color='r') #TeX equations 
plt.axis([40, 160, 0, 0.03]) 
plt.grid(True) 
plt.show() 
