# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:06:04 2020

@author: Amanda
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# N_execuções = 150
# hist = np.zeros([N_execuções])

DNA_SIZE = 20            # DNA (real number)
LIMITES = [-32.768, 32.768]        # limites superior e inferior da função
N_GERAÇÕES = 50
TAM_POP = 200           # tamanho da população
 


def F(x):

    firstSum = 0.0
    secondSum = 0.0
    for c in x: 
        print(c)
        
        firstSum += c**2
        secondSum += math.cos(2*math.pi*c)
    n = float(len(x))
    return -(-20.0*math.exp(-0.2*math.sqrt(firstSum/n)) - math.exp(secondSum/n) + 20 + math.e)


def mutação(pop):

    filhos = {'DNA': np.empty((TAM_POP, DNA_SIZE))}
    filhos['sigma'] = np.empty_like(filhos['DNA'])
    
    for X_filhos, Sigma_filhos in zip(filhos['DNA'], filhos['sigma']):
        
        X_filhos = pop['DNA']
        Sigma_filhos = pop['sigma']
        
        
    
        X_filhos = X_filhos + Sigma_filhos*np.random.randn(*X_filhos.shape)
        Sigma_filhos[:] = np.exp(1/np.sqrt(2*20) * np.random.randn(*X_filhos.shape))*np.exp(1/np.sqrt(2*np.sqrt(20)) * np.random.randn(*X_filhos.shape))*Sigma_filhos  
        
    
        X_filhos[:] = np.clip(X_filhos, *LIMITES)    
    return filhos


def seleção(filhos):

    for key in ['DNA', 'sigma']:
        pop[key] = (filhos[key])


    return pop

## População inicial
pop = dict(DNA=5 * np.random.rand(1, DNA_SIZE).repeat(TAM_POP, axis=0), 
           sigma=np.random.rand(TAM_POP, DNA_SIZE))          
# x = np.linspace(*DNA_BOUND, 200)
# plt.plot(x, F(x))

i = 0
menor = np.zeros([N_GERAÇÕES])
media = np.zeros([N_GERAÇÕES])
maior = np.zeros([N_GERAÇÕES])


for i in range(N_GERAÇÕES):

    filhos = mutação(pop)
    pop = seleção(filhos)  


    for k in range(TAM_POP):
        menor[i] = -np.max(F(pop['DNA'][k,:]))
        maior[i] = -np.min(F(pop['DNA'][k,:]))
        media[i] = -np.mean(F(pop['DNA'][k,:]))

    
plt.plot(media, label='Média') 
plt.plot(menor, label='Mínimo')
plt.plot(maior, label='Máximo')
plt.legend()   
plt.xlabel('Gerações')
plt.ylabel('Aptidão')
plt.grid()





 