class Brain:
    def __init__(self, schedule_next_task_function=None, handle_no_tasks_available_function=None, add_food_items_function=None, on_request_failed_function=None, on_offer_failed_function=None, on_trade_failed_function=None, on_init_function=None, choose_preferred_offer_to_receive_function=None, choose_preferred_request_to_fulfill_function=None, should_accept_trade_function=None, find_matches_function=None, create_request_counteroffer_function=None, create_offer_counteroffer_function=None, create_trade_counteroffer_function=None, on_food_expected_function=None, on_info_received_function=None, get_info_to_send_function=None):
        self.schedule_next_task_function = schedule_next_task_function
        self.handle_no_tasks_available_function = handle_no_tasks_available_function
        self.add_food_items_function = add_food_items_function
        self.on_request_failed_function = on_request_failed_function
        self.on_offer_failed_function = on_offer_failed_function
        self.on_trade_failed_function = on_trade_failed_function
        self.on_init_function = on_init_function
        self.choose_preferred_offer_to_receive_function = choose_preferred_offer_to_receive_function
        self.choose_preferred_request_to_fulfill_function = choose_preferred_request_to_fulfill_function
        self.should_accept_trade_function = should_accept_trade_function
        self.find_matches_function = find_matches_function
        self.create_request_counteroffer_function = create_request_counteroffer_function
        self.create_offer_counteroffer_function = create_offer_counteroffer_function
        self.create_trade_counteroffer_function = create_trade_counteroffer_function
        self.on_food_expected_function = on_food_expected_function
        self.on_info_received_function = on_info_received_function
        self.get_info_to_send_function = get_info_to_send_function

    def schedule_next_task(self, agent, behaviour): # Must return a task or None
        if self.schedule_next_task_function:
            return self.schedule_next_task_function(agent, behaviour)   
        return None
    
    def handle_no_tasks_available(self, agent, behaviour):
        if self.handle_no_tasks_available_function:
            self.handle_no_tasks_available_function(agent, behaviour)

    def add_food_items(self, agent, food_item_list):
        if self.add_food_items_function:
            self.add_food_items_function(agent, food_item_list)

    def on_request_failed(self,agent,behaviour):
        if self.on_request_failed_function:
            self.on_request_failed_function(agent, behaviour)

    def on_offer_failed(self,agent,behaviour):
        if self.on_offer_failed_function:
            self.on_offer_failed_function(agent, behaviour)
    def on_trade_failed(self,agent,behaviour):
        if self.on_trade_failed_function:
            self.on_trade_failed_function(agent, behaviour)
    
    def on_init(self):
        if self.on_init_function:
            self.on_init_function()

    def choose_preferred_offer_to_receive(self, agent, jid_offer_pairs): #must return one such pair
        if self.choose_preferred_offer_to_receive_function:
            return self.choose_preferred_offer_to_receive_function(agent, jid_offer_pairs)
        return None

    def choose_preferred_request_to_fulfill(self, agent, jid_request_pairs): #must return one such pair
        if self.choose_preferred_request_to_fulfill_function:
            return self.choose_preferred_request_to_fulfill_function(agent, jid_request_pairs)
        return None

    def should_accept_trade(self,agent, proposal, other_agent_jid) -> bool:
        if self.should_accept_trade_function:
            return self.should_accept_trade_function(agent, proposal, other_agent_jid)
        return False

    def find_matches(self,agent,needed_quantities, context="offer"): #returns a list of foods that fill the quantities, or none otherwise
        if self.find_matches_function:
            return self.find_matches_function(agent, needed_quantities, context)
        return None
    
    def create_request_counteroffer(self,agent,request, other_agent_jid): #None to cancel
        if self.create_request_counteroffer_function:
            return self.create_request_counteroffer_function(agent, request, other_agent_jid)
        return None
    
    def create_offer_counteroffer(self,agent,request, other_agent_jid): #None to cancel
        if self.create_offer_counteroffer_function:
            return self.create_offer_counteroffer_function(agent, request, other_agent_jid)
        return None
    def create_trade_counteroffer(self,agent,request, other_agent_jid): #None to cancel
        if self.create_trade_counteroffer_function:
            return self.create_trade_counteroffer_function(agent, request, other_agent_jid)
        return None
    def on_food_expected(self, agent, food_list, other_agent_jid):
        if self.on_food_expected_function:
            self.on_food_expected_function(agent, food_list, other_agent_jid)

    def on_info_received(self, agent, agent_info):
        if self.on_info_received_function:
            self.on_info_received_function(agent, agent_info)

    def get_info_to_send(self,agent):
        if self.get_info_to_send_function:
            return self.get_info_to_send_function(agent)
        return None