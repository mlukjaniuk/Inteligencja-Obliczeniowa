import pygad
import numpy

prices = [100, 300, 200, 40, 500, 70, 100, 250, 300, 280, 300]
weights = [7, 7, 6, 2, 5, 6, 1, 3, 10, 3, 15]
things = ["zegar", "obraz-pejzaż", "obraz-portret", "radio", "laptop", "lampka nocna", "srebrne sztućce", "porcelana", "figurka z brązu", "skórzana torebka", "odkurzacz"]


#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1
gene_space = [0, 1]

#definiujemy funkcję fitness dla problemu plecakowego
def fitness_function(solution, solution_idx):
    #obliczamy wagę plecaka
    weight = numpy.sum(solution * weights)
    #obliczamy cenę plecaka
    price = numpy.sum(solution * prices)
    #jeśli waga jest większa niż 25, to ocena jest 0
    if weight > 25:
        price = 0
    #zwracamy ocenę
    return price


#ile chromosomów w populacji
sol_per_pop = 10
#ile genów w chromosomie
num_genes = len(weights)

#ile wyłaniamy rodziców do krzyżowania
num_parents_mating = 5
num_generations = 10
keep_parents = 2

#jaki typ selekcji rodziców
parent_selection_type = "sss"

#w ilu punktach krzyżujemy
crossover_type = "single_point"

#mutacja na ilu procentach genów
mutation_type = "random"

mutation_percent_genes = 10


#inicjacja algorytmu z powyższymi parametrami
ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function, 
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)
                    

num_of_gen = 0
last_fitness = 0
while True:
    ga_instance.run()
    num_of_gen += 1
    if ga_instance.best_solution()[1] == last_fitness:
        break
    last_fitness = ga_instance.best_solution()[1]


# podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Najlepsze rozwiazanie : {solution}".format(solution=solution))
print("Wybrane przedmioty: {solution}".format(solution=numpy.array(things)[solution == 1]))
print("Ocena najlepszego rozwiazania : {solution_fitness}".format(solution_fitness=solution_fitness))
print("Do najlepszego rozwiazania potrzeba {num_of_gen} pokoleń".format(num_of_gen=num_of_gen))

