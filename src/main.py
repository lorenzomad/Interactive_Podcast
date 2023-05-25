"""before you start make sure that the openai api key is set to the 
environment variable OPENAI_API"""

import time

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from podcast import Podcast
from ui import UI


#user_name = input("What is your name?\n")
USER_NAME = "Lorenzo"

# create the podcast object
podcast = Podcast(USER_NAME)

#instantiate the flask app
app = Flask(__name__)
app.secret_key = "secret"

class MessageForm(FlaskForm):
    message = StringField('message', validators=[DataRequired()])
    submit = SubmitField("send")

class TopicForm(FlaskForm):
    topic = StringField('topic', validators=[DataRequired()])
    submit = SubmitField("Start Conversation")


@app.route("/", methods= ["GET", "POST"])
def home_page():
    """home page"""
    topic_form = TopicForm()
    print(topic_form.topic.data)

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
        messages=podcast.expert.messages if podcast.expert is not None else [],
        form=message_form
        )


if __name__== "__main__":

    app.run(debug =True)
