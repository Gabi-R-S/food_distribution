from spade.behaviour import OneShotBehaviour

class PerformTradeBehaviour(OneShotBehaviour):
    def __init__(self, target_jid,request, offer, communication_id, **kwargs):
        super(**kwargs)
        self.offer = offer
        self.request =request
        self.communication_id =communication_id
        self.target_jid
        
    async def run(self):
        if not self.agent.stock.reserve_all(self.offer.food_items):
            self.agent.brain.on_offer_failed(agent,self)
            return
        
        
        
        message = Message(to=self.target_jid,thread=self.communication_id)
        message.set_metadata("performative", "trade")
        message.body= json.dumps({
                "request": self.request,
                "offer": self.offer
            })
            
            await self.send(message)
        
        
        reply = await self.receive(timeout=20)
        if reply:
            if reply.get_metadata("performative") == "agree":
                other_trade = utils.reconstruct_trade(json.loads(reply.body)))
                if should_accept_trade(self.agent, other_trade, reply.agent_jid)
                    self.agent.stock.cancel_reserve_all(self.offer.food_items) 
                    offered= self.agent.brain.find_matches(self.agent,other_trade.request)
                    
                    if offered is None:
                        message= Message(to=self.target_jid,thread=self.communication_id)
                        message.set_metadata("performative", "cancel")
                        await self.send(message)
                    else:    
                        for food_item in offered:
                            self.agent.stock.remove_food_item(offered)
                        
                        message= Message(to=self.food_distributer_address)
                        message.body = json.dumps({"to": self.target_id,"food":offered})
                        await self.send(message) 
                        
                        self.brain.on_food_expected(self.agent,other_trade.request.food_items, self.target_jid)
            
                        message= Message(to=self.target_jid,thread=self.communication_id)
                        message.set_metadata("performative", "confirm")
                        message.body = json.dumps(offered)
                        await self.send(message) 
                else:
                            
                    self.agent.stock.cancel_reserve_all(self.offer.food_items)
                    message= Message(to=self.target_jid,thread=self.communication_id)
                    message.set_metadata("performative", "cancel")
                    await self.send(message)
 
        else:
            self.agent.stock.cancel_reserve_all(self.offer.food_items)

            
        