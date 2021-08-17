from money_model import MoneyModel

import matplotlib.pyplot as plt
import numpy as np

# num_models = 1
num_agents = 50
num_steps = 20

grid_width = 10
grid_height = 10

# Run the model
model = MoneyModel(num_agents, grid_width, grid_height)
for i in range(num_steps):
  model.step()

agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell in model.grid.coord_iter():
  cell_content, x, y = cell
  agent_count = len(cell_content)
  agent_counts[x][y] = agent_count

# plt.imshow(agent_counts, interpolation='nearest')
# plt.colorbar()

gini = model.datacollector.get_model_vars_dataframe()
gini.plot()

plt.show()
