from spade.behaviour import CyclicBehaviour
from food_distributer.behaviours.SendFoodBehaviour import SendFoodBehaviour
import json
from spade.template import Template
from helpers.utils import *
class ReceiveFoodBehaviour(CyclicBehaviour):
    async def run(self):
        msg = self.receive(timeout=10)
        if msg:
            data = json.loads(msg.body)
            food_list = reconstruct_food_item_list(data["food"])
            self.agent.brain.add_food_items(self.agent, food_list)
