from spade.behaviour import CyclicBehaviour
from behaviours.handle_request_request_behaviour import HandleRequestRequestBehaviour
import json
class ReceiveRequestRequestsBehaviour(CyclicBehaviour):
    async def run(self):
        msg = self.receive(timeout=10)
        if msg:
            data = json.loads(msg.body)
            self.agent.add_behaviour(HandleRequestRequestBehaviour(data))