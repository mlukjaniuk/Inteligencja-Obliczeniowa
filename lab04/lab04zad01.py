import pyswarms as ps
import numpy as np
import math
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt

options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}

x_max = np.ones(6)
x_min = np.zeros(6)
my_bounds = (x_min, x_max)

def endurance(tab):
    x, y, z, u, v, w = tab
    return -1 * (math.exp(-2*(y-math.sin(x))**2) + math.sin(z*u) + math.cos(v*w))

def forward_prop(params):
    j = list(map(endurance, params))
    return np.array(j)

def f(x):
    j = list(map(endurance, x))
    return np.array(j)

optimizer = ps.single.GlobalBestPSO(n_particles=100, dimensions=6, options=options, bounds=my_bounds)
optimizer.optimize(f, iters=1000)

cost_history = optimizer.cost_history
plot_cost_history(cost_history)
plt.show()