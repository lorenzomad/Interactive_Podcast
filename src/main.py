from podcast import Podcast
from ui import UI
"""before you start make sure that the openai api key is set to the 
environment variable OPENAI_API"""


#user_name = input("What is your name?\n")
user_name = "Lorenzo Maddalena"


ui = UI()
todays_topic = ui.topic_selection()

podcast = Podcast(user_name, todays_topic)
podcast.introduce_agent()
podcast.start_conversation()
