import random


# Setting Parameters
N = 3           # N*N puzzle
PS = 100        # Population Size
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
