from spade.behaviour import OneShotBehaviour
from spade.message import Message
import json
import helpers.utils as utils

MAX_INVALID_LOOPS=5
class PerformRequestBehaviour(OneShotBehaviour):
    def __init__(self, needed_quantities, communication_id, **kwargs): #needed quantities is a list of food quantities.
        super(**kwargs)
        self.needed_quantities = needed_quantities
        self.communication_id =communication_id
    
    async def run(self):
        
        total_quantity = 0
        for quantity in self.needed_quantities:
            total_quantity=quantity.amount
            
        
        if not self.agent.stock.reserve_space(total_quantity):
            self.agent.brain.on_request_failed(self.agent,self)
            return
        
        for agent_jid in self.agent.neighbour_jids:
            message = Message(to=agent_jid,thread=self.communication_id)
            message.set_metadata("performative", "request")
            message.body= json.dumps(self.needed_quantities)
            
            await self.send(message)
        
        reply_count=0
        num_neighbours=len(self.agent.neighbour_jids)
        offers=[]
        invalid_loops=0
        direct_participant_jids=[]
         
        while reply_count < num_neighbours and invalid_loops < 
MAX_INVALID_LOOPS:
            reply = await self.receive(timeout=5)
            if reply:
                invalid_loops = 0
                reply_count += 1
                
                if reply.get_metadata("performative") == "agree":
                    offers.append(utils.reconstruct_offer(json.loads(reply.body)))
                    direct_participant_jids.append(reply.sender)
            else:
                invalid_loops+=1
            
        
        chosen_agent_jid, favourite_offer= self.agent.brain.choose_preferred_offer_to_receive(self.agent,  list(zip(direct_participant_jids,offers)))
        
        if favourite_offer:
            # if it was picked, it's because we can get the items or don't mind discarding them.
            self.agent.stock.free_reserved_space(total_quantity)
            self.agent.brain.add_food_items(self, favourite_offer.food_items)
                
            for agent_jid in self.agent.neighbour_jids:
                if agent_jid != chosen_agent_jid:
                    message= Message(to=agent_jid,thread=self.communication_id)
                    message.set_metadata("performative", "cancel")
                    await self.send(message)
                else:
                    message= Message(to=agent_jid,thread=self.communication_id)
                    message.set_metadata("performative", "confirm")
                    await self.send(message)
        else:
            for agent_jid in self.agent.neighbour_jids:
                message= Message(to=agent_jid,thread=self.communication_id)
                message.set_metadata("performative", "cancel")
                await self.send(message)