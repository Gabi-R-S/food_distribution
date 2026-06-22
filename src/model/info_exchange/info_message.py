
class InfoMessage:
    def __init__(self,agent_info_dic): #agent_id->agent_info
        self.agent_info_list=agent_info_dic
    
    def get_merged(self, other_message):
        final_dic ={}
        for agent_id, agent_info in self.agent_info_dic.items():
            if agent_id in other_message.agent_info_dic:
                other_agent_info = other_message.agent_info_dic[agent_id]
                if agent_info.timestamp>other_agent_info:
                    final_dic[agent_id]=agent_info
                else:
                    final_dic[agent_id]= other_agent_info           
            else:
                final_dic[agent_id]=agent_info
        
        for agent_id, agent_info in other_message.agent_info_dic.items():
            if agent_id not in final_dic:
                final_dic[agent_id]=agent_info
        
        return InfoMessage(final_dic)