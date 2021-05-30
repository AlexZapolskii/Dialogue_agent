# Dialogue_agent

This project is about building Russian speaking chat-bot/personal assistant, based on RASA 2.0 framework.
Current version is working in command line interface.

My bot is able to tell what is time now and what is weather like in given city.
In order to get weather and time information, I use weather API - https://www.weatherapi.com/.
I use one endpoint that allows to get current weather information for a given city: url = 'https://api.weatherapi.com/v1/current.json'
and has only one parameter - q for city. 

My bot is able to show weather in Russian cities, 
it is capable of identifying complex names like "Нижний Новгород" as city entity and make correct api call.

# To sum up:

Bot functionality:
1) Show time (no parameters)
2) Show weather (entity extraction helps to parameterize API call)
3) Remember users name and repeat it
4) Remember users email and phone number
5) Bot Challenge - answer questions like "are u a human" or "are u a bot"
    
# To try this chat bot u need to do the following things (windows 10):
 
 1) Extract the project
 2) Install latest version of anaconda for windows
 3) Open anaconda prompt
 4) Go to the project directory
 5) Create virtual environment using command "conda create --name virtualenvname
 6) activate venv "conda activate virtualenvname"
 7) install packages: "conda install ujson", "conda install tensorflow" and "pip install rasa" and dont forget to install Microsoft Visual C++ 
 8) If you want to start from scratch - just run "rasa init" command in your terminal, otherwise run "rasa train" to train a new model or "rasa shell" to run a bot in command line
 9) In order to provide api functionality, you should start action server by opening another anaconda prompt, activating venv and typing "rasa run actions"
 10) Type "Привет" to start conversation)

P.S.:
 Dont forget to signup to weather api to get key (insert it to line 21 in actions.py file)

# Brief introduction to Rasa 2.0

  If you want to customize your bot, you should consider the following files:
  
  1) nlu.yml - you can add new intents and provide examples to train nlu model
  2) domain.yml - where you register all intents and provide responses
  3) stories.yml - you should provide possible storylines with certain intents and responses.
  4) action.py - provide your custom python code to run custom actions, call api, etc



