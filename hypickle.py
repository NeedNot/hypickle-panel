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
import itertools
import sys
import getopt, sys

playername = str(sys.argv[1])

player_data = requests.get('https://api.slothpixel.me/api/players/' + playername).json()

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


quests = '[color=5555FF][b]Quests [/b]: ' + "{:,}".format(player_data['quests_completed'])

karma = "[color=FF55FF][b]Karma: [/b]" + "{:,}".format(player_data['karma'])

achievement_points = '[color=55FFFF][b]Achievement Points: [/b]' + "{:,}".format(player_data['achievement_points'])




firstlogin = player_data['first_login']
lastlogin = player_data['last_login']

online_offline = "[color=55FF55]Playing: " + player_data['last_game'] if player_data["online"] else "[color=FF5555]Status: Offline"

bw_losses = "{:,}".format(player_data['stats']['BedWars']['losses'])
bw_losses = "" + bw_losses
bw_wins = "{:,}".format(player_data['stats']['BedWars']['wins'])
bw_wins = "" + bw_wins


#try:
#    bw_wins = player_data['stats']['BedWars']['wins']
#except KeyError:
#    bw_wins = 0


if player_data['rank'] == "HELPER": lastlogin = 1000
if player_data['rank'] == "ADMIN": lastlogin = 1000
if player_data['rank'] == "MODERATOR": lastlogin = 1000

firstlogin = firstlogin/1000
firstlogin = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(firstlogin))


lastlogin = lastlogin/1000
lastlogin = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(lastlogin))

if player_data['rank'] == "HELPER": lastlogin = 1
if player_data['rank'] == "ADMIN": lastlogin = 1
if player_data['rank'] == "MODERATOR": lastlogin = 1

if lastlogin == 1: lastlogin = "Unknown"

image_url = "https://crafatar.com/renders/body/"  + player_data['uuid'] + "?overlay"

playerhead = requests.get(image_url)


with open("images/playerbody.png",'wb') as f:

    f.write(playerhead.content)


bw_level = player_data['stats']['BedWars']['level']
if (bw_level < 100):
    bw_prestige = "stone"

if (bw_level >= 100):
    bw_prestige = "iron"

if (bw_level >= 200):
    bw_prestige = "gold"

if (bw_level >= 300):
    bw_prestige = "diamond"

if (bw_level >= 400):
    bw_prestige = "emerald"

if (bw_level >= 500):
    bw_prestige = "sapphire"

if (bw_level >= 600):
    bw_prestige = "ruby"

if (bw_level >= 700):
    bw_prestige = "crystal"

if (bw_level >= 800):
    bw_prestige = "opal"

if (bw_level >= 900):
    bw_prestige = "amethyst"

if (bw_level >= 1000):
    bw_prestige = "rainbow"

bw_level = str(bw_level)
colors = ['FFAA00','FFFF55','55FF55','55FFFF','FF55FF','AA00AA']

def color_level(score):
    result = ''
    for digit, color in zip(str(bw_level),itertools.cycle(colors)):
        result += f'[color={color}]{digit}'
    return result

bw_level = (color_level(1000))

if bw_prestige == "stone":
    bw_level = "[color=AAAAAA]" + '&bl;' + str(player_data['stats']['BedWars']['level']) + '[font=fonts/seguisym]\u272b[/font]&br;'

if bw_prestige == "iron":
    bw_level = "[color=FFFFFF]" + '&bl;' + str(player_data['stats']['BedWars']['level']) + '[font=fonts/seguisym]\u272b[/font]&br;'

if bw_prestige == "gold":
    bw_level = "[color=FFAA00]" + '&bl;' + str(player_data['stats']['BedWars']['level']) + '[font=fonts/seguisym]\u272b[/font]&br;'

if bw_prestige == "diamond":
    bw_level = "[color=55FFFF]" + '&bl;' + str(player_data['stats']['BedWars']['level']) + '[font=fonts/seguisym]\u272b[/font]&br;'

if bw_prestige == "emerald":
    bw_level = "[color=00AA00]" + '&bl;' + str(player_data['stats']['BedWars']['level']) + '[font=fonts/seguisym]\u272b[/font]&br;'

if bw_prestige == "sapphire":
    bw_level = "[color=00AAAA]" + '&bl;' + str(player_data['stats']['BedWars']['level']) + '[font=fonts/seguisym]\u272b[/font]&br;'

if bw_prestige == "ruby":
    bw_level = "[color=AA0000]" + '&bl;' + str(player_data['stats']['BedWars']['level']) + '[font=fonts/seguisym]\u272b[/font]&br;'

if bw_prestige == "crystal":
    bw_level = "[color=FF55FF]" + '&bl;' + str(player_data['stats']['BedWars']['level']) + '[font=fonts/seguisym]\u272b[/font]&br;'

if bw_prestige == "opal":
    bw_level = "[color=5555FF]" + '&bl;' + str(player_data['stats']['BedWars']['level']) + '[font=fonts/seguisym]\u272b[/font]&br;'

