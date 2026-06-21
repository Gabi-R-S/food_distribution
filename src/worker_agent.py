
import spade
from spade.agent import Agent
from behaviours.schedule_task_behaviour import ScheduleTaskBehaviour
from behaviours.remove_spoiled_food_behaviour import RemoveSpoiledFoodBehaviour
from behaviours.receive_food_behaviour import ReceiveFoodBehaviour


from behaviours.receive_offer_requests_behaviour import ReceiveOfferRequestsBehaviour
from behaviours.receive_request_requests_behaviour import ReceiveRequestRequestsBehaviour
from behaviours.receive_trade_requests_behaviour import ReceiveTradeRequestsBehaviour

from behaviours.perform_offer_behaviour import PerformOfferBehaviour
from behaviours.perform_request_behaviour import PerformRequestBehaviour
from behaviours.perform_trade_behaviour import PerformTradeBehaviour

from spade.template import Template

class WorkerAgent(Agent):
    def __init__(self,scheduler, stock, neighbour_jids, brain, food_distributer_address, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scheduler = scheduler
        self.stock = stock
        self.neighbour_jids = neighbour_jids
        self.brain=brain
        self.food_distributer_address=food_distributer_address

        self.counters={"offer":0,"trade":0,"request":0}
    
    def begin_offer(self,offer, callback=None):
        communication_id = "offer"+str(self.counters["offer"])
        self.counters["offer"]+=1
        
        template = Template(thread=communication_id)
        self.add_behaviour(PerformOfferBehaviour(offer, communication_id, callback))
        return communication_id
    
    def begin_trade(self,other_agent_jid,request,offer, callback=None):
        communication_id = "trade"+str(self.counters["trade"])
        self.counters["trade"]+=1
        
        template = Template(thread=communication_id)
        self.add_behaviour(PerformTradeBehaviour(other_agent_jid,request,offer, communication_id, callback))
        return communication_id
        
    def begin_request(self,request, callback=None):
        communication_id = "request"+str(self.counters["request"])
        self.counters["request"]+=1
        
        template = Template(thread=communication_id)
        self.add_behaviour(PerformRequestBehaviour(request, communication_id, callback))
        return communication_id
            
    async def setup(self):
        self.add_behaviour(ScheduleTaskBehaviour())
        self.add_behaviour(RemoveSpoiledFoodBehaviour(period=1))
        
        template = Template()
        template.sender=self.food_distributer_address
        self.add_behaviour(ReceiveFoodBehaviour(),template)
        
        template = Template()
        template.set_metadata("performative","request")
        self.add_behaviour(ReceiveRequestRequestsBehaviour(),template)
        
        template = Template()
        template.set_metadata("performative","trade")
        self.add_behaviour(ReceiveTradeRequestsBehaviour(),template)
        
        template = Template()
        template.set_metadata("performative","offer")
        self.add_behaviour(ReceiveOfferRequestsBehaviour(),template)
        
        