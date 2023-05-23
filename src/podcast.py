import random

import names

from ai_agent import AI_agent

GENDERS = ["female", "male"]

class Podcast:
    """class to manage the interaction between the user and the AI agent
    the class will output the text to the user"""

    def __init__(self, user_name, topic) -> None:
        self.user_name = user_name
        self.topic = topic
        self.expert = self.generate_ai_agent()

    def generate_ai_agent(self):
        """creates an ai agent on the defined topic"""
        agent_gender = random.choice(GENDERS)
        agent_name = names.get_full_name(gender=agent_gender)
        return AI_agent(agent_name, agent_gender, self.topic)
    
    def generate_intro(self):
        """generates and returns an introduction string"""
        introduction = f""" Hello {self.user_name}, please meet 
        {self.expert.name} who will be today's episode expert on the topic
        {self.topic}"""
        return introduction
    
    def start_conversation(self):
        self.expert.start_chat()

