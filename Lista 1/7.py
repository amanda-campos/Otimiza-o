# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:19:28 2020

@author: Amanda
"""
import numpy as np
import matplotlib.pyplot as plt

# Função Custo

def Custo(x):
    J = -x + 100*(pow(x-0.2,2)*(pow(x-0.8,2)))
    return J


X0 = 0
X = X0
J0 = Custo(X0)
Jatual = J0

N = 100000
K = 8
T0 = 10
e = 5e-2
fim = 0
n = 0
k = 1
Jmin = Jatual 
Xmin = X

history_J=np.zeros([int(N*K),1]); history_T=np.zeros([int(N*K),1])


while not(fim):
    T=T0/np.log2(2+k)
    for n in range(0,N):    
        X_hat = X + e*np.random.uniform()
        JX = Custo(X)
        JX_hat = Custo(X_hat)
        if np.random.uniform() < np.exp((JX-JX_hat)/T):
            X = X_hat
            JX = JX_hat
            if JX<Jmin:
                Jmin = JX
                Xmin = X
        if np.remainder(n+1,100)==0:
            print([k,n+1,Xmin,Jmin])

    k+=1
    if k==K: fim=1

print(Jmin)














