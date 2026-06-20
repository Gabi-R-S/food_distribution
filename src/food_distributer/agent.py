
import spade
from spade.agent import Agent
from food_distributer.behaviours.ReceiveFoodBehaviour import ReceiveFoodBehaviour

class DistributerAgent(Agent):
    def __init__(self,distance_matrix, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.distance_matrix=distance_matrix
        
    async def setup(self):
        self.add_behaviour(ReceiveFoodBehaviour())
