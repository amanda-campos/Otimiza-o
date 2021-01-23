# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:18:49 2020

@author: Amanda
"""
import numpy as np
import quantecon as qe
# Letra B



M = np.zeros([5,5])

M[0,0] = 1/2*(1-np.exp(-2))
M[1,0] = 1/2*np.exp(-2)
M[2,0] = 0
M[3,0] = 0
M[4,0] = 1/2

print(np.sum(M[:,0]))

M[0,1] = 1/2
M[1,1] = 0
M[2,1] = 1/2
M[3,1] = 0
M[4,1] = 0


print(np.sum(M[:,1]))

M[0,2] = 0
M[1,2] = 1/2*np.exp(-1)
M[2,2] = 1/2*(1-np.exp(-1))
M[3,2] = 1/2
M[4,2] = 0

print(np.sum(M[:,2])) 


M[0,3] = 0
M[1,3] = 0
M[2,3] = 1/2*np.exp(-2)
M[3,3] = 1/2*(2-np.exp(-1)-np.exp(-2))
M[4,3] = 1/2*np.exp(-1)

print(np.sum(M[:,3]))

M[0,4] = 1/2
M[1,4] = 0
M[2,4] = 0
M[3,4] = 1/2 
M[4,4] = 0

print(np.sum(M[:,4]))

print(M)




# ##Fonte: https://python.quantecon.org/finite_markov.html
# import quantecon as qe
# P = [[0.2, 0.8], ##Coluna 1
#       [0.4, 0.6]] ##Coluna 2


# mc = qe.MarkovChain(P)
# mc.stationary_distributions

# M = np.transpose(M)
# print(M)
mc = qe.MarkovChain(np.transpose(M))
mc.stationary_distributions


autovals, autovecs = np.linalg.eig(M)
# print ("Autovetores de A: \n", autovecs[:,0])
# print ("Autovalores de A: \n",autovals)

inv = np.zeros(5)
z = np.sum(autovecs[:,0])
for i in range(0,5):
    print(i)
    inv[i] =  autovecs[i,0] / z
print('Vetor inveriante da matriz M: ' + str(inv) )


##Letra C
import math
T= 0.1/math.log(2,10)
print(np.exp(-0.2/T),
np.exp(-0.4/T),
np.exp(-0.3/T),
np.exp(-0.1/T),
np.exp(-0.2/T))

s = np.exp(-0.2/T) + np.exp(-0.4/T) + np.exp(-0.3/T) + np.exp(-0.1/T) + np.exp(-0.2/T)
print('soma:' + str(s))
print(np.exp(-0.2/T)/s,
      np.exp(-0.4/T)/s,
     np.exp(-0.3/T)/s, 
     np.exp(-0.1/T)/s,
     np.exp(-0.2/T)/s)