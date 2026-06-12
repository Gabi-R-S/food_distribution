from datetime import datetime
from model.food.food import FoodItem as FoodItem


class Schedule:
    def __init__(self, task_prototypes: list):
        self.task_prototypes = task_prototypes
        self.current_task = None
        self.current_task_start_time = None

    def get_wait_time(self, current_time) -> float:
        return 0.0

    def has_scheduled_task(self) -> bool:
        return self.current_task is not None

    def get_food_produced_by_current_task(self):
        now = datetime.now()
        if self.current_task:
            return [
                FoodItem(
                    food_quantity.type_of_food, now, food_quantity.duration_of_food
                )
                for food_quantity in self.current_task.food_produced
                for _ in range(food_quantity.amount)
            ]
        else:
            return []

    