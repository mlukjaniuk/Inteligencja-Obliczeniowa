from graph import *
import pygad
from mvc_checker import *
import matplotlib.pyplot as plt
import numpy as np


def fitness_function(graph):
    def fitness(solution, solution_idx):
        fitness = 0
        es = set()

        for i in graph.nodes:
            if solution[i] != 0:
                for j in graph.edges[i]:
                    if i < j:
                        es.add((i, j))
                    else:
                        es.add((j, i))
                    if solution[j] != 0:
                        fitness -= 10
        
        diff = graph.edges_set - es
        fitness -= len(diff)*100

        return fitness
    return fitness

def run_small_ga_instance(graph, n):
    ga_instance = pygad.GA(gene_space=[0, 1],
                        num_generations=300,
                        num_parents_mating=50,
                        fitness_func=fitness_function(graph),
                        sol_per_pop=300,
                        num_genes=n,
                        parent_selection_type='sss',
                        keep_parents=4,
                        crossover_type="single_point",
                        mutation_type="random",
                        mutation_percent_genes=20)
    
    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print("Najlepsze rozwiązanie: {solution}".format(solution=solution))
    print("Minimum vertex cover size: {solution_ones}".format(solution_ones=np.count_nonzero(solution)))
    print("Najlepsza wartość funkcji fitness: {solution_fitness}".format(solution_fitness=solution_fitness))
    ga_instance.plot_fitness()
    graph.plot_all_edges()
    graph.plot_all_nodes()
    graph.plot_covered_nodes(solution)
    graph.plot_covered_edges(solution)
    plt.show()
    return np.count_nonzero(solution)


def run_medium_ga_instance(graph, n):
    ga_instance = pygad.GA(gene_space=[0, 1],
                        num_generations=500,
                        num_parents_mating=200,
                        fitness_func=fitness_function(graph),
                        sol_per_pop=600,
                        num_genes=n,
                        parent_selection_type='sss',
                        keep_parents=20,
                        crossover_type="single_point",
                        mutation_type="random",
                        mutation_percent_genes=15)
    
    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    # print("Najlepsze rozwiązanie ga: {solution}".format(solution=solution))
    # print("Minimum vertex cover size ga: {solution_ones}".format(solution_ones=np.count_nonzero(solution)))
    # print("Najlepsza wartość funkcji fitness: {solution_fitness}".format(solution_fitness=solution_fitness))
    # ga_instance.plot_fitness()
    # graph.plot_all_edges()
    # graph.plot_all_nodes()
    # graph.plot_covered_nodes(solution)
    # graph.plot_covered_edges(solution)
    # plt.show()
    return np.count_nonzero(solution)

def run_large_ga_instance(graph, n):
    ga_instance = pygad.GA(gene_space=[0, 1],
                        num_generations=700,
                        num_parents_mating=300,
                        fitness_func=fitness_function(graph),
                        sol_per_pop=600,
                        num_genes=n,
                        parent_selection_type='sss',
                        keep_parents=40,
                        crossover_type="single_point",
                        mutation_type="random",
                        mutation_percent_genes=15)
    
    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    # print("Najlepsze rozwiązanie ga: {solution}".format(solution=solution))
    # print("Minimum vertex cover size ga: {solution_ones}".format(solution_ones=np.count_nonzero(solution)))
    # print("Najlepsza wartość funkcji fitness: {solution_fitness}".format(solution_fitness=solution_fitness))
    # ga_instance.plot_fitness()
    # graph.plot_all_edges()
    # graph.plot_all_nodes()
    # graph.plot_covered_nodes(solution)
    # graph.plot_covered_edges(solution)
    # plt.show()
    return np.count_nonzero(solution)





