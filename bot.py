#import
import hikari
import lightbulb
import os
import aiohttp
import concurrent.futures
from random import choice
from lightbulb.ext import tasks


#put your token discord here
bot = lightbulb.BotApp(token='TOKEN')

#run commands folder
bot.load_extensions_from('./commands')

#running discord
bot.run()
