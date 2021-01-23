# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:57:06 2020

@author: Amanda
"""
#Questão 2 (b)

import numpy as np
import matplotlib.pyplot as plt


N = 100000
M = 10000
T = 1

def J(x):
    return (x-3)**2

x = np.zeros(N)
n=0
x[n] = np.random.choice([1,2,3,4,5])


for n in range(1,N):
    
    # x_hat = np.random.choice([1,2,3,4,5])
    perturbacao = np.random.choice([-1,1])
    
    if x[n] == 5:
        if perturbacao == 1:
            x_hat = 1
    elif x[n] == 1:
        if perturbacao == -1:
            x_hat= 5
    else:    
        x_hat = x[n-1] + perturbacao
    
    if np.random.uniform()< np.exp((J(x[n-1]) - J(x_hat))/T):    
    # if np.random.rand(1)< np.exp((J(x[n-1]) - J(x_hat))/T):
        x[n] = x_hat
    else:
        x[n] = x[n-1]

y = np.linspace(0,6,1000)
plt.figure(1)
plt.hist(x[M:], 5)
plt.show()

