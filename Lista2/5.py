# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:06:44 2020

@author: Amanda
"""


import numpy as np
import quantecon as qe
## M1
# T= 0.5

# M = np.zeros([4,4])

# M[0,0] = 1-np.exp(-0.1/T)
# M[1,0] =0
# M[2,0] = np.exp(-0.1/T)
# M[3,0] = 0


# print(np.sum(M[:,0]))

# M[0,1] = 0
# M[1,1] = 0
# M[2,1] = 0
# M[3,1] = 1

# print(np.sum(M[:,1]))

# M[0,2] = 1
# M[1,2] = 0
# M[2,2] = 0
# M[3,2] = 0

# print(np.sum(M[:,2])) 

# M[0,3] = 0
# M[1,3] = np.exp(-0.2/T)
# M[2,3] = 0
# M[3,3] = 1-np.exp(-0.2/T)

# print(np.sum(M[:,3]))

# print(M)

# mc = qe.MarkovChain(np.transpose(M))
# # print('Vetores invariantes:')
# mc.stationary_distributions



# M2
T= 0.5

M = np.zeros([4,4])

M[0,0] = 1-np.exp(-0.1/T)
M[1,0] =  np.exp(-0.1/T)
M[2,0] =0
M[3,0] = 0


print(np.sum(M[:,0]))

M[0,1] = 1
M[1,1] = 0
M[2,1] = 0
M[3,1] = 0

print(np.sum(M[:,1]))

M[0,2] = 0
M[1,2] = 0
M[2,2] = 0
M[3,2] = 1

print(np.sum(M[:,2])) 

M[0,3] = 0
M[1,3] = 0
M[2,3] = np.exp(-0.2/T)
M[3,3] = 1-np.exp(-0.2/T)

print(np.sum(M[:,3]))

print(M)

# mc = qe.MarkovChain(np.transpose(M))
# mc.stationary_distributions

autovals, autovecs = np.linalg.eig(M)
print ("Autovetores de A: \n", autovecs[:,0])
print ("Autovalores de A: \n",autovals)

inv = np.zeros(4)
z = np.sum(autovecs[:,0])
for i in range(0,4):
    print(i)
    inv[i] =  autovecs[i,0] / z
print('Vetor inveriante da matriz M: ' + str(inv) )

## Letra B

T= 0.5
print(np.exp(-0.2/T),
np.exp(-0.3/T),
np.exp(-0.3/T),
np.exp(-0.1/T))


# ## Letra C

# print( 2*np.exp(-0.3/T)/(np.exp(-0.2/T)+2*np.exp(-0.3/T)+np.exp(-0.1/T)))

