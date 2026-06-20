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
        requests=[]
        invalid_loops=0
        direct_participant_jids=[]
         
        while reply_count < num_neighbours and invalid_loops < 
MAX_INVALID_LOOPS:
            reply = await self.receive(timeout=5)
            if reply:
                invalid_loops = 0
                reply_count += 1
                
                if reply.get_metadata("performative") == "agree":
                    requests.append(utils.reconstruct_request(json.loads(reply.body)))
                    direct_participant_jids.append(reply.sender)
            else:
                invalid_loops+=1
            
        
        chosen_agent_jid, food_items= self.agent.brain.choose_preferred_request_to_fulfill(self.agent,  list(zip(direct_participant_jids,requests)))
        
        if food_items:
            # if it was picked, it's because we can offer the items
            
            self.agent.stock.cancel_reserve_all(self.offer.food_items)
            
            for food_item in food_items:
                self.agent.stock.remove_food_item(food_item)
            
            message = Message(to=self.food_distributer_address)
            message.body=json.dumps({"to": chosen_agent_jid, "food": food_items})
                
            for agent_jid in self.agent.neighbour_jids:
                if agent_jid != chosen_agent_jid:
                    message= Message(to=agent_jid,thread=self.communication_id)
                    message.set_metadata("performative", "cancel")
                    await self.send(message)
                else:
                    message= Message(to=agent_jid,thread=self.communication_id)
                    message.set_metadata("performative", "confirm")
                    message.body = json.dumps(food_items)
                    await self.send(message)
        else:
            for agent_jid in self.agent.neighbour_jids:
                message= Message(to=agent_jid,thread=self.communication_id)
                message.set_metadata("performative", "cancel")
                await self.send(message)    
        
    
        