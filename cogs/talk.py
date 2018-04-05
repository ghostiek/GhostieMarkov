from Markov import markov

class TalkCog:
    def __init__(self, bot, chain):
        self.bot = bot
        self.chain = chain

    async def on_message(self, message):
        if "ghostie" in message.content.lower() or self.bot.user.mentioned_in(message) and not message.author.bot :
            mes = markov.generate_message(message, self.chain)
            await message.channel.send(mes)

def setup(bot):
    bot.add_cog(TalkCog(bot, markov.build_chain(markov.read_file("responses"))))