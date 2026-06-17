class Brain:
    def schedule_next_task(self, agent, behaviour): # Must return a task or None
        return None
    
    def handle_no_tasks_available(self, agent, behaviour):
        pass
    
    def add_food_items(self, agent, behaviour):
        pass
    
    def on_request_failed(self,agent,behaviour):
        pass
    
    def on_offer_failed(self,agent,behaviour):
        pass
    
    def on_init(self):
        pass
    
    def choose_preferred_offer_to_receive(self, agent, jid_offer_pairs): #must return one such pair
        pass
    def choose_preferred_offer_to_give(self, agent, jid_offer_pairs): #must return one such pair
        pass