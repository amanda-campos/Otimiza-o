# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:09:32 2020

@author: Amanda
"""
import numpy as np 

J = lambda x: np.linalg.norm(x)**2
fx = lambda x: np.exp(-J(x))
N = int(3e6)
M = int(0.1*N)
x = np.zeros((N,2))
x[0,:] = np.random.random((1,2))**2-1

eps = 1e-4

F_hat = 0

for i in range(1,N):
    
    r = np.random.random((1,2))*2 - 1
    
    x_hat = x[i-1,:] + eps*r
    
    if x_hat[0,0] > 1 : ### Atualização dos valores x_hat dentro dos limites
        x_hat[0,0] = x_hat[0,0] - 2
        
    if x_hat[0,1] > 1 : 
        x_hat[0,1] = x_hat[0,1] - 2 
        
    if x_hat[0,0] < -1 : 
        x_hat[0,0] = -(x_hat[0,0] + 1)
        
    if x_hat[0,1] < -1 : 
        x_hat[0,1] = -(x_hat[0,1] + 1)
        
    if np.random.uniform() < np.exp(J(x[i-1]) - J(x_hat)):
        
        x[i] = x_hat
    else: x[i] = x[i-1,:]
    
    if i<N-M:
        F_hat += fx(x[i])
    print(F_hat/M)
    
values = x[-M,:]


n = np.linalg.norm(values, axis=1)**2

z = np.exp(-n)

print(np.sum(z)/M)

N = int(5e6)
f = lambda x: x*np.exp(-x)
x = np.random.random((N, 2))
x_norm = np.linalg.norm(x, axis=1)**2
z = f(x_norm)
result = np.mean(z)*4
print(result)
    
    
