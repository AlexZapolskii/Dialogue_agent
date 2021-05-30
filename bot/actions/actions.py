# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet, EventType
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict

import requests
import json
#wether api key
key = '####'  # Enter valid api key for weather api!


url = 'https://api.weatherapi.com/v1/current.json'
#url =  'https://api.weatherapi.com/v1/current.json?key=2873e6e7e817472f848180405212904&q=Moscow&aqi=no'
params = {'q': 'Moscow',
          'key': key}
#


class ActionCheckTime(Action):

    def name(self) -> Text:
        return "action_check_local_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("city")
        if not city:
            response = requests.get(url, params)
        else:
            params['q'] = city
            response = requests.get(url, params)  

        print(response.status_code, params['q'] )

        if response.status_code == 200:
            res = response.json()
            city = response.json()['location']['name']
            loc_time = response.json()['location']['localtime']
            temperature = res['current']['temp_c']

            dispatcher.utter_message(text=f'Local time at {city} is {loc_time}')
            dispatcher.utter_message(text=f'And temperature is about {temperature} degrees Celsius')
        else: 
            dispatcher.utter_message(text=f'Не получили ответ с сервера((')

        return []

class ActionReceiveName(Action):

    def name(self) -> Text:
        return "action_receive_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print('Saving name slot')
        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"Я запомнил ваше имя {text}!")
        return [SlotSet("name", text)]

class ActionReceiveCity(Action):

    def name(self) -> Text:
        return "action_receive_city"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print('Saving city slot')
        city = tracker.latest_message['text']
        dispatcher.utter_message(text=f"Смотрим текущую погоду в {city}!")
        return [SlotSet("city", city)]


class ActionSayName(Action):

    def name(self) -> Text:
        return "action_say_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        if not name:
            dispatcher.utter_message(text="Я не знаю, как вас зовут")
        else:
            dispatcher.utter_message(text=f"Ваше имя {name}!")
        return []

class ActionCheckWhether(Action):

    def name(self) -> Text:
        return "action_check_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot('city')
        params['q'] = city
        response = requests.get(url, params)
        print(response.status_code)
        res = response.json()
        city = response.json()['location']['name']
        loc_time = response.json()['location']['localtime']
        temperature = res['current']['temp_c']

        dispatcher.utter_message(text=f'Local time at {city} is {loc_time}')
        dispatcher.utter_message(text=f'And temperature is about {temperature} degrees Celsius')

        return []

