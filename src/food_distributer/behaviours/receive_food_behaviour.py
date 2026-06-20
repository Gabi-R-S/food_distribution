from spade.behaviour import CyclicBehaviour
from food_distributer.behaviours.SendFoodBehaviour import SendFoodBehaviour
import json
from spade.template import Template

class ReceiveFoodBehaviour(CyclicBehaviour):
    async def run(self):
        msg = self.receive(timeout=10)
        if msg:
            data = json.loads(msg.body)
            self.agent.add_behaviour(SendFoodBehaviour(msg.sender,data["food"],data["to"]))