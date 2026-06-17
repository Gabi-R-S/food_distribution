from spade.behaviour import OneShotBehaviour
import json
class HandleOfferRequestsBehaviour(OneShotBehaviour):
    def __init__(self, data, **kwargs):
        super(**kwargs)
        self.data=data
    
    async def run(self):
        # TODO
        pass
        