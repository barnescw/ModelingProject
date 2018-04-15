import random

from mesa import Agent, Model
from mesa.time import SimultaneousActivation
from mesa.space import ContinuousSpace

class StudentAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        print(self.unique_id)
        self.move()

    def advance(self):
        pass

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

class BuildingAgent(Agent):
    def __init__(self, name, model, x, y):
        super().__init__(name, model, x, y)

    def step(self):
        print(self.name)

class CampusModel(Model):
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = ContinuousSpace(width, height, False)
        self.schedule = SimultaneousActivation(self)
        for i in range(self.num_agents):
            a = StudentAgent(i, self)
            self.schedule.add(a)

            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.schedule.step()