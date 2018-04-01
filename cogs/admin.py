from discord.ext import commands
import client

class AdminCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "ban")
    async def ban(self, ctx):
        print("Here")
        await ctx.send("Works")

def setup(bot):
    bot.add_cog(AdminCog(bot))