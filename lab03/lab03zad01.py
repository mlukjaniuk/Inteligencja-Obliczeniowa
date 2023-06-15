import random
import math
import pygad
import matplotlib.pyplot as plt

def endurance(x, y, z, u, v, w):
    return math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w)

gene_space = [random.uniform(0, 1) for _ in range(6)]

def fitness_func(solution, solution_idx):
    x, y, z, u, v, w = solution
    fitness = endurance(x, y, z, u, v, w)
    return fitness

num_generations = 50 # Liczba pokoleń
sol_per_pop = 100 # Liczba osobników w populacji
mutation_percent_genes = 17 # Procent mutacji genów
num_genes = 6 # Liczba genów w chromosomie

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=24,
                       fitness_func=fitness_func,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       gene_space=gene_space,
                       mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Najlepsza wytrzymałość: {:.4f}".format(solution_fitness))
print("Najlepszy chromosom: {}".format(solution))

plt.plot(ga_instance.best_solutions_fitness)
plt.title("Wartość funkcji fitness w kolejnych pokoleniach")
plt.xlabel("Numer pokolenia")
plt.ylabel("Wartość funkcji fitness")
plt.show()
