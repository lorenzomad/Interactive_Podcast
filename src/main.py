"""before you start make sure that the openai api key is set to the 
environment variable OPENAI_API"""

from podcast import Podcast
from ui import UI


#user_name = input("What is your name?\n")
user_name = "Lorenzo Maddalena"

#choose topic 
ui = UI()
todays_topic = ui.topic_selection()

#start podcast episode
podcast = Podcast(user_name, todays_topic)
podcast.introduce_agent()
podcast.start_conversation()
