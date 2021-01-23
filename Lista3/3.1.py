# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:29:51 2020

@author: Amanda
"""
# https://www.sfu.ca/~ssurjano/rastr.html
import numpy as np
import math
#------------------------------------------------------------------------------

numero_variaveis = 20
b = 5.12  ## Limite superior
a = -5.12  ## Limite inferior    limites = [a,b)


def Custo(X):
    numero_variaveis = 20
#https://en.wikipedia.org/wiki/Rastrigin_function#:~:text=In%20mathematical%20optimization%2C%20the%20Rastrigin,has%20been%20generalized%20by%20Rudolph.
    d = numero_variaveis
    sum = 0;

    for ii in range(0,d):
    	xi = X[ii]
    	sum = sum + (xi**2 - 10*math.cos(2*math.pi*xi))


    y = 10*d + sum

    return y
 
#------------------------------------------------------------------------------
# Simulated Annealing 
X0 = (b-a)*np.random.rand(numero_variaveis) + a

N=int(1e5);  K=100; T0=5e-1; e=1e-1
X = X0
Xmin = X0
np.random.seed(0); 
fim=0; n=0; k=0; Jmin=Custo(X); Xmin=X; T=T0;


while not(fim):
    T = T0/(1+k)
    # T = T0/np.log2(2+k)
    for n in range(N):
        X_hat = X + e*(np.random.standard_cauchy(np.shape(X)))
        # X_hat = X + e*(np.random.normal(0,1,np.shape(X)))
        
        if np.random.uniform()<np.exp((Custo(X)-Custo(X_hat))/T):
            X = X_hat
            if Custo(X) < Jmin:
                Jmin = Custo(X)
                Xmin = X

    print([k,Jmin])
    k=k+1
    if k == K: fim =1
print(Jmin)


