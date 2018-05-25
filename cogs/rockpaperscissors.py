import discord
from discord.ext import commands
import math
import random

# discord.py calls groups of commands cogs
# cogs can also be handlers for different types of events
# and respond to changes in data as they happen

# setup
class RPSCog:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        print(message.content)
    
    # rps command
    @commands.command()
    async def rps(self, ctx):
        # starts a rock paper scissors game
        await ctx.send("Starting RPS!")
        # get user input... BUT HOW?!?!?!
        #temporary random testing stuffs
        choices = ['rock','paper','scissors']
        randomNumber = random.randint(0,2)
        print(randomNumber)
        userChoice = choices[randomNumber]
        #userChoice = prompt for input("Choose your fighter: Rock, Paper, or Scissors")
        print(userChoice)
        # choose bot sign (rock, paper, or scissors)
        randomNumber = random.randint(0,2)
        print(randomNumber)
        botChoice = choices[randomNumber]
        await ctx.send("I choose... hm..." + botChoice)
        
        # figure out who won
        winDict = {
            "scissors":"paper",
            "paper":"rock",
            "rock":"scissors",
            }
        await ctx.send("...and the winner is...")

        # Hardcoding for testing
        userChoice = "rock"
        botChoice = "scissors"
        
        # report winner
        print("finding winner")
        lowerUserChoice = userChoice.lower()
        print(lowerUserChoice)
        didIWin = winDict.get(lowerUserChoice)
        print(didIWin)
        if didIWin == botChoice:
            await ctx.send("Congrats, you win!")
        elif str(lowerUserChoice) == botChoice:
            await ctx.send("It's a tie!")
        else:
            await ctx.send("PracticeBot wins!")
        # end command
        await ctx.send("Thanks for playing")

# add this cog to the bot
def setup(bot):
    bot.add_cog(RPSCog(bot))
