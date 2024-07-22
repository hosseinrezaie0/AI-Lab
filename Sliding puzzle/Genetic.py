import random


# Setting Parameters
N = 3           # N*N puzzle
PS = 10        # Population Size
MR = 0.8        # Mutation Rate

# Create initial population
def init_population(N, PS):
    population = []
    for i in range(PS):
        member = []
        for i in range(1,N*N):
            member = random.sample(range(1, N*N), N*N-1)
        population.append(member + [None])              # None is for fitness evaluation
    return population


# Cross over
def cross_over(population, N, PS):
    for i in range(0,PS,2):
        child1 = population[i][:N*N//2] + population[i+1][N*N//2:]
        child2 = population[i+1][:N*N//2] + population[i][N*N//2:]
        population.append(child1)
        population.append(child2)
    return population 
