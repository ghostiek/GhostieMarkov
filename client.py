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
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()
    with open(os.getcwd() + r"\data\token.txt") as file:
        content = file.read()
    bot.run(content, bot=True, reconnect=True)