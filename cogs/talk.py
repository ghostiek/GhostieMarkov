from Markov import markov
from discord.ext import commands

class TalkCog:
    def __init__(self, bot, chain):
        self.bot = bot
        self.chain = chain

    async def on_message(self, message):
        if not "ghostie" in message.content.lower() or message.author.bot:
            return
        mes = markov.generate_message(self.chain)
        await message.channel.send(mes)

def setup(bot):
    bot.add_cog(TalkCog(bot, markov.build_chain(markov.read_file("responses"))))