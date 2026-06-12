class Task:
    def __init__(self, name, cost, food_produced:list, length): # food_produced is a list of costs
        self.name = name
        self.cost = cost
        self.food_produced = food_produced
        self.length = length
