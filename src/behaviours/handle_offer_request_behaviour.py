from spade.behaviour import OneShotBehaviour
import json
from helpers.utils import *
class HandleOfferRequestBehaviour(OneShotBehaviour):
    def __init__(self, other_agent, data,communication_id, **kwargs):
        super(**kwargs)
        self.offer=reconstruct_offer(data)
        self.other_agent = other_agent
        self.communication_id=communication_id
    
    async def run(self):
        request = self.brain.create_offer_counteroffer(self.agent,self.request,self.other_agent)
        
        if request:
            message= Message(to=self.other_agent,thread=self.communication_id)
            message.set_metadata("performative","agree")
            message.body=json.dumps(offer)
            
            await self.send(message)

            reply = self.receive(timeout=20)
                            
            if reply:
                food_list = reconstruct_food_list(json.loads(reply.body))
                if reply.get_metadata("performative") =="confirm":
                    self.agent.brain.on_food_expected(self.agent, food_list, self.other_agent)
                        
            else:
                pass #nothing to do for now
                
        else:
            message= Message(to=self.other_agent, thread=self.communication_id)
            message.set_metadata("performative","cancel")
            await self.send(message)
            
        