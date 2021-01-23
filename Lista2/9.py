# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:44:35 2020

@author: Amanda
"""

import numpy as np
from numpy import log as ln
import quantecon as qe

## Letra B

T= 1/ln(3)

M = np.zeros([5,5])

M[0,0] = 0
M[1,0] = 1/4
M[2,0] = 1/4
M[3,0] = 1/4
M[4,0] = 1/4

print(np.sum(M[:,0]))

M[0,1] = 1/4*np.exp(-3/T)
M[1,1] = 2/4*(1-np.exp(-3/T)) + 1/4*(1-np.exp(-2/T)) + 1/4*(1-np.exp(-1/T)) 
M[2,1] = 1/4*np.exp(-2/T)
M[3,1] = 1/4*np.exp(-1/T)
M[4,1] = 1/4*np.exp(-3/T)


print(np.sum(M[:,1]))

M[0,2] = 1/4*np.exp(-1/T)
M[1,2] = 1/4
M[2,2] = 2/4*(1-np.exp(-1/T))
M[3,2] = 1/4
M[4,2] = 1/4*np.exp(-1/T)

print(np.sum(M[:,2])) 


M[0,3] = 1/4*np.exp(-2/T)
M[1,3] = 1/4
M[2,3] = 1/4*np.exp(-1/T)
M[3,3] = 1/4*(1-np.exp(-1/T)) + 2/4*(1-np.exp(-2/T))
M[4,3] = 1/4*np.exp(-2/T)

print(np.sum(M[:,3]))

M[0,4] = 1/4 
M[1,4] = 1/4
M[2,4] = 1/4 
M[3,4] = 1/4 
M[4,4] = 0

print(np.sum(M[:,4]))


print(M)

mc = qe.MarkovChain(np.transpose(M))
mc.stationary_distributions
