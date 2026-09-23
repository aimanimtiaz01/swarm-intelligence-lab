"""
# SWARM INTELLIGENCE LAB
## Lab 03: Particle Swarm Optimization
**Name**: Aiman Imtiaz Ranjha
**Program**: BS(AI)-7
**Instructor**: Sir Ahsan Javed
"""


import random
# fixing the randomness to my roll number (58) so the results stay the same every time i run it
random.seed(58)

def f(x):
  return (x - 7) **2 + 4    # the function we're minimizing

# initializing the 5 particles and giving them a range (0 to 14) letting Python decide exactly where to randomly place them within this range
positions = [random.uniform(0, 14) for _ in range(5)]

velocities = [0 for _ in range(5)] # all particles start with zero speed

# making a proper copy of initial positions. if i don't use [:] it will just reference the original list and mess up past memory
pbest_pos = positions[:]

# taking the best personal best (pbest) from all the
# particles and setting it as the new global best (gbest) for the next iteration
gbest_pos = min(pbest_pos, key=f)

# inertia, personal pull, swarm pull
W, C1, C2 = 0.6, 1.5, 1
# W keeps the particle moving in its current direction
# C1 pulls particle towards its own best memory
# C2 pulls it towards the swarm's best spot

iterations = 40

for it in range(iterations):
    for i in range(5):
        r1,r2 = random.random(), random.random()

        #Calculate new velocity by combining old momentum, personal best pull and global best pull
        velocities[i]= W*velocities[i] + C1*r1*(pbest_pos[i]-positions[i]) + C2*r2*(gbest_pos-positions[i])

       # updating the particle's current position by adding the newly calculated velocity
        positions[i]= positions[i] + velocities[i]

        # checking if the function value at this new position is lower (better) than its historical personal best
        if f(positions[i]) < f(pbest_pos[i]):
            pbest_pos[i] = positions[i]

    # Update global best after all particles have moved for this iteration
    gbest_pos = min(pbest_pos, key=f)

# the final x coordinate where the swarm decided to settle down
print("Swarm converged near x=",gbest_pos)


# %% [markdown]
"""
### Parameter Testing & Comparison

**Inertia (w) Test:** When I changed w = 0.2, the particles lost momentum fast and settled down very accurately converging at x = 6.99999998. When I tried w = 0.9 the extra momentum caused them to bounce around more before settling which resulted in a slightly less precise convergence at x = 6.99744152.

**Pull Strengths (c1, c2) Test:** With c1 = c2 = 0.5, the swarm drifted more weakly but still managed to find a highly accurate minimum at x = 6.99999402. But when I bumped it up to c1 = c2 = 3 the strong pull caused the particles to jump aggressively across the space resulting in a slightly rougher convergence at x = 6.98153279. Overall, the swarm always found the minimum near x=7 but extreme values slightly reduced the final precision.
"""