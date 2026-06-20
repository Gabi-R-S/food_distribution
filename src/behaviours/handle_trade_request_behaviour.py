from spade.behaviour import OneShotBehaviour
import json
from helpers.utils import *
class HandleTradeRequestBehaviour(OneShotBehaviour):
    def __init__(self, other_agent, data,communication_id, **kwargs):
        super(**kwargs)
        self.trade=reconstruct_trade(data)
        self.other_agent = other_agent
    
    async def run(self):
        trade = self.brain.create_trade_counteroffer(self.agent,self.trade,self.other_agent)
        
        if trade:
            if not self.agent.stock.reserve_all(trade.offer.food_items):
                #TODO: alert brain that reserve failed?
                    
                message= Message(to=self.other_agent, thread=self.communication_id)
                message.set_metadata("performative","cancel")
                await self.send(message)
                return
            
            message= Message(to=self.other_agent,thread=self.communication_id)
            message.set_metadata("performative","agree")
            message.body=json.dumps(trade)
            
            await self.send(message)

            reply = self.receive(timeout=20)
                            
            if reply:
                food_list = reconstruct_food_list(json.loads(reply.body))
                if reply.get_metadata("performative") =="confirm":
                    self.agent.brain.on_food_expected(self.agent, food_list, self.other_agent)
                    
                    self.agent.stock.cancel_reserve_all(trade.offer.food_items)
                    for food_item in trade.offer.food_items:
                        self.agent.stock.remove_item(food_item)
                    
                    message= Message(to=self.agent.food_distributer_address)
                    message.body=json.dumps({"to":self.other_agent,"food": trade.offer.food_items})
                    
                    await self.send(message)                        
            else:
                pass #nothing to do for now
                
        else:
            message= Message(to=self.other_agent, thread=self.communication_id)
            message.set_metadata("performative","cancel")
            await self.send(message)
            
        