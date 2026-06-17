from spade.behaviour import CyclicBehaviour
from behaviours.handle_trade_request_behaviour import HandleTradeRequestBehaviour
import json
class ReceiveTradeRequestsBehaviour(CyclicBehaviour):
    async def run(self):
        msg = self.receive(timeout=10)
        if msg:
            data = json.loads(msg.body)
            self.agent.add_behaviour(HandleTradeRequestBehaviour(data))