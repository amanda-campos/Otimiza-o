#https://github.com/MorvanZhou/Evolutionary-Algorithm


import numpy as np
import matplotlib.pyplot as plt
import math 
BITS = 16            #tamanho do cromossomo 
POPULAÇÃO = 30           # tamanho da população
TAXA_CROSS = 0.8         # probabilidade de crossover
TAXA_MUTAÇÃO = 0.003   #probabilidade de mutação
N_GENERAÇÕES = 50
X_LIMITES = [-2,2]         #limites de x


def F(x): return -(x**2-0.3*np.cos(10*x*math.pi))    #máximo da função


# encontra as fitness diferentes de zero para seleção
def get_fitness(pred): return pred + 1e-3 - np.min(pred)


# conversão binário para decimal normalizado no limite de X
def codificação(pop): return pop.dot(2 ** np.arange(BITS)[::-1]) / float(2**BITS-1) * X_LIMITES[1]


def seleção(pop, fitness):    # SELEÇÃO
    idx = np.random.choice(np.arange(POPULAÇÃO), size=POPULAÇÃO, replace=True,
                           p=fitness/fitness.sum())
    return pop[idx]


def crossover(pai, pop):     #CROSSOVER
    if np.random.rand() < TAXA_CROSS:
        i_ = np.random.randint(0, POPULAÇÃO, size=1)                             # seleciona outro indivíduo da população
        cross_points = np.random.randint(0, 2, size=BITS).astype(np.bool)   # pontos do crossover
        pai[cross_points] = pop[i_, cross_points]                            # produz 1 filho
    return pai


def mutação(filho): # inversão de 1 bit
    for point in range(BITS):
        if np.random.rand() < TAXA_MUTAÇÃO:
            filho[point] = 1 if filho[point] == 0 else 0
    return filho


pop = np.random.randint(2, size=(POPULAÇÃO, BITS))   #População inicial

i = 0
menor = np.zeros([N_GENERAÇÕES])
media = np.zeros([N_GENERAÇÕES])

for _ in range(N_GENERAÇÕES):

    F_values = F(codificação(pop))
    fitness = get_fitness(F_values)
    pop = seleção(pop, fitness)
    pop_copy = pop.copy()
    for pai in pop:
        filho = crossover(pai, pop_copy)
        filho = mutação(filho)
        pai[:] = filho       # pai é substituído por seu filho
    menor[i] = -np.max(F_values)
    media[i] = -np.mean(F_values)
    i = i + 1
    
plt.plot(media, label='Média') 
plt.plot(menor, label='Mínimo')
plt.legend()   
plt.xlabel('Gerações')
plt.ylabel('Fitness')
plt.grid()

print ('Média:', -np.mean(F_values))
print ('Menor:', -np.max(F_values))