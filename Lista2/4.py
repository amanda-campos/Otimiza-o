# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 18:18:37 2020

@author: Amanda
"""


import numpy as np
import quantecon as qe
T= 1
print(np.exp(-0.3/T),
np.exp(-0.1/T),
np.exp(-0.1/T),
np.exp(-0.2/T))



M = np.zeros([4,4])

M[0,0] = 0
M[1,0] = 1/3
M[2,0] = 1/3
M[3,0] = 1/3


print(np.sum(M[:,0]))

M[0,1] = 1/3*np.exp(-0.2/T)
M[1,1] = 1/3*(1-np.exp(-0.2/T)) + 1/3*(1-np.exp(-0.1/T)) 
M[2,1] = 1/3
M[3,1] = 1/3*np.exp(-0.1/T)

print(np.sum(M[:,1]))

M[0,2] = 1/3*np.exp(-0.2/T)
M[1,2] = 1/3
M[2,2] = 1/3*(1-np.exp(-0.2/T)) + 1/3*(1-np.exp(-0.1/T)) 
M[3,2] = 1/3*np.exp(-0.1/T)

print(np.sum(M[:,2]))

M[0,3] = 1/3*np.exp(-0.1/T)
M[1,3] = 1/3
M[2,3] = 1/3
M[3,3] = 1/3*(1-np.exp(-0.1/T)) 

print(np.sum(M[:,3]))

print(M)

mc = qe.MarkovChain(np.transpose(M))

print(mc.stationary_distributions)

autovals, autovecs = np.linalg.eig(M)
print ("Autovetores de A: \n", autovecs[:,0])
print ("Autovalores de A: \n",autovals)

inv = np.zeros(4)
z = np.sum(autovecs[:,0])
for i in range(0,4):
    print(i)
    inv[i] =  autovecs[i,0] / z
print('Vetor inveriante da matriz M: ' + str(inv) )




