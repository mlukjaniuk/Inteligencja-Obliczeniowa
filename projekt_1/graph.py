import random
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.coords = []
        self.edges_set = set()
    
    def create_nodes(self, n):
        self.nodes = [i for i in range(n)]
        return self.nodes
    
    def create_edges(self, edges):
        self.edges = edges
        return self.edges
    
    def create_coords(self, coords):
        self.coords = coords
        return self.coords

    def create_random_edges(self, n, min_param, max_param):
        self.edges = [[] for i in range(n)]
        max = int(n * max_param)
        min = int(n * min_param)
        if min == 0:
            min = 1
            max = 2

        for i in range(n):
            for j in range(random.randint(min, max)):
                r = random.randint(0, n - 1)
                if r != i:
                    self.edges[i].append(r)
                    self.edges[r].append(i)

        for i in range(n):
            if len(self.edges[i]) == 0:
                r = random.randint(0, n - 1)
                self.edges[i].append(r)
                self.edges[r].append(i)

        return self.edges
    
    def create_random_coords(self, n):
        self.coords = [[] for i in range(n)]
        for i in range(n):
            self.coords[i].append(random.randint(0, 100))
            self.coords[i].append(random.randint(0, 100))
        return self.coords

    def create_edges_set(self):
        for i in range(len(self.edges)):
            for j in self.edges[i]:
                if i < j:
                    self.edges_set.add((i, j))
                else:
                    self.edges_set.add((j, i))
        return self.edges_set

    def plot_all_nodes(self):
        for i in range(len(self.coords)):
            plt.plot(self.coords[i][0], self.coords[i][1], markersize=15, marker=".", c="r")
        plt.axis("off")
        fig = plt.gcf()
        fig.set_size_inches([10, 6])

    def plot_all_edges(self):
        for i in range(len(self.edges)):
            for j in range(len(self.edges[i])):
                plt.plot((self.coords[i][0], self.coords[self.edges[i][j]][0]), (self.coords[i][1], self.coords[self.edges[i][j]][1]), c="r")

    def plot_covered_edges(self, solution):
        for i in range(len(self.edges)):
            if solution[i] == 1:
                for j in range(len(self.edges[i])):
                    plt.plot((self.coords[i][0], self.coords[self.edges[i][j]][0]), (self.coords[i][1], self.coords[self.edges[i][j]][1]), c="b")

    def plot_covered_nodes(self, solution):
        for i in range(len(self.coords)):
            if solution[i] == 1:
                plt.plot(self.coords[i][0], self.coords[i][1], "b.", markersize=15)

