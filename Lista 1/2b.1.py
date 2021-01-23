# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:35:09 2020

@author: Amanda
"""

import numpy as np
import matplotlib.pyplot as plt


N = int(1e5)
M = int(1e4)
T = 1


X = np.zeros(N)

X[0] = np.random.choice([1,2,3,4,5]); n = 0;

J0 = (X[0]-3)**2; Xatual = X[0]; Jatual= J0;

fim = 0; 

while not(fim):

    perturbacao = np.random.choice([-1,1])
    
    if Xatual == 5:
        if perturbacao == 1:
            X[n] = 1
    elif Xatual == 1:
        if perturbacao == -1:
            X[n] = 5
    else:    
        X[n] = Xatual + perturbacao
    
    dJ = (X[n]-3)**2 - (Xatual-3)**2
    
    q = np.exp(-dJ/T)
    
    r = np.random.uniform(0,1)
    
    if (r > q): 
        a = 0
    if (r < q): 
        a = 1
    if (dJ< 0):
        Xatual = X[n]
    if (dJ>=0):
        Xatual = (1-a)*Xatual + a*X[n]
    
    if (n == N):
        fim = 1
    
    n = n + 1 
    
y = np.linspace(0,6,1000)
plt.figure(1)
plt.hist(X[M:],5)
plt.show()