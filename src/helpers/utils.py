from food.food import FoodItem
from food.food_offer import FoodOffer
def reconstruct_food_item_list(self,parsed_json):
    return [FoodItem(type=item["type"], created_at=item["created_at"], time_to_expire=item["time_to_expire"]) for item in parsed_json]

def reconstruct_offer(self,parsed_json):
    return FoodOffer(reconstruct_food_item_list(parsed_json["food_item"],parsed_json["value"]))