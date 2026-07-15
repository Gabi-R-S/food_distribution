class ReplaceOldestAddFoodItems:
    def __init__(self, max_items):
        self.max_items = max_items

    def add_food_items(self, agent, new_food_items):
        # Add new food items to the stock, replacing the oldest items if necessary
        for item in new_food_items:
            if not agent.stock.is_full():
                agent.stock.add_food_item(item)
            else:
                # Replace the oldest item
                items= agent.stock.get_available_food_items()
                if len(items) == 0:
                    break
                oldest_item = min(items, key=lambda x: x.creation_time)
                agent.stock.remove_food_item(oldest_item)
                agent.stock.add_food_item(item)
                