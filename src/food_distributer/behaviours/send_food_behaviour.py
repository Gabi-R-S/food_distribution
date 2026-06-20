from spade.behaviour import OneShotBehaviour
import json
from spade.template import Template
import asyncio
from spade.message import Message
class SendFoodBehaviour(OneShotBehaviour):
    def __init__(self,from_agent, food_list, to_agent, **kwargs):
        super(**kwargs)
        self.from_agent = from_agent
        self.food_list = food_list
        self.to_agent = food_list
        
    async def run(self):
        time = self.agent.distances[self.from_agent][self.to_agent]
        await asyncio.sleep(time)
        
        message= Message(to=self.to_agent)
        message.body= json.dumps({"from":self.from_agent, "food":self.food_list})
        await self.send(message)
        