import keep_alive
from discord.ext import commands
import os

#import all of the cogs
from music import music_cog

bot = commands.Bot(command_prefix='!')

#register the class with the bot

bot.add_cog(music_cog(bot))

#start the bot with our token
keep_alive.keep_alive()
bot.run(os.environ['token'])
