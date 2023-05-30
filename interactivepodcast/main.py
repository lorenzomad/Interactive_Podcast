"""before you start make sure that the openai api key is set to the 
environment variable OPENAI_API"""

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from podcast.podcast import Podcast
from agent.tts import TTS


#user_name = input("What is your name?\n")
USER_NAME = "Lorenzo"

# create the podcast object
podcast = Podcast(USER_NAME)

tts = TTS()
tts.generate_audio("hello I am adam")
tts.play_audio()

#instantiate the flask app
app = Flask(__name__)
app.secret_key = "secret"

class MessageForm(FlaskForm):
    """form for the sending of messages to the ai agent"""
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField("Send")

class TopicForm(FlaskForm):
    """form for selecting the topic of the podcast"""
    topic = StringField('Topic', validators=[DataRequired()])
    submit = SubmitField("Start Conversation")


@app.route("/", methods= ["GET", "POST"])
def home_page():
    """home page"""
    topic_form = TopicForm()

    if topic_form.validate_on_submit():
        podcast.set_topic(topic_form.topic.data)
        podcast.generate_ai_agent()
        podcast.introduce_agent()

    return render_template("index.html", form=topic_form)


@app.route("/podcast", methods=["GET", "POST"])
def podcast_page():
    """podcast page"""
    message_form = MessageForm()

    if message_form.validate_on_submit():
        message = message_form.message.data
        podcast.expert.receive_message(message)

    return render_template(
        "podcast.html", 
        messages=podcast.expert.messages[1:],
        form=message_form
        )


if __name__== "__main__":

    app.run(debug =True)
