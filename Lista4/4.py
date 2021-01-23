# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:34:42 2020

@author: Amanda
"""
import numpy as np
from abc import ABC, abstractmethod


class Individual(ABC):
    def __init__(self, value=None, init_params=None):
        if value is not None:
            self.value = value
        else:
            self.value = self._random_init(init_params)

    @abstractmethod
    def pair(self, other, pair_params):
        pass

    @abstractmethod
    def mutate(self, mutate_params):
        pass

    @abstractmethod
    def _random_init(self, init_params):
        pass


class Optimization(Individual):
    def pair(self, other, pair_params):
        return Optimization(pair_params['alpha'] * self.value + (1 - pair_params['alpha']) * other.value)

    def mutate(self, mutate_params):
        self.value += np.random.normal(0, mutate_params['rate'], mutate_params['dim'])
        for i in range(len(self.value)):
            if self.value[i] < mutate_params['lower_bound']:
                self.value[i] = mutate_params['lower_bound']
            elif self.value[i] > mutate_params['upper_bound']:
                self.value[i] = mutate_params['upper_bound']

    def _random_init(self, init_params):
        return np.random.uniform(init_params['lower_bound'], init_params['upper_bound'], init_params['dim'])


class TSP(Individual):
    def pair(self, other, pair_params):
        self_head = self.value[:int(len(self.value) * pair_params['alpha'])].copy()
        self_tail = self.value[int(len(self.value) * pair_params['alpha']):].copy()
        other_tail = other.value[int(len(other.value) * pair_params['alpha']):].copy()

        mapping = {other_tail[i]: self_tail[i] for i in range(len(self_tail))}

        for i in range(len(self_head)):
            while self_head[i] in other_tail:
                self_head[i] = mapping[self_head[i]]

        return TSP(np.hstack([self_head, other_tail]))

    def mutate(self, mutate_params):
        for _ in range(mutate_params['rate']):
            i, j = np.random.choice(range(len(self.value)), 2, replace=False)
            self.value[i], self.value[j] = self.value[j], self.value[i]

    def _random_init(self, init_params):
        return np.random.choice(range(init_params['n_cities']), init_params['n_cities'], replace=False)


class Population:
    def __init__(self, size, fitness, individual_class, init_params):
        self.fitness = fitness
        self.individuals = [individual_class(init_params=init_params) for _ in range(size)]
        self.individuals.sort(key=lambda x: self.fitness(x))

    def replace(self, new_individuals):
        size = len(self.individuals)
        self.individuals.extend(new_individuals)
        self.individuals.sort(key=lambda x: self.fitness(x))
        self.individuals = self.individuals[-size:]

    def get_parents(self, n_offsprings):
        mothers = self.individuals[-2 * n_offsprings::2]
        fathers = self.individuals[-2 * n_offsprings + 1::2]

        return mothers, fathers


class Evolution:
    def __init__(self, pool_size, fitness, individual_class, n_offsprings, pair_params, mutate_params, init_params):
        self.pair_params = pair_params
        self.mutate_params = mutate_params
        self.pool = Population(pool_size, fitness, individual_class, init_params)
        self.n_offsprings = n_offsprings

    def step(self):
        mothers, fathers = self.pool.get_parents(self.n_offsprings)
        offsprings = []

        for mother, father in zip(mothers, fathers):
            offspring = mother.pair(father, self.pair_params)
            offspring.mutate(self.mutate_params)
            offsprings.append(offspring)

        self.pool.replace(offsprings)
        


def fitness(opt):
    return -opt.value[0] * (opt.value[0] - 1) * (opt.value[0] - 2) * (opt.value[0] - 3) * (opt.value[0] - 4)


evo = Evolution(
    pool_size=10, fitness=fitness, individual_class=Optimization, n_offsprings=3,
    pair_params={'alpha': 0.5},
    mutate_params={'lower_bound': 0, 'upper_bound': 4, 'rate': 0.25, 'dim': 1},
    init_params={'lower_bound': 0, 'upper_bound': 4, 'dim': 1}
)
n_epochs = 50

for i in range(n_epochs):
    evo.step()

print(evo.pool.individuals[-1].value)

import matplotlib.pyplot as plt


def tsp_fitness_creator(cities):
    matrix = []
    for city in cities:
        row = []
        for city_ in cities:
            row.append(np.linalg.norm(city - city_))
        matrix.append(row)
    distances = np.array(matrix)

    def fitness(tsp):
        res = 0
        for i in range(len(tsp.value)):
            res += distances[tsp.value[i], tsp.value[(i + 1) % len(tsp.value)]]
        return -res

    return fitness


def compute_distances(cities):
    distances = []
    for from_city in cities:
        row = []
        for to_city in cities:
            row.append(np.linalg.norm(from_city - to_city))
        distances.append(row)
    return np.array(distances)


def route_length(distances, route):
    length = 0
    for i in range(len(route)):
        length += distances[route[i], route[(i + 1) % len(route)]]
    return length


def plot_route(cities, route, distances):
    length = route_length(distances, route)

    plt.figure(figsize=(12, 8))
    plt.scatter(x=cities[:, 0], y=cities[:, 1], s=1000, zorder=1)
    for i in range(len(cities)):
        plt.text(cities[i][0], cities[i][1], str(i), horizontalalignment='center', verticalalignment='center', size=16,
                 c='white')
    for i in range(len(route)):
        plt.plot([cities[route[i]][0], cities[route[(i + 1) % len(route)]][0]],
                 [cities[route[i]][1], cities[route[(i + 1) % len(route)]][1]], 'k', zorder=0)
    if len(route)>0:
        plt.title(f'Visiting {len(route)} cities in length {length:.2f}', size=16)
    else:
        plt.title(f'{len(cities)} cities', size=16)
    plt.show()


cities = np.array([[35, 51],
                   [113, 213],
                   [82, 280],
                   [322, 340],
                   [256, 352],
                   [160, 24],
                   [322, 145],
                   [12, 349],
                   [282, 20],
                   [241, 8],
                   [398, 153],
                   [182, 305],
                   [153, 257],
                   [275, 190],
                   [242, 75],
                   [19, 229],
                   [303, 352],
                   [39, 309],
                   [383, 79],
                   [226, 343]])

fitness = tsp_fitness_creator(cities)
distances = compute_distances(cities)

evo = Evolution(
    pool_size=100, fitness=fitness, individual_class=TSP, n_offsprings=30,
    pair_params={'alpha': 0.5},
    mutate_params={'rate': 1},
    init_params={'n_cities': 20}
)
n_epochs = 1000

hist = []
for i in range(n_epochs):
    hist.append(evo.pool.fitness(evo.pool.individuals[-1]))
    evo.step()

plt.plot(hist)
plt.show()

plot_route(cities, route=evo.pool.individuals[-1].value, distances=distances)