from spade.behaviour import CyclicBehaviour
from food_distributer.behaviours.SendFoodBehaviour import SendFoodBehaviour
import json
from spade.template import Template
from helpers.utils import *
class ReceiveInfoBehaviour(CyclicBehaviour):
    async def run(self):
        msg = self.receive(timeout=10)
        if msg:
            data = json.loads(msg.body)
            agent_info = reconstruct_info_message(data)
            self.agent.brain.on_info_received(self.agent, agent_info)
