from spade.behaviour import OneShotBehaviour

class PerformOfferBehaviour(OneShotBehaviour):
    def __init__(self, offer, communication_id, **kwargs):
        super(**kwargs)
        self.offer = offer
        self.communication_id =communication_id
    
    async def run(self):
        if not self.agent.stock.reserve_all(self.offer.food_items):
            self.agent.brain.on_offer_failed(agent,self)
            return
        
        for agent_jid in self.agent.neighbour_jids:
            message = Message(to=agent_jid,thread=self.communication_id)
            message.set_metadata("performative", "offer")
            message.body= json.dumps(self.offer)
            
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
                    offers.append(utils.reconstruct_offers(json.loads(reply.body)))
                    direct_participant_jids.append(reply.sender)
            else:
                invalid_loops+=1
            
        
        chosen_agent_jid, favourite_offer= self.agent.brain.choose_preferred_offer_to_give(self.agent,  list(zip(direct_participant_jids,offers)))
        
        if favourite_offer:
            # if it was picked, it's because we can offer the items
            
            self.agent.stock.cancel_reserve_all(self.offer.food_items)
            for food_item in favourite_offer.food_items:
                self.agent.stock.remove_food_item(food_item)
            
            
                
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
        
    
        