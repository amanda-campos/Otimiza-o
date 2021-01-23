# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 13:12:38 2020

@author: Amanda
"""


import numpy as np
import matplotlib.pyplot as plt
import math


def F(x):
    y = -(-20.0*math.exp(-0.2*math.sqrt(x**2.0)) - math.exp(math.cos(2.0*math.pi*x)) + 20.0 + math.e)
    return y
F = np.vectorize(F) 

Nruns = 100; Jmax = 0; Ngerações = 100; mu = 20;
Xmax = np.zeros([2])
for i in range(Nruns):
    
    Pop = 2*np.random.rand(1,20) - 0.5
    
    ngerações = 0
    
    while ngerações < Ngerações:
        
        J = F(Pop).T
        
        ngerações +=1
        if np.max(J) > Jmax:
            Jmax = max(J)
            Xmax[0] = Pop(0,np.argwhere(J[:,0] == max(J)))
            Xmax[1] = Pop(1,np.argwhere(J[:,0] == max(J)))
            
        #Seleção de Pais SUS
        M = np.zeros([mu,2])
        for i in range(20):
            M[i,0] = int(i)
            M[i,1] =  (J[i]-min(J))/sum(J-min(J))
            
        p = M[M[:,1].argsort(),]
        a = p.cumsum(axis=0)
        a = a[:,1]
        MP2 = np.zeros((mu,1))
        r0 = np.random.rand(1,1)/mu; r = r0; k = 0; i = 0;
        while k<mu:
            while r<=a[i]:
                MP2[k] = p[i,1]
                r = r+1/mu
                k = k+1
            i=i+1
        MP2(np.argwhere(MP2==0)) = p[mu-1,1]
         # Recombinação        
        Pop = Pop(:,MP2) 0.5*Pop(:,MP2(1:2:end-1))+Pop(:,MP2(2:2:end))