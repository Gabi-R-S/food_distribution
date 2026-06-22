from spade.behaviour import PeriodicBehaviour
import asyncio
from spade.message import Message
class PropagateInfoBehaviour(PeriodicBehaviour):      
    async def run(self):
        content = json.dumps(self.agent.brain.get_info_to_send(self.agent))
        
        for neighbour_jid in self.agent.neighbour_jids:
            message= Message(to=neightbour_jid)
            message.body=content
            message.set_metadata("performative","inform")
            await self.send(message)
        