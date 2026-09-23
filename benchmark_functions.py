# %% [markdown]
"""
# SWARM INTELLIGENCE LAB
## Lab 01: Benchmark Functions & Random Search
**Name**: Aiman Imtiaz Ranjha
**Program**: BS(AI)-7
**Instructor**: Sir Ahsan Javed
"""

# %% [markdown]
"""
### 1. Sphere Function
"""

# %%
import numpy as np
import matplotlib.pyplot as plt

def sphere(x, y):
  return x**2 + y**2

x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)
Z = sphere(X, Y)
plt.contourf(X, Y, Z, levels=30, cmap='viridis')
plt.colorbar(label='f(x, y)')
plt.title('Sphere Function Landscape')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



# %% [markdown]
"""
### 2. Rastrigin Function
"""

# %%
def rastrigin(x, y):
    A = 10
    return 2*A + (x**2 - A*np.cos(2*np.pi*x)) + (y**2 - A*np.cos(2*np.pi*y))

x = np.linspace(-5.12, 5.12, 200)
y = np.linspace(-5.12, 5.12, 200)
X, Y = np.meshgrid(x, y)
Z = rastrigin(X, Y)
plt.contourf(X, Y, Z, levels=30, cmap='viridis')
plt.colorbar(label='f(x, y)')
plt.title('Rastrigin Function Landscape')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# %% [markdown]
"""
### 3. Ackley Function
"""

# %%
def ackley(x, y):
  return (-20*np.exp(-0.2*np.sqrt(0.5*(x**2+y**2))) - np.exp(0.5*(np.cos(2*np.pi*x) + np.cos(2*np.pi*y))) + np.e + 20)

x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)
Z = ackley(X, Y)
plt.contourf(X, Y, Z, levels=30, cmap='viridis')
plt.colorbar(label='f(x, y)')
plt.title('Ackley Function Landscape')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



# %% [markdown]
"""
### 4. Ackley Function: Standard Domain Values
"""

# %%

x = np.linspace(-32.768, 32.768, 200)
y = np.linspace(-32.768, 32.768, 200)

X, Y = np.meshgrid(x, y)
Z = ackley(X, Y)

plt.contourf(X, Y, Z, levels=30, cmap='viridis')
plt.colorbar(label='f(x, y)')
plt.title('Ackley Function with Standard Domain')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



# %% [markdown]
"""
### 5. Random Search Algorithm
"""

# %%
import random
def random_search(func, bounds, iterations=1000):
  best_point = None
  best_score = float('inf')
  for i in range(iterations):
      x = random.uniform(bounds[0], bounds[1])
      y = random.uniform(bounds[0], bounds[1])
      score = func(x, y)
      if score < best_score:
          best_score = score
          best_point = (x, y)
  return best_point, best_score



# %% [markdown]
"""
### 6. Random Search on Each Function
"""

# %%
print("RANDOM SEARCH RESULTS")

best_point, best_score = random_search(sphere, (-5, 5))
print("\nSphere -> Best point:", best_point)
print("Sphere -> Best score:", best_score)

best_point, best_score = random_search(rastrigin, (-5.12, 5.12))
print("\nRastrigin -> Best point:", best_point)
print("Rastrigin -> Best score:", best_score)


best_point, best_score = random_search(ackley, (-5, 5))
print("\nAckley -> Best point:", best_point)
print("Ackley -> Best score:", best_score)

best_point, best_score = random_search(ackley, (-32.768, 32.768))
print("\nAckley (Standard Domain) -> Best point:", best_point)
print("Ackley (Standard Domain) -> Best score:", best_score)

# %% [markdown]
"""
### 7. Observations & Analysis

**1. Which function did Random Search solve best? Why do you think that happened, based on its landscape shape?**
Random Search solved Sphere the best with a score of 0.004. The Sphere function has a single smooth bowl shape that slopes gradually toward the center at (0,0). When Random Search generates random points many of them naturally fall closer to the minimum simply because the landscape is so uniform and symmetrical. There are no false pockets to trap the algorithm so even random guessing works reasonably well.

**2. Which function did Random Search struggle with the most? What about its landscape made it difficult?**
Random Search struggled most with Rastrigin achieving a score of 1.40. Rastrigin's landscape has many small deceptive pockets spread across the entire space. When Random Search finds one of these local minima it has no way to know whether it is the true best point or just a false pocket. Since Random Search has no strategy to continue exploring beyond a decent solution, it stops and reports a poor result.

**3. If you increased iterations from 1000 to 10,000, do you expect the results to improve? For which function would the improvement matter least, and why?**
Yes, results would improve overall but the improvement would matter least for Sphere. Sphere already achieved 0.004 at 1000 iterations which is very close to optimal. Increasing iterations would help Rastrigin and Ackley more because they have many local minima that need more attempts to explore. Sphere's simple smooth shape means it already performs nearly as well as it can with fewer iterations.

**4. In your own words, what is the main weakness of Random Search as a strategy?**
Random Search has no memory and no learning. It treats every random point as a fresh start and never uses information from previous attempts to guide the next one. On Rastrigin (1.40) and Ackley (0.186) this becomes a serious problem because the algorithm wastes attempts on bad regions and cannot build on successes. A smarter algorithm would remember where it found good solutions and explore nearby areas more thoroughly.
"""