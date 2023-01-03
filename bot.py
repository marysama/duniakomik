#import
import hikari
import lightbulb
import os
import aiohttp
import concurrent.futures
from random import choice
from lightbulb.ext import tasks


#token discord
bot = lightbulb.BotApp(token='MTAyNjM5NzY2NTE3ODY5MzY2Mg.G-a8R3.tBBNiEgMHzy2weQZxfBZxo6ajTHnxWTRvfY3yU')

#run commands folder
bot.load_extensions_from('./commands')

#running discord
bot.run()