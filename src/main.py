from podcast import Podcast
from ai_agent import AI_agent

"""before you start make sure that the openai api key is set to the 
environment variable OPENAI_API"""

#user_name = input("What is your name?\n")
user_name = "Lorenzo Maddalena"
todays_topic = input("What is the topic you would like to discuss today?\n")

podcast = Podcast(user_name, todays_topic)
print(podcast.generate_intro())
podcast.start_conversation()