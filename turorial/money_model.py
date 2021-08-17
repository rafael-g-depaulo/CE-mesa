# tutorial code from https://mesa.readthedocs.io/en/master/tutorials/intro_tutorial.html

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid

class MoneyAgent(Agent):
  """ An agent with fixed initial wealth."""
  def __init__(self, unique_id, model):
    super().__init__(unique_id, model)
    self.wealth = 1

  def step(self):
    # move into neighboring cell
    possible_steps = self.model.grid.get_neighborhood(
      self.pos,
      moore=True,
      include_center=False)
    new_position = self.random.choice(possible_steps)
    self.model.grid.move_agent(self, new_position)

    # give money to roommate
    if self.wealth > 0:
      self.give_money_to_random_roommate()

  def give_money_to_random_roommate(self):
    roommates = self.model.grid.get_cell_list_contents([self.pos])
    if len(roommates) > 1:
      lucky = self.random.choice(roommates)
      lucky.wealth += 1
      self.wealth -= 1

class MoneyModel(Model):
  """A model with some number of agents."""
  def __init__(self, N, width, height):
    self.num_agents = N
    self.grid = MultiGrid(width, height, True)
    self.schedule = RandomActivation(self)

    # Create agents
    for i in range(self.num_agents):
      a = MoneyAgent(i, self)
      self.schedule.add(a)
      x = self.random.randrange(self.grid.width)
      y = self.random.randrange(self.grid.height)
      self.grid.place_agent(a, (x, y))

  def step(self):
    '''Advance the model by one step.'''
    self.schedule.step()
