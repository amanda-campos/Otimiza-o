# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:11:45 2020

@author: Amanda
"""
## 4 VARIAVÉIS

## REFERÊNCIA: https://learnwithpanda.com/2020/04/04/python-code-of-simulated-annealing-optimization-algorithm/
from mpl_toolkits import mplot3d

import random

import numpy as np
import matplotlib.pyplot as plt
#------------------------------------------------------------------------------

number_variables = 4
upper_bounds = [10, 10, 10, 10]   
lower_bounds = [-10, -10, -10, -10]  



def Custo(X):
    x1 = X[0]
    x2 = X[1]
    x3 = X[2]
    x4 = X[3]
    
    value = x1**2 + x2**2 + x3**2 + x4**2 + (0.5*x1 + 0.5*2*x2 + 0.5*3*x3 + 0.5*4*x4)**2 + (0.5*x1 + 0.5*2*x2 + 0.5*3*x3 + 0.5*4*x4)**4

    return value
 
#------------------------------------------------------------------------------
# Simulated Annealing 
X0=np.zeros((number_variables))
for v in range(number_variables):
    print (v)
    X0[v] = random.uniform(lower_bounds[v],upper_bounds[v])


N=int(1e5);  K=7; T0=5e-1; e=1e-1 
X = X0
Xmin = X0
np.random.seed(0); 
fim=0; n=0; k=0; Jmin=Custo(X); Xmin=X; T=T0;
history_J=np.zeros([int(N*K),1]); history_T=np.zeros([int(N*K),1])
X_hat = np.zeros(number_variables)

while not(fim):
    T = T0/np.log2(2+k)
    for n in range(N):
    
        for k in range(number_variables):
            X_hat[k] = X[k] + e*(random.uniform(lower_bounds[k],upper_bounds[k]))
            X_hat[k] = max(min(X[k],upper_bounds[k]),lower_bounds[k])  # repair the solution respecting the bounds
        if np.random.uniform()<np.exp((Custo(X)-Custo(X_hat))/T):
            X = X_hat
            if Custo(X) < Jmin:
                Jmin = Custo(X)
                Xmin = X
            history_J[k*N+n] = Custo(X)
            history_T[k*N+n] = T
    print([k,Jmin])
    k=k+1
    if k == K: fim =1
print(Jmin)
            




