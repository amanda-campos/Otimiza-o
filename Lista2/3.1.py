# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:29:51 2020

@author: Amanda
"""

import numpy as np
#------------------------------------------------------------------------------

numero_variaveis = 1
b = 32.768  ## Limite superior
a = -32.768 ## Limite inferior    limites = [a,b)


def Custo(X):
    numero_variaveis = 1
    # transformar matriz 2*10 em vetor de 20 dimensões
    A = np.zeros(2*numero_variaveis)
    for i in range(0,numero_variaveis):
        A[i] = X[0,i]
    for i in range(0,numero_variaveis):
        A[i+numero_variaveis] = X[1,i]
        
    c = 2*np.pi
    b = 0.2
    a = 20
    d = 2*numero_variaveis
    sum1 = 0;
    sum2 = 0;
    for ii in range(0,d):
    	xi = A[ii]
    	sum1 = sum1 + xi**2
    	sum2 = sum2 + np.cos(c*xi)
    

    term1 = -a * np.exp(-b*np.sqrt(sum1/d))
    term2 = -np.exp(sum2/d)

    y = term1 + term2 + a + np.exp(1)

    return y
 
#------------------------------------------------------------------------------
# Simulated Annealing 
X0 = (b-a)*np.random.rand(2,numero_variaveis) + a

N=int(1e5);  K=100; T0=5e-1; e=1e-1
X = X0
Xmin = X0
np.random.seed(0); 
fim=0; n=0; k=0; Jmin=Custo(X); Xmin=X; T=T0;


while not(fim):
    T = T0/np.log2(2+k)
    for n in range(N):
        X_hat = X + e*(np.random.normal(0,1,np.shape(X)))
        # X_hat = max(min(X,b),a) # inclui a sulução no limites
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


