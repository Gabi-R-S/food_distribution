from spade.behaviour import CyclicBehaviour
import asyncio
class ScheduleTaskBehaviour(CyclicBehaviour):
    async def run(self):
        
        task=self.agent.brain.schedule_next_task(self.agent, self)
        if task:
            food = self.agent.bran.find_matches(self.agent,task,cost,"eat") # if it was suggested, it's because there is food to do it.
            for food_item in food:
                self.agent.stock.remove_food_item(food_item)
            await asyncio.sleep(task.get_wait_time())  
            new_food = task.get_food_produced()         
            self.agent.brain.add_food_items(self.agent, self)
        else:
            self.agent.brain.handle_no_tasks_available(self.agent, self)
            
        
        
        
        