"""before you start make sure that the openai api key is set to the 
environment variable OPENAI_API"""

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from podcast import Podcast
from ui import UI


#user_name = input("What is your name?\n")
USER_NAME = "Lorenzo Maddalena"

# create the podcast object
podcast = Podcast(USER_NAME)

#instantiate the flask app
app = Flask(__name__)
app.secret_key = "secret"

class MessageForm(FlaskForm):
    message = StringField('message', validators=[DataRequired()])
    submit = SubmitField("send")


# def start_podcast():
#     """starts the selection of the topic and the podcast"""
#     #choose topic 
#     # ui = UI()
#     # todays_topic = ui.topic_selection()
#     # todays_topic = "ai"
#     #start podcast episode
    
#     return podcast
    

@app.route("/")
def home_page():
    """home page"""
    return render_template("index.html")

@app.route("/podcast", methods=["GET", "POST"])
def podcast_page():
    """podcast page"""

    global podcast

    if request.method == "POST":
        podcast.expert.receive_message("ciao")


    podcast.introduce_agent()
    form = MessageForm()
    
    return render_template(
        "podcast.html", 
        messages= podcast.expert.messages,
        form=form
        )
    

if __name__== "__main__":

    podcast = Podcast(USER_NAME)
    podcast.set_topic("ai")
    podcast.generate_ai_agent()
    app.run(debug =True)
    
    

    