if bw_prestige == "amethyst":
    bw_level = "[color=AA00AA]" + '&bl;' + str(player_data['stats']['BedWars']['level']) + '[font=fonts/seguisym]\u272b[/font]&br;'

if bw_prestige == "rainbow":
    bw_level = '[color=FF5555]&bl;[/color]' + str(bw_level) + '[color=FF55FF][font=fonts/seguisym]\u272b[/font][color=AA00AA]&br;'
bw_level = "[b]Level: [/b]" + bw_level

Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'window_state', 'maximized')
Config.set('graphics', 'boarderless', 1)
Config.set('graphics', 'minimum_width', 1000)
Config.set('graphics', 'minimum_height', 650)

class ScreenFive(Screen):
    pass

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
    screen_five = ObjectProperty(None)

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
        self.guild = "[color=00AA00][b]Guild: [/b]" + player_guild['name']
        self.firstlogin = "[b]First Login:[/b] " + firstlogin
        self.lastlogin = "[b]Last Login[/b]: " + lastlogin
        self.online = online_offline
        self.bw_wins = "" + "{:,}".format(player_data['stats']['BedWars']['wins'])
        self.bw_losses = "" + "{:,}".format(player_data['stats']['BedWars']['losses'])
        self.bw_w_l = "" + "{:,}".format(player_data['stats']['BedWars']['w_l'])
        self.bw_final_kills = "" + "{:,}".format(player_data['stats']['BedWars']['final_kills'])
        self.bw_final_deaths = "" + "{:,}".format(player_data['stats']['BedWars']['final_deaths'])
        self.bw_final_k_d = "" + "{:,}".format(player_data['stats']['BedWars']['final_k_d'])
        self.emeralds = "[color=00AA00]" + "{:,}".format((player_data['stats']['BedWars']['resources_collected']['emerald']))
        self.diamonds = "[color=55FFFF]" + "{:,}".format((player_data['stats']['BedWars']['resources_collected']['diamond']))
        self.gold = "[color=FFAA00]" + "{:,}".format((player_data['stats']['BedWars']['resources_collected']['gold']))
        self.iron = "[color=737373]" + "{:,}".format((player_data['stats']['BedWars']['resources_collected']['iron']))
        self.coins = "[color=FFAA00][b]Coins: [/b]" + "{:,}".format((player_data['total_coins']))
        self.wins = "[color=00AA00][b]Wins: [/b]" + "{:,}".format((player_data['total_wins']))
        self.kills = "[color=AA0000][b]Kills: [/b]" + "{:,}".format((player_data['total_kills']))
        self.bw_winstreak = "[color=5555FF][b]Winstreak: [/b]" + "{:,}".format((player_data['stats']['BedWars']['winstreak']))
        self.bw_coins = "[color=FFAA00][b]Coins: [/b]" + "{:,}".format((player_data['stats']['BedWars']['coins']))
        self.bw_level = bw_level
        self.bw_loot_boxes = "[b][color=AA00AA]Loot Boxes:[/b] [color=FF5555]" + "{:,}".format(player_data['stats']['BedWars']['boxes']['current'])
        self.bw_kills_all = "[b]Kills:[/b] " + "{:,}".format(player_data['stats']['BedWars']['kills'])
        self.bw_deaths_all = "[b]Deaths:[/b] " + "{:,}".format(player_data['stats']['BedWars']['deaths'])
        self.bw_k_d_all = "[b]K/D R:[/b] " + "{:,}".format(player_data['stats']['BedWars']['k_d'])
        self.bw_final_kills_all = "[b]Final Kills:[/b] " + "{:,}".format(player_data['stats']['BedWars']['final_kills'])
        self.bw_final_deaths_all = "[b]Final Deaths:[/b] " + "{:,}".format(player_data['stats']['BedWars']['final_deaths'])
        self.bw_final_k_d_all = "[b]Final K/D R:[/b] " + "{:,}".format(player_data['stats']['BedWars']['final_k_d'])
        self.bw_beds_broken = "[b]Beds Broken:[/b] " + "{:,}".format(player_data['stats']['BedWars']['beds_broken'])
        self.bw_beds_lost = "[b]Beds Lost:[/b] " + "{:,}".format(player_data['stats']['BedWars']['beds_lost'])
        self.bw_beds_b_l = "[b]Beds B/L R:[/b] " + "{:,}".format(player_data['stats']['BedWars']['bed_ratio'])
        self.bw_wins = "[b]Wins:[/b] " + "{:,}".format(player_data['stats']['BedWars']['wins'])
        self.bw_losses = "[b]Losses:[/b] " + "{:,}".format(player_data['stats']['BedWars']['losses'])
        self.bw_w_l = "[b]W/L R:[/b] " + "{:,}".format(player_data['stats']['BedWars']['w_l'])
        return HypicklePanel()

if __name__ =='__main__':
    Hypicklepanel().run()
