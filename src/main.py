"""before you start make sure that the openai api key is set to the 
environment variable OPENAI_API"""

from podcast import Podcast

#user_name = input("What is your name?\n")
user_name = "Lorenzo Maddalena"
todays_topic = input("What is the topic you would like to discuss today?\n")

podcast = Podcast(user_name, todays_topic)
podcast.introduce_agent()
podcast.start_conversation()
