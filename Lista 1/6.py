# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:44:52 2020

@author: Amanda
"""


import numpy as np
import matplotlib as plt

# Função Custo

def J(X):
    L=0.5
    Xorigin=np.zeros([2,1])    
    JA=np.mean(np.sum(np.power(X-np.tile(Xorigin,(1,P)),2),axis=0))
    JB=0
    for i in range(0,P):
        for j in range(i+1,P):
            JB+=np.sum(1/(np.power(X[:,i]-X[:,j],2)))
    JB=JB/(P*(P-1)/2)
    return JA+L*JB

# Definitions

N=int(1e3); epsilon=1e-1; 

np.random.seed(0); P=5; X=np.random.normal(0,1,[2,P])
fim=0; n=0; Jmin=J(X); Xmin=X; T=1; M = 0.1*N


for n in range(0,N):
    Xhat=X+epsilon*np.random.normal(0,1,np.shape(X)) 
    
    if np.random.uniform()<np.exp((J(X)-J(Xhat))/T):
        X = Xhat
        
    else:
        X=X
       
### B
        
J_1 = lambda r: 4*r**2 + 6.5/(r**2)
J_2 = lambda r: 5*r**2 + 5/(r**2)
T = 0.1
r_dir = 1
r_esq = 1.1291

print('r=1.1291', 'J_1 = ', J_1(r_esq))
print('r=1.0', 'J_2 = ', J_2(r_dir))


p = np.exp(-(J_2(r_dir))/0.1) / np.exp(-(J_1(r_esq))/0.1)
print(p)











