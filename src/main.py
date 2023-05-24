"""before you start make sure that the openai api key is set to the 
environment variable OPENAI_API"""

from flask import Flask, render_template

from podcast import Podcast
from ui import UI


#user_name = input("What is your name?\n")
user_name = "Lorenzo Maddalena"

app = Flask(__name__)


def start_podcast():
    """starts the selection of the topic and the podcast"""
    #choose topic 
    # ui = UI()
    # todays_topic = ui.topic_selection()
    todays_topic = "ai"
    #start podcast episode
    podcast = Podcast(user_name, todays_topic)
    return podcast
    

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/podcast")
def podcast_page():
    mypodcast = start_podcast()
    mypodcast.introduce_agent()
    
    return render_template("podcast.html", messages= mypodcast.expert.messages)
    

if __name__== "__main__":
    app.run(debug =True)
    
    

    