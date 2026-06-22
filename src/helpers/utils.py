from food.food import FoodItem
from food.food_offer import FoodOffer
from food.food_quantity import FoodQuantity
def reconstruct_food_item_list(parsed_json):
    return [FoodItem(type=item["type"], created_at=item["created_at"], time_to_expire=item["time_to_expire"]) for item in parsed_json]


def reconstruct_food_quantity_list(parsed_json):
    return [FoodItem(type_of_food=item["type_of_food"], duration_of_food=item["duration_of_food"], amount=item["amount"]) for item in parsed_json]

def reconstruct_offer(parsed_json):
    return FoodOffer(reconstruct_food_item_list(parsed_json["food_item"],parsed_json["value"]))

def reconstruct_request(parsed_json):
    return FoodRequest(reconstruct_food_quantity_list(parsed_json["food_item"],parsed_json["value"]))

def reconstruct_trade(parsed_json):
    return {"offer": reconstruct_offer(parsed_json["offer"]),"request": reconstruct_offer(parsed_json["request"])}



def reconstruct_agent_info(data):
    return AgentInfo(data["timestamp"],data["value_list"], reconstruct_food_list(data["food_list"]))
    
def reconstruct_info_message(data):
    agent_info_dic={}
    for k,v in data["agent_info_dic"].items():
        agent_info_dic[k]=reconstruct_agent_info(v)
    return InfoMessage(agent_info_dic)