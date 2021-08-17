from money_model import MoneyModel, compute_gini

from mesa.batchrunner import BatchRunner

import matplotlib.pyplot as plt
import numpy as np

fixed_params = {
  "width": 10,
  "height": 10
}

variable_params = {
  "N": range(10, 500, 10)
}

batch_run = BatchRunner(
  MoneyModel,
  variable_params,
  fixed_params,
  iterations=5,
  max_steps=100,
  model_reporters={"Gini": compute_gini}
)

batch_run.run_all()

run_data = batch_run.get_model_vars_dataframe()
run_data.head()
plt.scatter(run_data.N, run_data.Gini)

plt.show()
