import os

import openai


OPENAI_KEY = os.environ.get("OPENAI_API")



class AiAgent:
    """class to provide the AI agent to the user"""

    def __init__(self, name, gender, topic) -> None:
        openai.api_key = OPENAI_KEY
        self.topic = topic
        self.name = name
        self.gender = gender
        self.initialize_agent("expert")


    def initialize_agent(self, role):
        """sends the first message to initialize the agent's role"""
        self.messages = [ {"role": "system",
                           "content": f"You are a {role} in {self.topic},"
                            "simulate that you are a guest in a podcast as the expert on the topic"
                            "never disclose that you are an AI language model, but instead "
                            "you should remain in character as the expert for the whole conversation"
                           } ]

    def start_chat(self):
        """Starts the agent for the chat"""
        while True:
            message = input("User: \n")
            if message and message.lower() != "stop":
                self.receive_message(message)
                

            

    def receive_message(self, message):
        """receives and replies to a single message"""
        self.messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages
        )

        reply = chat.choices[0].message.content
        print(f"\n {self.name}: {reply}")
        self.messages.append({"role": "assistant", "content": reply})
