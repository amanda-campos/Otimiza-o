# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:29:51 2020

@author: Amanda
"""

import random
import numpy as np
#------------------------------------------------------------------------------

numero_variaveis = 10
limites_max = numero_variaveis*[32.768]   
limites_min = numero_variaveis*[-32.768]    


def Custo(X):
    c = 2*np.pi
    b = 0.2
    a = 20
    d = 10
    sum1 = 0;
    sum2 = 0;
    for ii in range(0,d):
    	xi = X[ii]
    	sum1 = sum1 + xi**2
    	sum2 = sum2 + np.cos(c*xi)
    

    term1 = -a * np.exp(-b*np.sqrt(sum1/d))
    term2 = -np.exp(sum2/d)

    y = term1 + term2 + a + np.exp(1)

    return y
 
#------------------------------------------------------------------------------
# Simulated Annealing 
X0=np.zeros((numero_variaveis))
for v in range(numero_variaveis):
    print (v)
    X0[v] = random.uniform(limites_min[v],limites_max[v])


N=int(1e5);  K=100; T0=1e-3; e=1e-1
X = X0
Xmin = X0
np.random.seed(0); 
fim=0; n=0; k=0; Jmin=Custo(X); Xmin=X; T=T0;
# history_J=np.zeros([int(N*K),1]); history_T=np.zeros([int(N*K),1])
X_hat = np.zeros(numero_variaveis)

while not(fim):
    T = T0/np.log2(2+k)
    for n in range(N):
    
        for v in range(numero_variaveis):
            X_hat[v] = X[v] + e*(random.uniform(limites_min[v],limites_max[v]))
            X_hat[v] = max(min(X[v],limites_max[v]),limites_min[v])  # repair the solution respecting the bounds
        if np.random.uniform()<np.exp((Custo(X)-Custo(X_hat))/T):
            X = X_hat
            if Custo(X) < Jmin:
                Jmin = Custo(X)
                Xmin = X
            # history_J[k*N+n] = Custo(X)
            # history_T[k*N+n] = T
    print([k,Jmin])
    k=k+1
    if k == K: fim =1
print(Jmin)




