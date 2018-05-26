import discord
from discord.ext import commands
import math
import random

# discord.py calls groups of commands cogs
# cogs can also be handlers for different types of events
# and respond to changes in data as they happen

# setup
from typing import Any


class RPSCog:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        print(message.content)
    
    # rps command
    @commands.command()
    async def rps(self, ctx, userChoice):
        # starts a rock paper scissors game
        await ctx.send("Starting RPS!")
        #temporary random testing stuffs
        #randomNumber = random.randint(0,2)
        #print(randomNumber)
        #userChoice = choices[randomNumber]

        # get user input... BUT HOW?!?!?!
        #await ctx.send("Choose your fighter: Rock, Paper, or Scissors")
        #print(ctx.kwargs)
        #userChoice = ctx.message.content
        print(userChoice)
        userChoice = str(userChoice)
        print(userChoice)
        
        # choose bot sign (rock, paper, or scissors)
        choices = ['rock','paper','scissors']
        randomNumber = random.randint(0,2)
        #print(randomNumber)
        botChoice = choices[randomNumber]
        await ctx.send("I choose... hm..." + str(botChoice))
        
        # figure out who won
        winDict = {
            "scissors":"paper",
            "paper":"rock",
            "rock":"scissors",
            }
        await ctx.send("...and the winner is...")

        # Hardcoding for testing, deprecated until needed
        #userChoice = "rock"
        #botChoice = "scissors"
        
        # report winner- it's working!
        #print("finding winner")
        # making sure the user's choice is in the right format
        lowerUserChoice = str(userChoice.lower())  # type: String
        print(lowerUserChoice)
        print(userChoice)
        didIWin = winDict[lowerUserChoice]
        print(didIWin)
        if didIWin == botChoice:
            await ctx.send("Congrats, you win!")
        elif lowerUserChoice == botChoice:
            await ctx.send("It's a tie!")
        else:
            await ctx.send("Me! I, the bot, have won!")
        # end command
        await ctx.send("Thanks for playing")

# add this cog to the bot
def setup(bot):
    bot.add_cog(RPSCog(bot))
