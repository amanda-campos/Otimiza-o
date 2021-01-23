# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:19:28 2020

@author: Amanda
"""

import numpy as np
# Função Custo


def pertubação(X): #Criação de uma nova sequencia de cidades visitadas
    pos1 = np.random.randint(1,5)
    pos2 = np.random.randint(1,5)
    
    aux1 = X[pos1] 
    aux2 = X[pos2] 
    
    X[pos1] = aux2
    X[pos2] = aux1    
    
    return X

def Custo(X):  ##Cálculo das distancias
    if (np.array_equal(X,np.array([1,2,3,4,5])) or  np.array_equal(X,np.array([1,5,4,3,2]))):
        J = 5
    elif (np.array_equal(X,np.array([1,2,3,5,4])) or np.array_equal(X,np.array([1,2,4,3,5])) or 
         np.array_equal(X,np.array([1,2,5,4,3])) or np.array_equal(X,np.array([1,5,4,2,3])) or 
         np.array_equal(X,np.array([1,5,3,4,2])) or np.array_equal(X,np.array([1,5,2,3,4])) or 
         np.array_equal(X,np.array([1,3,2,4,5])) or np.array_equal(X,np.array([1,3,4,5,2])) or
         np.array_equal(X,np.array([1,4,5,3,2])) or np.array_equal(X,np.array([1,4,3,2,5])) ):
        J = 6.24
       
    elif ( np.array_equal(X,np.array([1,2,4,5,3])) or np.array_equal(X,np.array([1,2,5,3,4])) or 
         np.array_equal(X,np.array([1,5,3,2,4])) or  np.array_equal(X,np.array([1,5,2,4,3])) or 
         np.array_equal(X,np.array([1,3,2,5,4])) or  np.array_equal(X,np.array([1,3,4,2,5])) or 
         np.array_equal(X,np.array([1,3,5,4,2])) or  np.array_equal(X,np.array([1,4,5,2,3])) or
         np.array_equal(X, np.array([1,4,3,5,2])) or  np.array_equal(X,np.array([1,4,2,3,5]))):
        J = 6.86
        
    else: #( np.array_equal(X,np.array([1,3,5,2,4])) or  np.array_equal(X,np.array([1,4,2,5,3]))):
        J = 8.10
    return J

X0 = np.array([1,3,5,2,4]) #Percurso inicial aleatório
X = X0
J0 = Custo(X0)
Jatual = J0

N = 100
K = 8
T0 = 1
e = 5e-2
fim = 0
n = 0
k = 1
Jmin = Jatual 
Xmin = X


while not(fim):
    T=T0/np.log2(2+k)
    for n in range(0,N):    
        X_hat = pertubação(X)
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




## Letra B


PJ5 = 2*np.exp(-5)/ (2*np.exp(-5) + 10*np.exp(-6.24) + 10*np.exp(-6.86) + 2*np.exp(-8.10))

PJ6 = 10*np.exp(-6.24)/ (2*np.exp(-5) + 10*np.exp(-6.24) + 10*np.exp(-6.86) + 2*np.exp(-8.10))

PJ7 = 10*np.exp(-6.86)/ (2*np.exp(-5) + 10*np.exp(-6.24) + 10*np.exp(-6.86) + 2*np.exp(-8.10))

PJ8 = 2*np.exp(-8.10)/ (2*np.exp(-5) + 10*np.exp(-6.24) + 10*np.exp(-6.86) + 2*np.exp(-8.10))


