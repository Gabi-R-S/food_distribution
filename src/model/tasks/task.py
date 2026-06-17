from model.food.food import FoodItem as FoodItem
from datetime import datetime

class Task:
    def __init__(self, name, cost, food_produced:list, length, start_time=None): # food_produced is a list of costs
        self.name = name
        self.cost = cost
        self.food_produced = food_produced
        self.length = length
        self.start_time=start_time
    
    def get_food_produced(self):
        now = datetime.now()
        return [
                FoodItem(
                    food_quantity.type_of_food, now, food_quantity.duration_of_food
                )
                for food_quantity in self.current_task.food_produced
                for _ in range(food_quantity.amount)
            ]
        

    def get_wait_time(self, current_time=datetime.now()) -> float:
        return max(0,self.length+self.start_time- current_time)
