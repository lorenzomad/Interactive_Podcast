# Interactive_Podcast
Generates an interactive podcast where the user can interact with the other people.
The objective is to create an app where the user can interview an expert (AI agent) to obtain information on a topic they care about.

The user can retrieve the list of rising topics of the last day/weeek (based on google search trends/news) to have a starting topic.


## High level architecture 

The software will be based on the following elements:

- UI to interact and choose the topic
  - main menu to start an interaction
  - list with updated hot topics of the day/week (from google trends/local news articles)
- Podcast
  - to start a podcast interaction  
- AI agent 
  - Text generation component (powered by Chat-GPT)
  - Text to speech component that will allow the AI agent to speak with natural voice (with bark tts)
- User interpretation 
  - voice to text element to allow the interpretation of the messages to the AI agent

## MVP objective

The MVP objective for the application is to create a text based version of the interactive podcast to run in Python


[![Python application](https://github.com/lorenzomad/Interactive_Podcast/actions/workflows/python-app.yml/badge.svg)](https://github.com/lorenzomad/Interactive_Podcast/actions/workflows/python-app.yml)
