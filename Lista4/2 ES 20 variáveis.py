# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:06:04 2020

@author: Amanda
"""

import numpy as np
import matplotlib.pyplot as plt
import math

N_execuções = 150
hist = np.zeros([N_execuções])
for ii in range(N_execuções):
        
    DNA_SIZE = 20            # DNA (real number)
    LIMITES = [-32.768, 32.768]        # limites superior e inferior da função
    N_GERAÇÕES = 200
    TAM_POP = 30           # tamanho da população
    N_FILHOS = 200  
    
    
    def F(x):
    
        firstSum = 0.0
        secondSum = 0.0
        for c in x: 
            print(c)
            
            firstSum += c**2
            secondSum += math.cos(2*math.pi*c)
        n = float(len(x))
        return -(-20.0*math.exp(-0.2*math.sqrt(firstSum/n)) - math.exp(secondSum/n) + 20 + math.e)
    
    
    def recombinação(pop, n_filhos):
    
    
        filhos = {'DNA': np.empty((n_filhos, DNA_SIZE))}
        filhos['sigma'] = np.empty_like(filhos['DNA'])
        for X_filhos, Sigma_filhos in zip(filhos['DNA'], filhos['sigma']):
            # Recombinação
            p1, p2 = np.random.choice(np.arange(TAM_POP), size=2, replace=False)
            cp = np.random.randint(0, 2, DNA_SIZE, dtype=np.bool)  # pontos de crossover 
            X_filhos[cp] = pop['DNA'][p1, cp]
            X_filhos[~cp] = pop['DNA'][p2, ~cp]
            Sigma_filhos[cp] = pop['sigma'][p1, cp]
            Sigma_filhos[~cp] = pop['sigma'][p2, ~cp]
    
            # Mutação
            
            Sigma_filhos[:] = np.exp(1/np.sqrt(20) * np.random.randn(*Sigma_filhos.shape))*Sigma_filhos    # > 0
            X_filhos += Sigma_filhos * np.random.randn(*X_filhos.shape)
            X_filhos[:] = np.clip(X_filhos, *LIMITES)    
        return filhos
    
    
    def seleção(pop, filhos):
    
        for key in ['DNA', 'sigma']:
            pop[key] = np.vstack((pop[key], filhos[key]))
        for i in range(230):
            fitness[i] = F(pop['DNA'][i,:])
            
        # fitness = custo_fitness(F(pop['DNA']))           
        ind = np.arange(pop['DNA'].shape[0])
        otim_ind = ind[fitness.argsort()][-TAM_POP:]   
        for k in ['DNA', 'sigma']:
            pop[k] = pop[k][otim_ind]
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
    n = TAM_POP + N_FILHOS 
    fitness = np.zeros([n])
    
    for i in range(N_GERAÇÕES):
    
        filhos = recombinação(pop, N_FILHOS)
        pop = seleção(pop, filhos)  
    
    
        for k in range(TAM_POP):
            menor[i] = -np.max(F(pop['DNA'][k,:]))
            maior[i] = -np.min(F(pop['DNA'][k,:]))
            media[i] = -np.mean(F(pop['DNA'][k,:]))
    
        
    # plt.plot(media, label='Média') 
    # plt.plot(menor, label='Mínimo')
    # plt.plot(maior, label='Máximo')
    # plt.legend()   
    # plt.xlabel('Gerações')
    # plt.ylabel('Aptidão')
    # plt.grid()
    
    hist[ii] = min(maior)

plt.hist(hist)




 