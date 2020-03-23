from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.graphics import *
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import requests
from kivy.properties import StringProperty

Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 600)
Config.set('graphics', 'borderless', 1)




class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Login(App):
  playername = StringProperty()
  def build(self):
    self.playername = ''
    return LoginScreen()
  def enter_key():
      app.stop()



if __name__ =='__main__':
    Login().run()
app = App.get_running_app()

print(app.playername)
player = requests.get('https://api.slothpixel.me/api/players'+ app.playername).json()

print(player['error'])
