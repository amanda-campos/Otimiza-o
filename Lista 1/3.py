# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 17:38:21 2020

@author: Amanda
"""


import numpy as np
import matplotlib.pyplot as plt


N = 100000
M = 10000
T = 1


x = np.zeros(N)
n=0
x[0] = np.random.uniform(0,1)
e = 0.1; T = 0.1;
J0 = x[0]**2; Xatual = x[0]; Jatual = J0;


for n in range(1,N):
    
    x_hat = x[n-1] + e*np.random.randn()   
        
    if np.random.uniform(0,1)< np.exp(((x[n-1])**2 - (x_hat)**2)/T):
        x[n] = x_hat
    else:
        x[n] = x[n-1]

y = np.linspace(0,6,1000)
plt.figure(1)
plt.hist(x[M:], 5)
plt.show()



