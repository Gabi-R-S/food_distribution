from spade.behaviour import OneShotBehaviour
import json
class HandleRequestRequestBehaviour(OneShotBehaviour):
    def __init__(self, data, **kwargs):
        super(**kwargs)
        self.data=data
    
    async def run(self):
        # TODO
        pass
        