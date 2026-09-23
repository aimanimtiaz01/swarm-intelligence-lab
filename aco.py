"""
# SWARM INTELLIGENCE LAB
## Lab 02: Ant Colony Optimization
**Name**: Aiman Imtiaz Ranjha
**Program**: BS(AI)-7
**Instructor**: Sir Ahsan Javed
"""
import random

random.seed(58)
paths = {'Path A': 10, 'Path B': 15, 'Path C': 8, 'Path D': 12}

pheromone = {p: 1.0 for p in paths}

evaporation_rate = 0.5
Q = 100
iterations = 50
ants_per_iteration = 10  

for it in range(iterations):
    for ant in range(ants_per_iteration):
        total = sum(pheromone.values())
        weights = [pheromone[p] / total for p in paths]

        chosen = random.choices(list(paths.keys()), weights=weights)[0]

        pheromone[chosen] += Q / paths[chosen]

    for p in pheromone:
        pheromone[p] = pheromone[p] * (1 - evaporation_rate)

best = max(pheromone, key=pheromone.get)

print("Colony converged on:", best)