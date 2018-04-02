import discord
from discord.ext import commands
import sys
import traceback
import os

bot = commands.Bot(command_prefix='$')

extensions = ["cogs.admin",
              "cogs.mine",
              "cogs.talk"]

@bot.event
async def on_ready():
    print("\n\nLogged in as: " + bot.user.name + "-" + str(bot.user.id) + "\nVersion: " + str(discord.__version__)+"\n")
    print('Successfully logged in and booted...!')

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print("Failed to load extension " + extension, file=sys.stderr)
            traceback.print_exc()
    with open(os.getcwd() + "\\data\\token.txt") as file:
        content = file.read()
    bot.run(content, bot=True, reconnect=True)