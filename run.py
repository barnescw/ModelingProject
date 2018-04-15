'''import numpy as np
import matplotlib.pyplot as plt
import time

from congestion import *

n_students = 12
minutes = 60
width = 5
height = 5

# create model
model = CampusModel(n_students, width, height)

agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
plt.imshow(agent_counts, interpolation='nearest')
plt.colorbar()
plt.show()

for i in range(minutes):
    model.step()
    time.sleep(10)
'''

from server import server
server.port = 8521 # The default
server.launch()
