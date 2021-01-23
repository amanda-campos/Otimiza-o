# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:44:35 2020

@author: Amanda
"""
import math
import numpy as np
import quantecon as qe
# def perturbacao(x): ### +1, +2 ou +3
#     e = math.ceil(np.remainder(2+(np.random.uniform()*3),3))
    
#     print(e)
#     x_hat = x + e
#     if x_hat == 5:
#         return 1
#     if x_hat == 6:
#         return 2
#     if x_hat == 7:
#         return 3
#     else:
#         return x_hat
    

# def Custo(x):
#     if x==1:
#         return 7
#     if x==2:
#         return 1
#     if x==3:
#         return 10
#     if x==4:
#         return 4
    
# X0 = 1
# X = X0
# J0 = Custo(X0)
# Jatual = J0

# N = 100
# K = 8
# T0 = 1
# fim = 0
# n = 0
# k = 1
# Jmin = Jatual 
# Xmin = X


# while not(fim):
#     T=T0/np.log2(2+k)
#     for n in range(0,N):    
#         X_hat = perturbacao(X)
#         JX = Custo(X)
#         JX_hat = Custo(X_hat)
#         if np.random.uniform() < np.exp((JX-JX_hat)/T):
#             X = X_hat
#             JX = JX_hat
#             if JX<Jmin:
#                 Jmin = JX
#                 Xmin = X
#         if np.remainder(n+1,100)==0:
#             print([k,n+1,Xmin,Jmin])
#     k+=1
#     if k==K: fim=1

# print(Jmin)


## Letra B

T= 10

M = np.zeros([4,4])

M[0,0] = 1/3*(1-np.exp(-3/T))
M[1,0] = 1/3
M[2,0] = 1/3*np.exp(-3/T)
M[3,0] = 1/3


print(np.sum(M[:,0]))

M[0,1] = 1/3*np.exp(-6/T)
M[1,1] = 1/3*(1-np.exp(-6/T)) + 1/3*(1-np.exp(-9/T)) + 1/3*(1-np.exp(-3/T)) 
M[2,1] = 1/3*np.exp(-9/T)
M[3,1] = 1/3*np.exp(-3/T)

print(np.sum(M[:,1]))

M[0,2] = 1/3
M[1,2] = 1/3
M[2,2] = 0
M[3,2] = 1/3

print(np.sum(M[:,2])) 

M[0,3] = 1/3*np.exp(-3/T)
M[1,3] = 1/3
M[2,3] = 1/3*np.exp(-6/T)
M[3,3] = 1/3*(1-np.exp(-3/T)) + 1/3*(1-np.exp(-6/T))

print(np.sum(M[:,3]))

print(M)

mc = qe.MarkovChain(np.transpose(M))
mc.stationary_distributions

autovals, autovecs = np.linalg.eig(M)
print ("Autovetores de A: \n", autovecs[:,0])
print ("Autovalores de A: \n",autovals)

inv = np.zeros(4)
z = np.sum(autovecs[:,0])
for i in range(0,4):
    print(i)
    inv[i] =  autovecs[i,0] / z
print('Vetor inveriante da matriz M: ' + str(inv) )