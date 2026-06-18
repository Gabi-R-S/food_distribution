from spade.behaviour import CyclicBehaviour
from behaviours.handle_request_request_behaviour import HandleRequestRequestBehaviour
import json
from spade.template import Template

class ReceiveRequestRequestsBehaviour(CyclicBehaviour):
    async def run(self):
        msg = self.receive(timeout=10)
        if msg:
            data = json.loads(msg.body)
            template = Template()
            template.thread = msg.thread
            template.sender =msg.sender
            self.agent.add_behaviour(HandleRequestRequestBehaviour(msg.sender,data,msg.thread), template)