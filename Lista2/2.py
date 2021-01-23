# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:03:41 2020

@author: Amanda
"""
import numpy as np
import matplotlib.pyplot as plt 
## 
def J(x):
    if x == 1:
        return 0.5
    if x == 2:
        return 0.2
    if x == 3:
        return 0.3
    if x == 4:
        return 0.1
    if x == 5:
        return 0.4

N = 1000
M = 0.1*N
Temp = np.zeros(10)
Temp[0] = 0.1; Temp[1] = 0.0631; Temp[2] = 0.05; Temp[3] = 0.0431;Temp[4] = 0.0387
Temp[5] = 0.0356; Temp[6] = 0.0333; Temp[7] = 0.0315; Temp[8] = 0.0301; Temp[9] = 0.0289
x = np.zeros(N)
n = 0
x[n] = np.random.choice([1,2,3,4,5])

i = 0; fim = 0
k = 1; K=11

while not(fim):    
    T = Temp[i]
    i += 1 
    for n in range(1,N):
        perturbacao = np.random.choice([-1,1])
        x_hat = x[n-1] + perturbacao
        if x_hat == 6:
            x_hat = 1
        elif x_hat == 0:
            x_hat= 5
        
        if np.random.uniform(0,1)< np.exp((J(x[n-1]) - J(x_hat))/T):
            x[n] = x_hat
        else:
            x[n] = x[n-1]
            
    y = np.linspace(0,6,1000)
    plt.figure(1)
    plt.hist(x, 5)
    plt.title('T = ' + str(T))
    plt.show()
    

    k+=1
    if k==K: fim=1        



