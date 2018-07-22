from discord.ext import commands
import discord
import random
import urllib.request
import urllib.error
import os
import numpy as np
from keras.preprocessing import image
from keras.models import load_model

class FunCog:
    def __init__(self, bot):
        self.bot = bot
        path = os.getcwd() + os.sep + "data" + os.sep + 'myfirstalgo.h5'
        self.classifier = load_model(path)

    @commands.command(name = "choose")
    async def ban(self, ctx, *, params:str):
        choice = random.choice(params.split(","))
        await ctx.send("I pick " + choice)

    @commands.command(name = "cat")
    async def cat(self, ctx):
        url = 'https://thecatapi.com/api/images/get'
        dir = os.getcwd() + os.sep + "data" + os.sep + "cat.jpeg"
        urllib.request.urlretrieve(url, dir)
        await ctx.send(file = discord.File(dir))

    @commands.command(name="test")
    async def test(self, ctx):
        await ctx.send(str(ctx.author.id))

    @commands.command(name="detect")
    async def detect(self, ctx, photo_url):
        #Download it
        dir = os.getcwd() + os.sep + "data" + os.sep + "test.jpeg"
        try:
            urllib.request.urlretrieve(photo_url, dir)
        except urllib.error.HTTPError as e:
            print("HTTP Error " + str(e.code) + ": " + e.msg)
            await ctx.send("Something went wrong")
            return

        test_image = image.load_img(dir, target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = self.classifier.predict(test_image)
        if result[0][0] == 1:
            prediction = 'dog'
            await ctx.send(prediction)
        else:
            prediction = 'cat'
            await ctx.send(prediction)


def setup(bot):
    bot.add_cog(FunCog(bot))