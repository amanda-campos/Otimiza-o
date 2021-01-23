# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:11:45 2020

@author: Amanda
"""


## REFERÊNCIA: https://learnwithpanda.com/2020/04/04/python-code-of-simulated-annealing-optimization-algorithm/
from mpl_toolkits import mplot3d

import random

import numpy as np
import matplotlib.pyplot as plt
#------------------------------------------------------------------------------

number_variables = 2
upper_bounds = [2, 2]   
lower_bounds = [-2, -2]  

 
def Custo(X):
    x=X[0]
    y=X[1]
    value = x*np.exp(-x**2-y**2)
    return value
 
#------------------------------------------------------------------------------
# Simulated Annealing 
X0=np.zeros((number_variables))
for v in range(number_variables):
    X0[v] = random.uniform(lower_bounds[v],upper_bounds[v])


N=int(1e5);  K=7; T0=5e-1; e=1e-1 
X = X0
Xmin = X0
np.random.seed(0); 
fim=0; n=0; k=0; Jmin=Custo(X); Xmin=X; T=T0;
history_J=np.zeros([int(N*K),1]); history_T=np.zeros([int(N*K),1])
X_hat = np.zeros(number_variables)

while not(fim):
    T = T0/np.log2(2+k)
    for n in range(N):
    
        for k in range(number_variables):
            X_hat[k] = X[k] + e*(random.uniform(lower_bounds[k],upper_bounds[k]))
            X_hat[k] = max(min(X[k],upper_bounds[k]),lower_bounds[k])  # repair the solution respecting the bounds
        if np.random.uniform()<np.exp((Custo(X)-Custo(X_hat))/T):
            X = X_hat
            if Custo(X) < Jmin:
                Jmin = Custo(X)
                Xmin = X
            history_J[k*N+n] = Custo(X)
            history_T[k*N+n] = T
    print([k,Jmin])
    k=k+1
    if k == K: fim =1
print(Jmin)
            
#         J = Custo(X)
#         dJ = abs(J - best_fitness)
#         if i == 0 and j == 0:
#             J_hat = dJ
             
#         if J < best_fitness:
#             p = math.exp(-J_hat/(J_hat*T))
#             # make a decision to accept the worse solution or not
#             if random.random()<p:
#                 accept = True # this worse solution is accepted
#             else:
#                 accept = False # this worse solution is not accepted
#         else:
#             accept = True # accept better solution
#         if accept==True:
#             X_hat = X # update the best solution
#             best_fitness = Custo(X_hat)
#             n = n + 1 # count the solutions accepted
#             J_hat = (J_hat *(n-1) + dJ)/n # update EA
     
#     print('interação: {}, X_hat: {}, best_fitness: {}'.format(i, X_hat, best_fitness))
#     record_best_fitness.append(best_fitness)
#     # Cooling the temperature
#     T = T*cooling
#     # Stop by computing time
#     end = time.time()
#     if end-start >= computing_time:
#         break
# plt.plot(record_best_fitness)


# Plotar função
# x*exp(-x^2-y^2),x=-2..2,y=-2..2
def f(x, y):
    return x*np.exp(-x**2-y**2)

x = np.linspace(-2, 2, 30)
y = np.linspace(-2, 2, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('x*exp(-x^2-y^2)');

# fig = plt.figure()
# ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');




