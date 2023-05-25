import random

import names

from ai_agent import AiAgent

GENDERS = ["female", "male"]

class Podcast:
    """class to manage the interaction between the user and the AI agent
    the class will output the text to the user"""

    def __init__(self, user_name) -> None:
        self.user_name = user_name
        self.topic = None
        self.expert = None
        
    
    def set_topic(self, topic):
        """sets the topic of the podcast"""
        self.topic = topic

    def generate_ai_agent(self):
        """creates an ai agent on the defined topic"""
        if self.topic != None:
            agent_gender = random.choice(GENDERS)
            agent_name = names.get_full_name(gender=agent_gender)
            self.expert = AiAgent(agent_name, agent_gender, self.topic)
        else:
            print("You need to select a topic first")

    def introduce_agent(self):
        """generates and returns an introduction string"""
        introduction = f""" Hello {self.expert.name}, please meet {self.user_name}. 
        He will be today's episode expert on the topic {self.topic}. 
        {self.expert.name}, do you mind giving an introduction about yourself?"""
        print(introduction)
        self.expert.receive_message(introduction)
    
    def start_conversation(self):
        self.expert.start_chat()

