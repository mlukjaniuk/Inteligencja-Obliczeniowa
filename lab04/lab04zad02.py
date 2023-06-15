import matplotlib.pyplot as plt
import random
import time
from aco import AntColony


plt.style.use("dark_background")


COORDS = (
    (20, 52),
    (43, 50),
    (20, 84),
    (70, 65),
    (29, 90),
    (87, 83),
    (73, 23),
    (13, 11),
    (83, 21),
    (50, 77),
    (32, 14),
    (75, 10),
    (17, 63)
)


def random_coord():
    r = random.randint(0, len(COORDS))
    return r


def plot_nodes(w=12, h=8):
    for x, y in COORDS:
        plt.plot(x, y, "g.", markersize=15)
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])


def plot_all_edges():
    paths = ((a, b) for a in COORDS for b in COORDS)

    for a, b in paths:
        plt.plot((a[0], b[0]), (a[1], b[1]))


plot_nodes()

# Czas wykonywania algorytmu
start = time.time()
colony = AntColony(COORDS, ant_count=1000, alpha=0.5, beta=1.2, 
                    pheromone_evaporation_rate=0.80, pheromone_constant=1000.0,
                    iterations=100)

optimal_nodes = colony.get_path()
end = time.time()
print(end - start)


for i in range(len(optimal_nodes) - 1):
    plt.plot(
        (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
        (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
    )


plt.show()

# Różne zestawy danych i czasy wykonywania algorytmu:

# ant_count = 100, alpha = 0.5, beta = 1.2, pheromone_evaporation_rate = 0.40, pheromone_constant = 1000.0, iterations = 100
# 5.19s

# ant_count = 100, alpha = 0.5, beta = 1.2, pheromone_evaporation_rate = 0.40, pheromone_constant = 1000.0, iterations = 300
# 16.37s

# ant_count = 300, alpha = 0.5, beta = 1.2, pheromone_evaporation_rate = 0.40, pheromone_constant = 1000.0, iterations = 100
# 15.18s

# ant_count = 100, alpha = 0.5, beta = 1.2, pheromone_evaporation_rate = 0.40, pheromone_constant = 1000.0, iterations = 100
# 52.69s

# ant_count = 300, alpha = 0.5, beta = 1.2, pheromone_evaporation_rate = 0.40, pheromone_constant = 1000.0, iterations = 300
# 47.38s

# ant_count = 100, alpha = 0.5, beta = 1.2, pheromone_evaporation_rate = 0.80, pheromone_constant = 1000.0, iterations = 100
# 5.35s

# ant_count = 100, alpha = 0.5, beta = 1.2, pheromone_evaporation_rate = 0.40, pheromone_constant = 500.0, iterations = 100
# 5.06s

# ant_count = 100, alpha = 0.5, beta = 0.5, pheromone_evaporation_rate = 0.80, pheromone_constant = 1000.0, iterations = 100
# 4.98s

# ant_count = 100, alpha = 2, beta = 2, pheromone_evaporation_rate = 0.80, pheromone_constant = 1000.0, iterations = 100
# 5.12s


# Modyfikacja parametrów ma znaczący wpływ na szybkość wykonywania algorytmu. Mowa tutaj zwłaszcza o zmianie liczby mrówek i iteracji, które
# potrafią wydłużyć czas wykonywania algorytmu nawet kilkanaście razy. Zmiana parametrów alpha, beta, pheromone_evaporation_rate i
# pheromone_constant nie wpływa diametralnie na czas wykonywania algorytmu - przy tej samej liczbie mrówek i iteracji czas wykonywania różni
# się o kilkanaście setnych sekundy.