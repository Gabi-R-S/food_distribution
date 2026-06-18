from food.food import FoodItem
from food.food_offer import FoodOffer
from food.food_quantity import FoodQuantity
def reconstruct_food_item_list(self,parsed_json):
    return [FoodItem(type=item["type"], created_at=item["created_at"], time_to_expire=item["time_to_expire"]) for item in parsed_json]


def reconstruct_food_quantity_list(self,parsed_json):
    return [FoodItem(type_of_food=item["type_of_food"], duration_of_food=item["duration_of_food"], amount=item["amount"]) for item in parsed_json]

def reconstruct_offer(self,parsed_json):
    return FoodOffer(reconstruct_food_item_list(parsed_json["food_item"],parsed_json["value"]))

def reconstruct_request(self,parsed_json):
    return FoodRequest(reconstruct_food_quantity_list(parsed_json["food_item"],parsed_json["value"]))

def reconstruct_trade(self,parsed_json):
    return {"offer": reconstruct_offer(parsed_json["offer"]),"request": reconstruct_offer(parsed_json["request"])}