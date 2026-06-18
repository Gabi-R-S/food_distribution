from spade.behaviour import OneShotBehaviour
import json
class HandleOfferRequestBehaviour(OneShotBehaviour):
    def __init__(self, other_agent,data,communication_id,should_reserve=True **kwargs):
        super(**kwargs)
        self.data=data
        self.other_agent = other_agent
    
    async def run(self):
        # TODO
        pass
        