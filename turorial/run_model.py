from money_model import MoneyModel

model = MoneyModel(5)

for i in range(10):
  model.step()
