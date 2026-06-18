from spade.behaviour import OneShotBehaviour

class PerformTradeBehaviour(OneShotBehaviour):
    def __init__(self, target_jid,request, offer, communication_id, reserve_space=True, **kwargs):
        super(**kwargs)
        self.offer = offer
        self.request =request
        self.communication_id =communication_id
        self.reserve_space=reserve_space
        self.target_jid
        
    async def run(self):
        if not self.agent.stock.reserve_all(self.offer.food_items):
            self.agent.brain.on_offer_failed(agent,self)
            return
        
        total_quantity = 0
        for quantity in self.request:
            total_quantity=quantity.amount
        
        reserve_space= total_quantity-len(self.offer.food_items)
        
        if reserve_space >0 and self.reserve_space:
            if not self.agent.stock.reserve_space(reserve_space):
                self.agent.brain.on_trade_failed(self.agent,self)
                return
        
        
        message = Message(to=self.target_jid,thread=self.communication_id)
        message.set_metadata("performative", "trade")
        message.body= json.dumps({
                "request": self.request,
                "offer": self.offer
            })
            
            await self.send(message)
        
        
        reply = await self.receive(timeout=10)
        if reply:
            if reply.get_metadata("performative") == "agree":
                other_trade = utils.reconstruct_trade(json.loads(reply.body)))
                if should_accept_trade(self.agent, other_trade, reply.agent_jid)
                    self.agent.stock.cancel_reserve_all(self.offer.food_items) 
                    offered= self.agent.brain.find_matches(self.agent)
                    
                    if offered is None:
                        self.agent.stock.cancel_reserve_all(self.offer.food_items)
                        if reserve_space >0 and self.reserve_space:
                            self.agent.stock.free_reserved_space(reserve_space)
                        message= Message(to=self.target_jid,thread=self.communication_id)
                        message.set_metadata("performative", "cancel")
                        await self.send(message)
                    else:    
                        self.agent.stock.remove_food_item(offered)
                        self.agent.brain.add_food_items(self.agent, other_trade.request.food_items)
                        
                        message= Message(to=self.target_jid,thread=self.communication_id)
                        message.set_metadata("performative", "confirm")
                        message.body = json.dumps(offered)
                        await self.send(message) 
                else:
                            
                    self.agent.stock.cancel_reserve_all(self.offer.food_items)
                    if reserve_space >0 and self.reserve_space:
                        self.agent.stock.free_reserved_space(reserve_space)
                    message= Message(to=self.target_jid,thread=self.communication_id)
                    message.set_metadata("performative", "cancel")
                    await self.send(message)
 
        else:
            self.agent.stock.cancel_reserve_all(self.offer.food_items)
            if reserve_space >0 and self.reserve_space:
                self.agent.stock.free_reserved_space(reserve_space)

            
        