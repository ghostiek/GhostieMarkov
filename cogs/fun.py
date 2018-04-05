from discord.ext import commands
import discord
import random
import urllib.request
import os


class FunCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "choose")
    async def ban(self, ctx, *, params:str):
        choice = random.choice(params.split(" "))
        await ctx.send("I pick " + choice)

    @commands.command(name = "cat")
    async def cat(self, ctx):
        url = 'https://thecatapi.com/api/images/get'
        dir = os.getcwd() + os.sep + "data" + os.sep + "cat.jpeg"
        urllib.request.urlretrieve(url, dir)
        await ctx.send(file = discord.File(dir))


def setup(bot):
    bot.add_cog(FunCog(bot))