
import spade
from spade.agent import Agent
from behaviours.schedule_task_behaviour import ScheduleTaskBehaviour
from behaviours.remove_spoiled_food_behaviour import RemoveSpoiledFoodBehaviour

class WorkerAgent(Agent):
    def __init__(self,scheduler, stock, neighbour_jids, brain, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scheduler = scheduler
        self.stock = stock
        self.neighbours = neighbour_jids
        self.brain=brain
        
    async def setup(self):
        self.add_behaviour(ScheduleTaskBehaviour())
        self.add_behaviour(RemoveSpoiledFoodBehaviour(period=1))