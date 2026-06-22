class Brain:
    def schedule_next_task(self, agent, behaviour): # Must return a task or None
        return None
    
    def handle_no_tasks_available(self, agent, behaviour):
        pass
    
    def add_food_items(self, agent, food_item_list):
        pass
    
    def on_request_failed(self,agent,behaviour):
        pass
    
    def on_offer_failed(self,agent,behaviour):
        pass
    
    def on_trade_failed(self,agent,behaviour):
        pass
    
    def on_init(self):
        pass
    
    def choose_preferred_offer_to_receive(self, agent, jid_offer_pairs): #must return one such pair
        pass
    def choose_preferred_request_to_fulfill(self, agent, jid_request_pairs): #must return one such pair
        pass
    
    def should_accept_trade(self,agent, proposal, other_agent_jid) -> bool:
        pass
    
    def find_matches(self,agent,needed_quantities, context="offer"): #returns a list of foods that fill the quantities, or none otherwise
        return None
    
    def create_request_counteroffer(self,agent,request, other_agent_jid): #None to cancel
        return None
    
    def create_offer_counteroffer(self,agent,request, other_agent_jid): #None to cancel
        return None
    def create_trade_counteroffer(self,agent,request, other_agent_jid): #None to cancel
        return None
    def on_food_expected(self, agent, food_list, other_agent_jid):
        pass
    
    def on_info_received(self, agent, agent_info):
        pass
    
    def get_info_to_send(self,agent):
        return None