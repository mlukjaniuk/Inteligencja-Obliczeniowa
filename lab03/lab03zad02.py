import numpy as np
import pygad
import time


# labirynt ze ścianami: 1 - ściana, 0 - puste pole

#labirynt 12x12

maze = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])


# pozycja startowa
start = (1, 1)

# pozycja końcowa
end = (maze.shape[0] - 2, maze.shape[1] - 2)

#maksymalna liczba ruchów
max_moves = 30

gene_space = np.array([0, 1, 2, 3])
sol_per_pop = 500
num_genes = max_moves
num_parents_mating = 100
num_generations = 100
keep_parents = 20
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 7


def fitness(solution, solution_idx):
    fitness = 0
    #pozycja startowa
    position = start
    #liczba ruchów
    moves = 0
    for gene in solution:
        # kara za wejście na ścianę
        if maze[position] == 1:
            fitness *= 3
        elif position == end:
            fitness += 10
            return fitness
        # kara za cofanie się
        elif gene == 0 and moves > 0 and solution[moves - 1] == 2:
            fitness -= 1
        elif gene == 1 and moves > 0 and solution[moves - 1] == 3:
            fitness -= 1
        elif gene == 2 and moves > 0 and solution[moves - 1] == 0:
            fitness -= 1
        elif gene == 3 and moves > 0 and solution[moves - 1] == 1:
            fitness -= 1
        # ruch w prawo
        elif gene == 1:
            position = (position[0], position[1] + 1)
        # ruch w lewo
        elif gene == 3:
            position = (position[0], position[1] - 1)
        # ruch w dół
        elif gene == 2:
            position = (position[0] + 1, position[1])
        # ruch w górę
        elif gene == 0:
            position = (position[0] - 1, position[1])
        moves += 1

    return -abs(position[0] - end[0]) - abs(position[1] - end[1]) + fitness
    
    


# inicjalizacja algorytmu genetycznego
ga_instance = pygad.GA(gene_space=gene_space,
                        num_generations=num_generations,
                        num_parents_mating=num_parents_mating,
                        fitness_func=fitness,
                        sol_per_pop=sol_per_pop,
                        num_genes=num_genes,
                        parent_selection_type=parent_selection_type,
                        keep_parents=keep_parents,
                        crossover_type=crossover_type,
                        mutation_type=mutation_type,
                        mutation_percent_genes=mutation_percent_genes)

# Pojedyncze uruchomienie algorytmu
ga_instance.run()

# najlepsze rozwiązanie
solution, solution_fitness, solution_idx = ga_instance.best_solution()

print("Najlepsze rozwiązanie: {solution}".format(solution=solution))
#Fitness powinno być jak najmniejsze
print("Najlepsza wartość funkcji fitness: {solution_fitness}".format(solution_fitness=solution_fitness))

# rysowanie wykresu
ga_instance.plot_fitness()

# Zadanie 2:
# Mierzenie średniego czasu działania algorytmu

# czasy = []
# for i in range(10):
#     start_time = time.time()
#     ga_instance.run()
#     czasy.append(time.time() - start_time)

# print("Średni czas działania algorytmu: {czas}".format(czas=sum(czasy)/len(czasy)))
# print(czasy)








