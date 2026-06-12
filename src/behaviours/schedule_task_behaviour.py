from spade.behaviour import CyclicBehaviour
import asyncio
class ScheduleTaskBehaviour(CyclicBehaviour):
    async def run(self):
        
        new_food = self.agent.scheduler.get_food_produced_by_current_task()         
        self.agent.brain.process_task_results(self.agent.scheduler,self.agent.stock ,new_food)
        
        
        
        if self.agent.brain.schedule_next_task(self.agent.stock, self.agent.scheduler):
            await asyncio.sleep(self.agent.scheduler.get_wait_time())  
        else:
            pass # Negotiate needs with collectors