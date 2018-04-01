from discord.ext import commands
import os

class MineCog:
    def __init__(self, bot):
        self.bot = bot

    #Event that logs messages
    async def on_message(self, message):
        if "ghostie" in message.content or message.content.startswith("$") or message.author.bot:
            return
        with open(os.getcwd() + r"\data\responses.txt", "a") as file:
            try:
                file.write(message.content + "\n")
            except UnicodeEncodeError:
                print("Invalid Unicode")

    #Manually grabs the 100 last messages
    @commands.command(name = "get")
    async def gather_all_messages(self, ctx, limit = 100):
        channel = ctx.message.channel
        with open(os.getcwd() + "\data\responses.txt", "a") as file:
            async for i in channel.history(limit = limit):
                try:
                    file.write(i.content + "\n")
                except UnicodeEncodeError:
                    print("Invalid Unicode")

def setup(bot):
    bot.add_cog(MineCog(bot))