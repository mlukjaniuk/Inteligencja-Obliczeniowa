from graph import *
from ga import *
from ants import *
from mvc_checker import *
import time
import tabulate


small_n = 6

#small input 1
graph_6_1 = Graph()
graph_6_1.create_nodes(small_n)
graph_6_1.create_edges([[1, 2, 3, 4, 5], [0, 2], [0, 1], [0], [0], [0]])
graph_6_1.create_coords([[50, 50], [40, 40], [50, 35], [70, 60], [75, 45], [65, 30]])
graph_6_1.create_edges_set()
min_cover_6_1 = 2


#small input 2
graph_6_2 = Graph()
graph_6_2.create_nodes(small_n)
graph_6_2.create_edges([[1, 2, 3], [0, 2], [0, 1, 4], [0, 4, 5], [2, 3], [3]])
graph_6_2.create_coords([[40, 50], [25, 35], [40, 20], [70, 50], [70, 20], [95, 50]])
graph_6_2.create_edges_set()
min_cover_6_2 = 3

#small input 3
graph_6_3 = Graph()
graph_6_3.create_nodes(small_n)
graph_6_3.create_edges([[1, 4, 5], [0, 2, 3], [1, 3], [1, 2, 4], [0, 3, 5], [0, 4]])
graph_6_3.create_coords([[20, 80], [40, 80], [50, 50], [40, 10], [20, 10], [10, 50]])
graph_6_3.create_edges_set()
min_cover_6_3 = 4


# print(findMinCover(graph_6_3))
# run_small_ga_instance(graph_6_3, small_n
# print(run_ant_colony(graph_6_3))


medium_n = 13

#medium input 1
graph_13_1 = Graph()
graph_13_1.create_nodes(medium_n)
graph_13_1.create_edges([[11], [4, 12, 5, 7], [10, 6, 12], [9], [1, 9, 5, 9], [4, 1, 6, 9], [5, 2, 10], [1, 10], [9], [3, 4, 8, 4, 5, 11], [2, 7, 6], [0, 9], [1, 2]])
graph_13_1.create_coords([[47, 7], [15, 54], [81, 61], [40, 22], [90, 9], [90, 93], [46, 51], [78, 96], [88, 40], [15, 46], [72, 36], [71, 37], [2, 70]])
graph_13_1.create_edges_set()
min_cover_13_1 = 6

#medium input 2
graph_13_2 = Graph()
graph_13_2.create_nodes(medium_n)
graph_13_2.create_edges([[1], [0, 6, 7], [9, 6, 4, 5], [6, 8], [5, 2, 11], [4, 2, 9, 9], [1, 2, 3, 12, 12, 12], [1, 11], [3, 11, 12], [2, 5, 5], [12, 12], [8, 7, 4], [6, 6, 10, 10, 8, 6]])
graph_13_2.create_coords([[71, 36], [21, 39], [37, 71], [12, 30], [66, 0], [50, 6], [1, 64], [68, 57], [62, 60], [85, 24], [82, 30], [59, 82], [16, 100]])
min_cover_13_2 = 10

# print("Minimum vertex cover:", findMinCover(graph_13_1))
run_medium_ga_instance(graph_13_1, medium_n)
# run_ant_colony(graph_13_1)

#medium input 3
graph_13_3 = Graph()
graph_13_3.create_nodes(medium_n)
graph_13_3.create_edges([[5, 6, 7], [5, 7, 2], [1], [12, 4, 4, 5, 10, 12], [3, 6, 3], [0, 1, 3, 7], [4, 0, 7], [1, 5, 6, 0, 9], [10, 11, 11], [7], [8, 3], [8, 8], [3, 3]])
graph_13_3.create_coords([[5, 70], [23, 17], [35, 92], [48, 23], [7, 37], [70, 21], [78, 62], [7, 45], [18, 61], [85, 40], [99, 72], [12, 47], [36, 94]])
min_cover_13_3 = 10

#large input 1
graph_30_1 = Graph()
graph_30_1.create_nodes(30)
graph_30_1.create_edges([[19, 18, 15], [12, 22], [10, 11, 16, 17], [27, 27], [8], [20], [9], [9, 15, 26], [4, 25], [7, 16, 26, 13, 26, 6], [2, 20], [2, 17], [1, 26, 29, 29], [9], [19, 20, 24], [7, 0], [9, 2, 25, 23], [11, 2], [0, 27, 23, 24], [0, 14, 23], [5, 10, 14, 27], [29, 22], [1, 21], [18, 19, 16, 27], [18, 14], [8, 16, 28], [9, 12, 7, 9], [3, 3, 18, 20, 23], [25, 29], [21, 28, 12, 12]])
graph_30_1.create_coords([[40, 76], [81, 31], [76, 85], [82, 74], [50, 23], [79, 93], [5, 90], [34, 75], [94, 70], [78, 65], [8, 96], [58, 4], [55, 51], [98, 84], [33, 15], [83, 37], [9, 99], [47, 2], [57, 34], [18, 85], [65, 24], [46, 64], [41, 23], [69, 26], [38, 39], [65, 11], [94, 13], [84, 36], [93, 13], [31, 21]])
min_cover_30_1 = 20

