from graph import *
from matplotlib import pyplot as plt
import numpy as np

class AntColony:
    def __init__(self, graph, colony_size, alpha, beta, evaporation_rate, initial_pheromone):
        self.graph = graph
        self.colony_size = colony_size
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.initial_pheromone = initial_pheromone
        self.pheromone = [[self.initial_pheromone for j in range(len(self.graph.nodes))] for i in range(len(self.graph.nodes))]

    def find_minimum_vertex_cover(self):
        best_solution = None
        best_solution_cost = float('inf')
        for _ in range(self.colony_size):
            solution = self.find_solution()
            solution_cost = self.calculate_solution_cost(solution)
            if solution_cost < best_solution_cost:
                best_solution = solution
                best_solution_cost = solution_cost
            self.update_pheromone(solution)
        return best_solution

    def find_solution(self):
        solution = [0] * len(self.graph.nodes)
        self.visited = [0] * len(self.graph.nodes)
        for i in range(len(self.graph.nodes)):
            if self.visited[i] == 0:
                self.visited[i] = 1
                solution[i] = 1
                for j in self.graph.edges[i]:
                    self.visited[j] = 1

        for i in range(len(self.graph.nodes)):
            for j in self.graph.edges[i]:
                if solution[i] == 0 and solution[j] == 0:
                    solution[i] = 1
                    break

        return solution

    def calculate_solution_cost(self, solution):
        return sum(solution)

    def update_pheromone(self, solution):
        for i in range(len(solution)):
            if solution[i] == 1:
                for j in self.graph.edges[i]:
                    self.pheromone[i][j] += 1
                    self.pheromone[j][i] += 1
        for i in range(len(self.graph.nodes)):
            for j in range(i+1, len(self.graph.nodes)):
                self.pheromone[i][j] *= (1 - self.evaporation_rate)
                self.pheromone[j][i] *= (1 - self.evaporation_rate)

    def plot_graph(self):
        edges = self.graph.edges
        nodes = self.graph.nodes
        coords = self.graph.coords
        
        x = [coords[i][0] for i in nodes]
        y = [coords[i][1] for i in nodes]
        plt.scatter(x, y, c='r')
        for i in range(len(nodes)):
            for j in range(len(edges[i])):
                plt.plot([x[i], x[edges[i][j]]], [y[i], y[edges[i][j]]], 'r')
    
    def plot_solution(self, solution):
        edges = self.graph.edges
        nodes = self.graph.nodes
        coords = self.graph.coords
        
        x = [coords[i][0] for i in nodes]
        y = [coords[i][1] for i in nodes]
        plt.scatter(x, y, c='r')
        covered_vertices = []
        for i in range(len(solution)):
            if solution[i] == 1:
                plt.scatter(x[i], y[i], c='b')
                covered_vertices.append(i)
        for i in range(len(covered_vertices)):
            for j in edges[covered_vertices[i]]:
                plt.plot([x[covered_vertices[i]], x[j]], [y[covered_vertices[i]], y[j]], 'b')

def run_ant_colony(graph):
    colony = AntColony(graph, 100, 1.5, 1, 0.1, 500)

    solution = colony.find_minimum_vertex_cover()

    # colony.plot_graph()
    # colony.plot_solution(solution)
    # plt.show()

    # print('The minimum vertex cover size ants: {}'.format(sum(solution)))
    return sum(solution)


# Metoda find_solution inicjalizuje rozwiązanie jako listę zer o tej samej długości co liczba
# wierzchołków w grafie. Tworzy również listę odwiedzonych wierzchołków wypełnioną zerami o takiej samej długości.
# Następnie iteruje po każdym wierzchołku w grafie i jeśli wierzchołek nie był jeszcze odwiedzony, ustawia wierzchołek i
# wszystkich jego sąsiadów jako odwiedzonych i dodaje wierzchołek do rozwiązania. Następnie iteruje po każdej krawędzi w grafie
# i dodaje jeden z końców każdej krawędzi do rozwiązania, jeśli oba końce krawędzi nie są już w rozwiązaniu.

# Metoda update_pheromone aktualizuje macierz feromonów dodając 1 do poziomu feromonu dla każdej krawędzi,
# która jest włączona w rozwiązanie. Następnie aktualizuje poziomy feromonów dla wszystkich krawędzi w grafie,
# mnożąc je przez (1 - self.evaporation_rate), co odpowiada procesowi wydzielania feromonów.