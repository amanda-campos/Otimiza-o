# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:33:42 2020

@author: Amanda
"""

import numpy as np
   

# LETRA A           
M = np.array([[0.5,0.25,0.25],[0.25,0.50,0.25], [0.25, 0.25, 0.50]])

p0 = np.array([[0.3],[0.4], [0.3]])

M2 = M.dot(M)
M3 = M2.dot(M)

print(M3.dot(p0))


## LETRA B
a = np.random.uniform(0.00,0.25,1)
b = np.random.uniform(0.25,0.75,1)
c = np.random.uniform(0.75,1.00,1)

p0 = np.array([a,b,c])

M = np.array([[0.5,0.25,0.25],[0.25,0.50,0.25], [0.25, 0.25, 0.50]])

M2 = M.dot(M)
M3 = M2.dot(M)

print(M3.dot(p0))

# LETRA C
M = np.array([[0.5,0.25,0.25],[0.25,0.50,0.25], [0.25, 0.25, 0.50]])
M2 = M.dot(M)
M3 = M2.dot(M)

C = np.zeros((100,4))


for i in range(100):
    prob = np.random.choice([0,1,2])

    if prob == 0:
        a = np.random.uniform(0.00,0.50,1)
        b = np.random.uniform(0.50,0.75,1)
        c = np.random.uniform(0.75,1.00,1)       
        p0 = np.array([a,b,c])
    
    if prob == 1:
        a = np.random.uniform(0.00,0.25,1)
        b = np.random.uniform(0.25,0.75,1)
        c = np.random.uniform(0.75,1.00,1)        
        p0 = np.array([a,b,c])    
    
    if prob == 2:
        a = np.random.uniform(0.00,0.25,1)
        b = np.random.uniform(0.25,0.50,1)
        c = np.random.uniform(0.50,1.00,1)   
        p0 = np.array([a,b,c]) 
 
    C[i,0] = np.linalg.norm(p0)
    C[i,1] = np.linalg.norm(M.dot(p0))
    C[i,2] = np.linalg.norm(M2.dot(p0))
    C[i,3] = np.linalg.norm(M3.dot(p0))
    
## LETRA D   
import matplotlib.pyplot as plt 
plt.figure(1)
plt.hist(C, 4)
plt.legend('0123')
plt.show()






