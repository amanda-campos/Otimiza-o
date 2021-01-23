# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 18:09:46 2020

@author: Amanda
"""
import numpy as np


X = np.array([[5,4,5,-5,-4],[4,5,5,-4,-5]])

M,N=np.shape(X)
K = 3 #número de clusters
Y=np.array([[0,1,-1],[0,1,-1]])
d=np.zeros([K,N])
T = 10
p_ygivenx=np.zeros([K,N])

# Partition Condition
for n in range(0,N):
    for k in range(0,K):
        d[k,n]=np.sum(np.power(X[:,n]-Y[:,k],2))
        p_ygivenx[k,n]=np.exp(-d[k,n]/T)
Zx=np.sum(p_ygivenx,axis=0)   
p_ygivenx=p_ygivenx/np.tile(Zx,(K,1))

# Centroid Condition
Y=np.zeros([M,K])
for k in range(0,K):
    y=np.zeros(M)
    w=0
    for n in range(0,N):
        y+=p_ygivenx[k,n]*X[:,n]
        w+=p_ygivenx[k,n]
    Y[:,k]=y/w