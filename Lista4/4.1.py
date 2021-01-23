# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 09:56:52 2020

@author: Amanda
"""
#  ref: https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35


import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt

class Cidades:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distancia = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distancia
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    

class Fitness:
    def __init__(self, rota):
        self.rota = rota
        self.distancia = 0
        self.fitness= 0.0
    
    def routeDistance(self):
        if self.distancia ==0:
            pathDistancia = 0
            for i in range(0, len(self.rota)):
                fromCity = self.rota[i]
                toCity = None
                if i + 1 < len(self.rota):
                    toCity = self.rota[i + 1]
                else:
                    toCity = self.rota[0]
                pathDistancia += fromCity.distancia(toCity)
            self.distancia = pathDistancia
        return self.distancia
    
    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness

# Rota inicial aleatória 
def CriaçãoRota(Listacidades):
    rota = random.sample(Listacidades, len(Listacidades))
    return rota  
  
#População inicial
def PopulaçaoInicial(Tamanho_população, Listacidades):
    população = []

    for i in range(0, Tamanho_população):
        população.append(CriaçãoRota(Listacidades))
    return população

#Rank dos indivíduos
def rankRotas(população):
    aptidão = {}
    for i in range(0,len(população)):
        aptidão[i] = Fitness(população[i]).routeFitness()
    return sorted(aptidão.items(), key = operator.itemgetter(1), reverse = True)

#Seleção dos pais
def seleção(popRanked, taxaElit):
    selecionados = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    
    for i in range(0, taxaElit):
        selecionados.append(popRanked[i][0])
    for i in range(0, len(popRanked) - taxaElit):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]:
                selecionados.append(popRanked[i][0])
                break
    return selecionados

#Recombinação 
def matingPool(população, selecionados):
    matingpool = []
    for i in range(0, len(selecionados)):
        index = selecionados[i]
        matingpool.append(população[index])
    return matingpool

#Crossover: dois pais geram um filho
def Crossover(pai1, pai2):
    filho = []
    filho1 = []
    filho2 = []
    
    geneA = int(random.random() * len(pai1))
    geneB = int(random.random() * len(pai1))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        filho1.append(pai1[i])
        
    filho2 = [item for item in pai2 if item not in filho1]

    filho = filho1 + filho2
    return filho

#Aplicação do crossover em toda a população
def CrossoverPopulação(matingpool, taxaElit):
    filhos = []
    length = len(matingpool) - taxaElit
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0,taxaElit):
        filhos.append(matingpool[i])
    
    for i in range(0, length):
        filho = Crossover(pool[i], pool[len(matingpool)-i-1])
        filhos.append(filho)
    return filhos

#Mutação
def mutação(indivíduo, taxaMutação):
    for trocado in range(len(indivíduo)):
        if(random.random() < taxaMutação):
            trocar_com = int(random.random() * len(indivíduo))
            
            cidade1 = indivíduo[trocado]
            cidade2 = indivíduo[trocar_com]
            
            indivíduo[trocado] = cidade2
            indivíduo[trocar_com] = cidade1
    return indivíduo

#Aplicação da mutação em toda a população
def mutaçãoPop(população, taxaMutação):
    mutaçãoPop = []
    
    for ind in range(0, len(população)):
        mutatedInd = mutação(população[ind], taxaMutação)
        mutaçãoPop.append(mutatedInd)
    return mutaçãoPop

#Seleção dos sobreviventes
def prox_Geração(Ger_atual, taxaElit, taxaMutação):
    popRanked = rankRotas(Ger_atual)
    Resultados_selec = seleção(popRanked, taxaElit)
    matingpool = matingPool(Ger_atual, Resultados_selec)
    filho = CrossoverPopulação(matingpool, taxaElit)
    Prox_ger = mutaçãoPop(filho, taxaMutação)
    return Prox_ger

#Algoritmo genético principal
def geneticAlgorithm(população, Tamanho_população, taxaElit, taxaMutação, gerações):
    pop = PopulaçaoInicial(Tamanho_população, população)
    Progresso = []
    Progresso.append(1 / rankRotas(pop)[0][1])
    print("Distância Inicial: " + str(1 / rankRotas(pop)[0][1]))
    
    for i in range(0, gerações):
        pop = prox_Geração(pop, taxaElit, taxaMutação)
        Progresso.append(1 / rankRotas(pop)[0][1])
    
    plt.plot(Progresso)
    plt.ylabel('Distância')
    plt.xlabel('Gerações')
    plt.show()
    
    print("Distância Final: " + str(1 / rankRotas(pop)[0][1]))
    dist_final = 1 / rankRotas(pop)[0][1]
    melhorRotaIndex = rankRotas(pop)[0][0]
    melhorRota = pop[melhorRotaIndex]
    return melhorRota, dist_final

#Criação da lista de cidades
Listacidades = []

arq = open("dados.txt","r")
N_cidades =  int(arq.readline())  
     
NNO=np.zeros(N_cidades)
X=np.zeros(N_cidades)
Y=np.zeros(N_cidades)

i=0
k=0
for linha in arq:
    
    if i<N_cidades:
        
        valores = linha.split()
        NNO[i]=valores[0]
        X[i]=valores[1]
        Y[i]=valores[2]
        
        i= i + 1
    
arq.close()

cidade_x = X
cidade_y = Y
for i in range(0,N_cidades):
    # Listacidades.append(Cidades(x=(random.random() * N_cidades), y=(random.random() * N_cidades)))
    Listacidades.append(Cidades(x=cidade_x[i], y=cidade_y[i]))
    
#Execução do código
melhorRota, dist_final = geneticAlgorithm(população=Listacidades, Tamanho_população=30, taxaElit=20, taxaMutação=0.01, gerações=200)
print(melhorRota)
lista = list(melhorRota)

## Imagem melhor rota
x = np.zeros(N_cidades+1)
y=  np.zeros(N_cidades+1)
 
for i in range(N_cidades):
    x[i] = lista[i].x
    y[i] = lista[i].y
    
x[N_cidades] = lista[0].x
y[N_cidades] = lista[0].y
plt.figure(figsize=(12, 8))
plt.scatter(x=x[:], y=y[:], s=1000, zorder=1)
for i in range(N_cidades):
    plt.text(x[i], y[i], str(i), horizontalalignment='center', verticalalignment='center', size=16,
             c='white')
plt.plot(x,y, 'k',zorder=0)
plt.title(f'{N_cidades} cidades com distância {dist_final:.2f}', size=16)
    
    
    
    