# run_large_ga_instance(graph_30_1, 30)
# run_ant_colony(graph_30_1)

#large input 2
graph_30_2 = Graph()
graph_30_2.create_nodes(30)
graph_30_2.create_edges([[5, 13], [12, 11, 6], [15, 28, 5], [17, 5, 7], [29, 9, 19, 25, 28], [0, 3, 2, 6], [1, 5], [3, 28, 23], [13, 28, 15], [4, 24], [22, 15], [1, 23, 15, 28], [1, 28], [0, 8, 28, 22], [15, 28], [2, 10, 11, 14, 8, 26], [27, 24], [3, 23], [27, 20], [4, 24], [18, 22, 22], [24, 27], [10, 20, 20, 13, 29], [11, 17, 7, 27], [16, 21, 9, 19], [4], [15], [16, 18, 23, 21], [2, 7, 8, 12, 13, 14, 11, 4], [4, 22]])
graph_30_2.create_coords([[77, 76], [99, 52], [60, 27], [78, 14], [97, 27], [64, 75], [19, 7], [62, 9], [32, 98], [46, 55], [76, 51], [32, 68], [41, 90], [66, 35], [92, 39], [24, 23], [34, 1], [94, 30], [19, 13], [41, 60], [24, 3], [28, 49], [79, 10], [31, 96], [54, 89], [92, 19], [34, 49], [54, 88], [62, 5], [72, 49]])
min_cover_30_2 = 22

# run_large_ga_instance(graph_30_2, 30)
# run_ant_colony(graph_30_2)

#large input 3
graph_30_3 = Graph()
graph_30_3.create_nodes(30)
graph_30_3.create_edges([[13, 18, 6], [8], [20, 20, 14], [15, 26], [16, 8, 7, 17, 17, 29], [23], [0, 16], [4, 18], [1, 4, 22, 13], [11, 22], [22, 17, 16], [9, 25, 18, 21, 22, 28], [23], [0, 20, 8, 21, 22], [2, 15, 24], [3, 20, 14, 16], [4, 6, 10, 15], [10, 4, 4, 18], [0, 7, 11, 29, 17], [25, 23, 23], [2, 2, 13, 15, 24], [11, 13, 27], [8, 9, 10, 11, 13], [12, 19, 19, 5], [20, 28, 14], [11, 19, 28, 29], [3], [21], [24, 25, 11], [18, 4, 25]])
graph_30_3.create_coords([[99, 93], [0, 60], [6, 21], [86, 64], [22, 7], [51, 41], [73, 97], [46, 69], [40, 2], [60, 16], [36, 97], [55, 21], [42, 46], [87, 61], [1, 87], [79, 24], [66, 37], [37, 60], [60, 48], [88, 52], [58, 85], [43, 1], [15, 47], [10, 99], [10, 10], [47, 56], [75, 93], [99, 5], [20, 76], [2, 21]])
min_cover_30_3 = 22

# run_large_ga_instance(graph_30_3, 30)
# run_ant_colony(graph_30_3)

small_inputs = [graph_6_1, graph_6_2, graph_6_3]
medium_inputs = [graph_13_1, graph_13_2, graph_13_3]
large_inputs = [graph_30_1, graph_30_2, graph_30_3]
small_mins = [min_cover_6_1, min_cover_6_2, min_cover_6_3]
medium_mins = [min_cover_13_1, min_cover_13_2, min_cover_13_3]
large_mins = [min_cover_30_1, min_cover_30_2, min_cover_30_3]

def exp(inputs, n):
    if inputs == small_inputs:
        ga = run_small_ga_instance
    elif inputs == medium_inputs:
        ga = run_medium_ga_instance
    else:
        ga = run_large_ga_instance
    correct_ga = 0
    correct_aco = 0
    times_ga = []
    times_aco = []
    for i in range (2):
        chosen_graph = random.choice(inputs)
        min_cover = small_mins[inputs.index(chosen_graph)]
        time_start_ga = time.time()
        res_ga = ga(chosen_graph, n)
        time_end_ga = time.time()
        if res_ga == min_cover:
            correct_ga += 1
        times_ga.append(time_end_ga - time_start_ga)
        time_start_aco = time.time()
        res_aco = run_ant_colony(chosen_graph)
        time_end_aco = time.time()
        if res_aco == min_cover:
            correct_aco += 1
        times_aco.append(time_end_aco - time_start_aco)
        if len(times_ga) == 0:
            avg_ga_time = 0
        else:
            avg_ga_time = sum(times_ga)/len(times_ga)
        if len(times_aco) == 0:
            avg_aco_time = 0
        else:
            avg_aco_time = sum(times_aco)/len(times_aco)
        
    print(tabulate.tabulate([["GA", correct_ga], ["Average GA time", avg_ga_time],["ACO", correct_aco], ["Average ACO time", avg_aco_time]], headers=["Algorithm", "Correct"]))






