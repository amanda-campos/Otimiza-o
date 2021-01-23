# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 17:59:19 2020

@author: Amanda
"""


#initialize population
import random
best=-100000

bits = 10
cromossomos = 4
populations =([[random.randint(0,1) for x in range(bits)] for i in range(cromossomos)])
print(type(populations))
parents=[]
new_populations = []
print(populations)


#fitness score calculation ............
def fitness_score() :
    global populations,best
    fit_value = []

    for i in range(cromossomos) :
        chromosome_value=0
        
        for j in range(bits-1,0,-1) :
            chromosome_value += populations[i][j]*(2**(bits-1-j))
        chromosome_value = -1*chromosome_value if populations[i][0]==1 else chromosome_value
        print(chromosome_value)
        fit_value.append(-(chromosome_value**2) + 5 )
    print(fit_value)
    fit_value, populations = zip(*sorted(zip(fit_value, populations) , reverse = True))
    best= fit_value[0]
    
fitness_score()

#print(type(populations))
#selecting parents....
def selectparent():
    global parents
    #global populations , parents
    parents=populations[0:2]
    print(type(parents))
    print(parents)
selectparent()

#single-point crossover .........

def crossover() :
    global parents
    
    cross_point = random.randint(0,bits-1)
    parents = parents + tuple([(parents[0][0:cross_point +1] +parents[1][cross_point+1:bits])])
    parents = parents + tuple([(parents[1][0:cross_point +1] +parents[0][cross_point+1:bits])])
    
    print(parents)
    

crossover()

def mutation() :
    global populations, parents
    mute = random.randint(0,49)
    if mute == 20 :
        x=random.randint(0,cromossomos-1)
        y = random.randint(0,bits-1)
        parents[x][y] = 1-parents[x][y]
    populations = parents
    print(populations)
mutation()

for i in range(1000) :
    fitness_score()
    selectparent() 
    crossover()
    mutation()
print("best score :")
print(best)
print("sequence........")
print(populations[0])
    