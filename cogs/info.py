import discord
from discord.ext import commands

# Lil info cog to let folks know about this bot

# setup
class InfoCog:
    def __init__(self, bot):
        self.bot = bot

    # info command
    @commands.command()
    async def info(self, ctx):
        #gives info about the bot to the user
        await ctx.send("Hi, I'm Practice-Bot, use >help to find out what I can do!")

#add to bot
def setup(bot):
    bot.add_cog(InfoCog(bot))

