from datetime import datetime


class Schedule:
    def __init__(self, task_prototypes: list):
        self.task_prototypes = task_prototypes
        #self.current_task = None
        self.current_task_start_time = None

    
    