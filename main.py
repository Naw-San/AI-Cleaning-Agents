import numpy as np  # For numerical operations and working with arrays
import matplotlib.pyplot as plt  # For visualizing data (e.g., the grid as a heatmap)
import random  # For random number generation (e.g., agent movement and dirt placement)
from tabulate import tabulate  # For creating formatted tables
from environment import Environment


def run_simulation(agent_class, grid_size, dirt_percentage):
    env = Environment(grid_size, grid_size, dirt_percentage)
    agent = agent_class(env)
    for _ in range(10000):
        agent.act()

    # Calculate percentage of cleaned grids
    return env.get_clean_cell_percentage()

def average_performance(agent_class, grid_size, dirt_percentage, runs=10):
    performances = []
    for _ in range(runs):
        performance = run_simulation(agent_class, grid_size, dirt_percentage)
        performances.append(performance)
    return np.mean(performances)

# Prepare table data
table_data = []
for grid_size in [10, 20, 50, 100, 500, 1000]:
    for agent_class in [RandomizedAgent, ReflexAgent, ModelBasedAgent]:
        performance = average_performance(agent_class, grid_size, 0.5)
        table_data.append([agent_class.__name__, grid_size, f"{performance:.2f}%"])


# Print table
headers = ["Agent Type", "Grid Size", "Average Performance"]
print(tabulate(table_data, headers, tablefmt="grid"))
