"""before you start make sure that the openai api key is set to the 
environment variable OPENAI_API"""

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from podcast import Podcast
from ui import UI


#user_name = input("What is your name?\n")
user_name = "Lorenzo Maddalena"

app = Flask(__name__)
app.secret_key = "secret"

class inputForm(FlaskForm):
    message = StringField('message', validators=[DataRequired()])
    submit = SubmitField("send")


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

@app.route("/podcast", methods=["GET", "POST"])
def podcast_page():

    if request.method == "POST":
        pass


    mypodcast = start_podcast()
    mypodcast.introduce_agent()
    form = inputForm()
    
    return render_template(
        "podcast.html", 
        messages= mypodcast.expert.messages,
        form=form
        )
    

if __name__== "__main__":
    app.run(debug =True)
    
    

    