from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
import requests
from kivy.graphics import *
import requests
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.progressbar import ProgressBar
import time
import math

player_data = requests.get('https://api.slothpixel.me/api/players/need_not').json()
player_guild = requests.get('https://api.slothpixel.me/api/guilds/' + player_data['uuid']).json()

if "error" in player_guild:
    player_guild = {"tag": "", "tag_color": "", "name": "None"}

guild_tag = (player_guild['tag'] or "")

guild_tag_color = player_guild['tag_color']
guild_tag_color = guild_tag_color.replace("[", "&bl;").replace("]", "&br; ").replace("&0", "[color=000000]").replace("&1", "[color=0000AA]").replace("&2", "[color=00AA00]").replace("&3", "[color=00AAAA]").replace("&4", "[color=AA0000]").replace("&5", "[color=AA00AA]").replace("&6", "[color=FFAA00]").replace("&7", "[color=AAAAAA]").replace("&8", "[color=555555]").replace("&9", "[color=5555FF]").replace("&a", "[color=55FF55]").replace("&b", "[color=55FFFF]").replace("&c", "[color=FF5555]").replace("&d", "[color=FF55FF]").replace("&e", "[color=FFFF55]").replace("&f", "[color=FFFFFF]")


guild_tag = guild_tag.replace("&0", "[color=000000]").replace("&1", "[color=0000AA]").replace("&2", "[color=00AA00]").replace("&3", "[color=00AAAA]").replace("&4", "[color=AA0000]").replace("&5", "[color=AA00AA]").replace("&6", "[color=FFAA00]").replace("&7", "[color=AAAAAA]").replace("&8", "[color=555555]").replace("&9", "[color=5555FF]").replace("&a", "[color=55FF55]").replace("&b", "[color=55FFFF]").replace("&c", "[color=FF5555]").replace("&d", "[color=FF55FF]").replace("&e", "[color=FFFF55]").replace("&f", "[color=FFFFFF]")

guild_tag = "&bl;" + guild_tag + "&br;"
if guild_tag == "&bl;&br;": guild_tag = ""


rank = (player_data['rank_formatted'] or "").title()
rank = rank.upper()
rank = rank.replace("[", "&bl;").replace("]", "&br; ").replace("&0", "[color=000000]").replace("&1", "[color=0000AA]").replace("&2", "[color=00AA00]").replace("&3", "[color=00AAAA]").replace("&4", "[color=AA0000]").replace("&5", "[color=AA00AA]").replace("&6", "[color=FFAA00]").replace("&7", "[color=AAAAAA]").replace("&8", "[color=555555]").replace("&9", "[color=5555FF]").replace("&A", "[color=55FF55]").replace("&B", "[color=55FFFF]").replace("&C", "[color=FF5555]").replace("&D", "[color=FF55FF]").replace("&E", "[color=FFFF55]").replace("&F", "[color=FFFFFF]")

level = player_data['level']


quests = player_data['quests_completed']
quests = "{:,}".format(quests)
quests = 'Quests: ' + quests

karma = player_data['karma']
karma = "{:,}".format(karma)
karma = "Karma: " + karma

achievement_points = player_data['achievement_points']
achievement_points = "{:,}".format(achievement_points)
achievement_points = 'Achievement Points: ' + achievement_points



firstlogin = player_data['first_login']
lastlogin = player_data['last_login']

online_offline = "[color=55FF55]Playing: " + player_data['last_game'] if player_data["online"] else "[color=FF5555]Status: Offline"

bw_losses = "{:,}".format(player_data['stats']['BedWars']['losses'])
bw_losses = "Losses: " + bw_losses
bw_wins = "{:,}".format(player_data['stats']['BedWars']['wins'])
bw_wins = "Wins: " + bw_wins


#try:
#    bw_wins = player_data['stats']['BedWars']['wins']
#except KeyError:
#    bw_wins = 0


rank_raw = player_data['rank']
if rank_raw == "HELPER": lastlogin = 1
if rank_raw == "ADMIN": lastlogin = 1
if rank_raw == "MODERATOR": lastlogin = 1

firstlogin = firstlogin/1000
firstlogin = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(firstlogin))


lastlogin = lastlogin/1000
lastlogin = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(lastlogin))

if lastlogin == "Wed, 31 Dec 1969 16:00:00": lastlogin = "Unknown"

image_url = "https://crafatar.com/renders/body/"  + player_data['uuid'] + "?overlay"

playerhead = requests.get(image_url)


with open("images/playerbody.png",'wb') as f:

    f.write(playerhead.content)


Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'window_state', 'maximized')
Config.set('graphics', 'boarderless', 1)
Config.set('graphics', 'minimum_width', 1000)
Config.set('graphics', 'minimum_height', 650)


class ScreenFour(Screen):
    pass

class ScreenThree(Screen):
    pass

class ScreenTwo(Screen):
    pass

class ScreenOne(Screen):
    pass

class Manager(ScreenManager):

    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)
    screen_four = ObjectProperty(None)

class HypicklePanel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Hypicklepanel(App):
    def build(self):
        self.rank_name = '[font=fonts/mcfont.otf]' + rank + player_data['username'] + ' ' + guild_tag_color + guild_tag + '[/font]'
        self.level = level % 1
        self.level_format = "[color=55FF55][font=fonts/mcfont.otf]" + str(math.floor(level))
        self.quests = quests
        self.ap = achievement_points
        self.karma = karma
        self.guild = "Guild: " + player_guild['name']
        self.firstlogin = "First Login: " + firstlogin
        self.lastlogin = "Last Login: " + lastlogin
        self.online = online_offline
        self.bw_wins = bw_wins
        self.bw_losses = bw_losses
        return HypicklePanel()

if __name__ =='__main__':
    Hypicklepanel().run()
