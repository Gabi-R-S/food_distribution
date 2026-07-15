from datetime import datetime

class Stock:
    def __init__(self, food_items, max_capacity):
        self.food_items = food_items
        self.max_capacity = max_capacity
        self.reserved_items=[]
        self.reserved_space=0
    
    def get_available_food_items(self):
        return [item for item in self.food_items if item not in self.reserved_items]
    
    def can_perform_task(self, task) -> bool:
        counts = {}
        desired_counts = {}
        cost = task.cost # list of food quantities
        
        for quantity in cost:
            counts[quantity.type_of_food] = 0
            desired_counts[quantity.type_of_food] = quantity.amount
        
        for item in self.food_items:
            if item not in self.reserved_items:
                counts[item.type_of_food] += 1
        
        for food_type, desired_amount in desired_counts.items():
            if counts[food_type] < desired_amount:
                return False
        
        return True

    def get_available_space(self):
        return self.max_capacity - len(self.food_items) - self.reserved_space
    
    def add_food_item(self, food_item):
        if len(self.food_items) < self.max_capacity-self.reserved_space:
            self.food_items.append(food_item)
            return True
        else:
            return False
    
    def remove_food_item(self, food_item):
        self.food_items.remove(food_item)
    
    def reserve_space(self, space):
        if self.reserved_space + space <= self.max_capacity - len(self.food_items):
            self.reserved_space += space
            return True
        else:
            return False
        
    def free_reserved_space(self, space):
        self.reserved_space -= space
        if self.reserved_space < 0:
            self.reserved_space = 0
            
    def reserve_item(self, food_item):
        self.reserved_items.append(food_item)
    def remove_spoiled_nonreserved_items(self):
        now = datetime.now()
        self.food_items = [item for item in self.food_items if now - item.created_at < item.time_to_expire or item in self.reserved_items]  
        
    def reserve_all(self, food_items) -> bool:
        # 1. Verify that EVERY requested item is available and not already reserved
        for item in food_items:
            if item not in self.food_items or item in self.reserved_items:
                return False  # Atomic failure: reject the whole batch if one is missing
        
        # 2. Reserve all valid items in the batch
        for item in food_items:
            self.reserve_item(item)
            
        return True
    
    def cancel_reserve_all(self, food_items) -> bool:

        #for item in food_items:
        #    if item not in self.reserved_items:
        #        return False  
        
        for item in food_items:
            self.reserved_items.remove(item)
            
        return True
    
    def is_full(self):
        return len(self.food_items) + self.reserved_space >= self.max_capacity
