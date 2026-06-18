from spade.behaviour import OneShotBehaviour
import json
from helpers.utils import *
class HandleTradeRequestBehaviour(OneShotBehaviour):
    def __init__(self, other_agent, data,communication_id, **kwargs):
        super(**kwargs)
        self.trade=reconstruct_trade(data)
        self.other_agent = other_agent
    
    async def run(self):
        # TODO
        pass
        