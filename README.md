# Interactive_Podcast
Webapp to start an interactive podcast where you can interact with an expert (AI generated) on a topic of your choice.
The objective is to create an app where the user can interview an expert (AI agent) to obtain information on a topic they care about.

The AI agent is currently an instance of OpenAI gpt3.5 turbo, therefore the use of the webapp requires you to have your personal OpenAI API key. 

The user can retrieve the list of rising topics of the last day/weeek (based on google search trends/news) to have a starting topic. (Not yet implemented in the webapp)

## Getting started
Clone the repository or downlaod the content and install the required packages with: 

`pip install -r requirements.txt`

If you don't have one, obtain an OpenAI API key (3 months free trial version available at the time of writing).
Set the environmental variable 'OPENAI_API' as the key that was generated. On Linux you can use the following command:

`export OPENAI_API=##########`

Start the application by running the main function: 

`python interactivepodcast/main.py`

This should start the web server, then you can navigate to the port that was forwarded and start the interaction.

## MVP project

This first version of the project is a text based flask webapp, where the user can select a topic and start a conversation with the AI agent.
The UI is still in development, but the core functionality is implemented in this version.
The use of the webapp requires the use of an OpenAI API key, to set as the environmental variable 'OPENAI_API' before starting the web server 

## High level architecture 

The software is based on the following elements:

- UI to interact and choose the topic
  - main menu to start an interaction
  - list with updated hot topics of the day/week (from google trends/local news articles) (TBD)
- Podcast
  - to start a podcast interaction
- AI agent 
  - Text generation component (powered by Chat-GPT)
  - Text to speech component that will allow the AI agent to speak with natural voice (with bark tts) (TBD)
- User interpretation 
  - voice to text element to allow the interpretation of the messages to the AI agent (TBD)


## Continuous integration

[![Python application](https://github.com/lorenzomad/Interactive_Podcast/actions/workflows/python-app.yml/badge.svg)](https://github.com/lorenzomad/Interactive_Podcast/actions/workflows/python-app.yml)
