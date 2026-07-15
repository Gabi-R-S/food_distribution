class RoundRobinScheduleNextTask:
    def __init__(self, task_prototypes: list):
        self.task_prototypes = task_prototypes
        self.current_task_index = 0
    
    def __call__(self, agent, behaviour):
        if not self.task_prototypes:
            return None
        
        initial_index = self.current_task_index
        next_index = (self.current_task_index + 1) % len(self.task_prototypes)
        task = None
        
        while next_index != initial_index:
            task = self.task_prototypes[self.current_task_index]
            
            if agent.stock.can_perform_task(task):
                break
            
            task = None
            self.current_task_index = next_index
            next_index = (self.current_task_index + 1) % len(self.task_prototypes)
        
        self.current_task_index = next_index
                
        return task
        