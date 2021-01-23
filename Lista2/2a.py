# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 17:11:11 2020

@author: Amanda
"""


import numpy as np
import quantecon as qe

M = np.zeros([5,5])

M[0,0] = 0
M[1,0] = 1/4
M[2,0] = 1/4
M[3,0] = 1/4
M[4,0] = 1/4

print(np.sum(M[:,0]))

M[0,1] = 1/4*np.exp(-3)
M[1,1] = 1/4*(1-np.exp(-3)) + 1/4*(1-np.exp(-1)) + 1/4*(1-np.exp(-2))
M[2,1] = 1/4*np.exp(-1)
M[3,1] = 1/4
M[4,1] = 1/4*np.exp(-2)

print(np.sum(M[:,1]))

M[0,2] = 1/4*np.exp(-2)
M[1,2] = 1/4
M[2,2] = 1/4*(1-np.exp(-2)) + 1/4*(1-np.exp(-1)) 
M[3,2] = 1/4
M[4,2] = 1/4*np.exp(-1)

print(np.sum(M[:,2]))

M[0,3] = 1/4*np.exp(-4)
M[1,3] = 1/4*np.exp(-1)
M[2,3] = 1/4*np.exp(-2)
M[3,3] = 1/4*(1-np.exp(-4)) + 1/4*(1-np.exp(-1)) + 1/4*(1-np.exp(-2)) + 1/4*(1-np.exp(-3))
M[4,3] = 1/4*np.exp(-3)

print(np.sum(M[:,3]))

M[0,4] = 1/4*np.exp(-1)
M[1,4] = 1/4
M[2,4] = 1/4
M[3,4] = 1/4
M[4,4] = 1/4*(1-np.exp(-1))

print(np.sum(M[:,4]))



## 2b

p0 = np.array([[np.exp(0.5)],[np.exp(0.2)], [np.exp(0.3)], [np.exp(0.1)], [np.exp(0.4)]])

M2 = M.dot(M)
M3 = M2.dot(M)
M4 = M3.dot(M)

print(M4.dot(p0))

## 2b

autovals, autovecs = np.linalg.eig(M)
print ("Autovetores de A: \n", autovecs[:,0])
print ("Autovalores de A: \n",autovals)

inv = np.zeros(5)
z = np.sum(autovecs[:,0])
for i in range(0,5):
    print(i)
    inv[i] =  autovecs[i,0] / z
print('Vetor inveriante da matriz M: ' + str(inv) )

mc = qe.MarkovChain(np.transpose(M))
mc.stationary_distributions

