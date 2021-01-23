# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:31:28 2020

@author: Amanda
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

np.random.seed(1); P=100; NC=8;

cluster_centers=np.random.normal(0,1,[2,NC])

aux=np.zeros([2,1]); aux[0]=cluster_centers[0,0]; aux[1]=cluster_centers[1,0]
data_vectors=0.1*np.random.normal(0,1,[2,P])+np.tile(aux,(1,P))
for k in range(1,NC):
    aux=np.zeros([2,1]); aux[0]=cluster_centers[0,k]; aux[1]=cluster_centers[1,k]
    data_vectors=np.concatenate((data_vectors,0.1*np.random.normal(0,1,[2,P])+np.tile(aux,(1,P))),axis=1)

# Função Custo
    ##x*exp(-x^2-y^2),x=-2..2,y=-2..2
def J(X,Y):
    # data_vectors go into X. 
    # codebook, which is under optimization, goes into Y.
    J=0; M,N=np.shape(X); M,K=np.shape(Y)

    # D+=np.min((np.power(np.tile(aux,(1,K))-Y,2),axis=0))
    
    J=(X*(np.exp(np.tile(-X**2)-Y**2,2)))
    return J

# Definitions

N=int(1e4); K=8;  T0=5e-3; epsilon=5e-2 # 


# Initialize Main Loop

np.random.seed(0); X=np.random.normal(0,1,[2,NC])
fim=0; n=0; k=0; Jmin=J(data_vectors,X); Xmin=X; T=T0;
history_J=np.zeros([int(N*K),1]); history_T=np.zeros([int(N*K),1])

# Main Loop

while not(fim):
    T=T0/np.log2(2+k)
    for n in range(0,N):
        Xhat=X+epsilon*np.random.normal(0,1,np.shape(X))
        JX=J(data_vectors,X); JXhat=J(data_vectors,Xhat) 
        if np.random.uniform()<np.exp((JX-JXhat)/T):
            X=Xhat; JX=JXhat
            if JX<Jmin:
                Jmin=JX; Xmin=X;
        history_J[k*N+n]=JX
        history_T[k*N+n]=T
        if np.remainder(n+1,100)==0:
            print([k,n+1,Jmin])
    k+=1
    if k==K: fim=1

print(Jmin)
print(J(data_vectors,cluster_centers)) # 0.01987 (global minimum)
print(Xmin.T)

# Results

plt.rc('font',size=16,weight='bold')

plt.figure()
plt.subplot(211)
plt.plot(history_J)
plt.grid()
plt.subplot(212)
plt.plot(history_T)
plt.grid()

vor=Voronoi(cluster_centers.T)
fig=voronoi_plot_2d(vor)
plt.plot(data_vectors[0,:],data_vectors[1,:],'k.')
plt.plot(Xmin[0,:],Xmin[1,:],'r.',markersize=20)
plt.grid()
plt.show()

