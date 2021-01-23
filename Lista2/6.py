# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 19:07:53 2020

@author: Amanda
"""



import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d


P=8; NC=2;
cluster_centers=np.random.normal(0,1,[2,NC])

aux=np.zeros([2,1]); aux[0]=cluster_centers[0,0]; aux[1]=cluster_centers[1,0]
data_vectors = np.array([1,1,1,0,1,0,0,0])

for k in range(1,NC):
    aux=np.zeros([2,1]); aux[0]=cluster_centers[0,k]; aux[1]=cluster_centers[1,k]
    # data_vectors=np.concatenate((data_vectors,0.1*np.random.normal(0,1,[2,P])+np.tile(aux,(1,P))),axis=1)

def pertubação(X): #Criação de uma nova sequência de cidades visitadas
    pos1 = np.random.randint(1,5)
    pos2 = np.random.randint(1,5)
    aux1 = X[pos1]
    aux2 = X[pos2]
    X[pos1] = aux2
    X[pos2] = aux1
    return X

# Given Cost Function

def J(X,Y):

    D=0; M,N=np.shape(X); M,K=np.shape(Y)
    aux=np.zeros([2,1])
    for n in range(0,N):
        aux[0]=X[0,n]; aux[1]=X[1,n];
        D+=np.min(np.sum(np.power(np.tile(aux,(1,K))-Y,2),axis=0))
    return D/N


N=int(1e3); K=20; T0=0.2;  epsilon=0.2  # (0.28410)


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
