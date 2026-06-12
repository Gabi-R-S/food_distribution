from spade.behaviour import PeriodicBehaviour
import asyncio
class RemoveSpoiledFoodBehaviour(PeriodicBehaviour):
    async def run(self):
        self.agent.stock.remove_spoiled_nonreserved_items()