# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 17:38:21 2020

@author: Amanda
"""


import numpy as np
import matplotlib.pyplot as plt


N = 100000
M = 10000

def J(x):
    return -T*np.log(f(x))

def f(x):
    return x**2

x = np.zeros(N)
n=0
x[0] = np.random.randn()
e = 0.1; T = 0.1;
J0 = J(x[0]); Xatual = x[0]; Jatual = J0;


for n in range(1,N):
    
    perturbacao = np.random.choice([-1,1])
    
    x_hat = x[n-1] + e*perturbacao 
        
    if np.random.uniform(0,1)< np.exp(((J(x[n-1]) - J(x_hat))/T)):
        x[n] = x_hat
    else:
        x[n] = x[n-1]

y = np.linspace(0,6,1000)
plt.figure(1)
plt.hist(x[M:], 5)
plt.show()



