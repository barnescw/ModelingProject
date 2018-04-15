from mesa.visualization.ModularVisualization import ModularServer

from congestion import CampusModel
from SimpleContinuousModule import SimpleCanvas


def student_draw(agent):
    portrayal = {"Shape": "circle",
                 "Color": "red",
                 "Filled": "true",
                 "Layer": 0,
                 "r": 0.5}
    return portrayal


campus_canvas = SimpleCanvas(student_draw, 500, 500)
model_params = {
    "N": 12,
    "width": 50,
    "height": 50
}

server = ModularServer(CampusModel, [campus_canvas], "Campus Congestion", model_params)