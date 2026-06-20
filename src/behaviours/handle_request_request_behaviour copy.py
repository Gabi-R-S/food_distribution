from spade.behaviour import OneShotBehaviour
import json
from helpers.utils import *
from spade.message import Message

from helpers.utils import *

class HandleRequestRequestBehaviour(OneShotBehaviour):
    def __init__(self, other_agent, data,communication_id, **kwargs):
        super(**kwargs)
        self.request=reconstruct_request(data)
        self.other_agent = other_agent
        self.communication_id=communication_id
    
    async def run(self):
        offer= self.brain.create_request_counteroffer(self.agent,self.request,self.other_agent)
        if offer:
            if not self.agent.stock.reserve_all(self.offer.food_items):
                #TODO: alert brain that reserve failed?
                    
                message= Message(to=self.other_agent, thread=self.communication_id)
                message.set_metadata("performative","cancel")
                await self.send(message)
                return
            
            message= Message(to=self.other_agent,thread=self.communication_id)
            message.set_metadata("performative","agree")
            message.body=json.dumps(offer)
            
            await self.send(message)

            reply = self.receive(timeout=20)
            
                            
            if reply:
                self.agent.stock.cancel_reserve_all(offer.food_items)
                if reply.get_metadata("performative") =="confirm":
                    for food_item in offer.food_items:
                        self.agent.stock.remove_food_item(food_item)
                    
                    message= Message(to=self.agent.food_distributer_address)
                    message.body=json.dumps({"to": self.other_agent, "food": offer.food_items})
                    
                    await self.send(message)
                        
            else:
                # if this critical part of the communication fails, assume the food was lost.
                self.agent.stock.cancel_reserve_all(offer.food_items)
                for food_item in offer.food_items:
                    self.agent.stock.remove_food_item(food_item)
                
        else:
            message= Message(to=self.other_agent, thread=self.communication_id)
            message.set_metadata("performative","cancel")
            await self.send(message)
            
        