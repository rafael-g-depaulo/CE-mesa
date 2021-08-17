from money_model import MoneyModel

import matplotlib.pyplot as plt
import numpy as np

num_steps = 20
num_models = 1
num_agents = 50

grid_width = 10
grid_height = 10

all_wealth = []
#This runs the model 100 times, each model executing 10 steps.
for j in range(num_models):
  # Run the model
  model = MoneyModel(num_agents, grid_width, grid_height)
  for i in range(num_steps):
    model.step()

  # Store the results
  for agent in model.schedule.agents:
    all_wealth.append(agent.wealth)

  agent_counts = np.zeros((model.grid.width, model.grid.height))
  for cell in model.grid.coord_iter():
      cell_content, x, y = cell
      agent_count = len(cell_content)
      agent_counts[x][y] = agent_count
  plt.imshow(agent_counts, interpolation='nearest')
  plt.colorbar()
  plt.show()

# plt.hist(all_wealth, bins=range(max(all_wealth)+1))
# plt.show()
