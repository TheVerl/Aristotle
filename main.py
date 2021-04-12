#!/usr/bin/env python3

# Import modules
import discord
from discord.ext import commands

# Global variables
client = discord.Client()
bot = commands.Bot(command_prefix="%")
prefix = bot.command_prefix

# Startup messages
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="with the pages"))
    with open ("discord.token") as f:
        token = f.read()
    f.close()
    print("We have logged in as {0.user}".format(bot))

# Pong!
@bot.command(name="ping")
async def testCommand(ctx):
    await ctx.channel.send("pong!")
    print("Command executed succesfully.")

# Initialisation.
def init():
    with open("discord.token") as f:
        token = f.read()
    f.close()
    bot.run(token)

if __name__ == '__main__':
    print("Loading...")
    init()