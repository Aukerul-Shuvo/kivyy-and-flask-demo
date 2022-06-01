from cgitb import text
import requests
import json

from tomlkit import string
import kivy
from kivy.app import App
from kivy.uix.label import Label


# Replace this with your
# current version
kivy.require('1.11.1')

active_case= []
dataa= []
parse_json= []
# Defining a class
class MyFirstKivyApp(App):

    # response_API = requests.get('http://127.0.0.1:5000')
    # dataa = response_API.text
    # print(dataa)
    # parse_json = json.loads(dataa)
    # active_case = parse_json[0]
    def build(self):
        listt= requests.get('http://127.0.0.1:5000')
        dataa = listt.text
        return Label(text= dataa)		


# Here our class is initialized
# and its run() method is called.
# This initializes and starts
# our Kivy application.
MyFirstKivyApp().run()			





