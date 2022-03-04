import dotenv
import math
import sys
from datetime import datetime, date

import nextcord
import nextcord.client
from nextcord.ext import commands
import nextcord.abc

from version import getnextcordversion, getpythonversion

bot = commands.Bot(command_prefix=["$", "\$"])

@bot.command(aliases=["getping"])
async def ping(ctx: commands.context.Context):
    await ctx.send("Pong!\nLatency is " + str(math.floor(bot.latency * 1000) / 1000) + " seconds")

@bot.command()
async def thing(ctx: commands.context.Context):
    await ctx.send('sure')

@bot.command()
async def version(ctx: commands.context.Context):
    await ctx.send( content = format ("""
running on python {0}
and nextcord {1}
    """.format (
        getpythonversion(),
        getnextcordversion()
    )))
    _

bot.remove_command("help")

@bot.command()
async def help(ctx: commands.context.Context):
    await ctx.send("disabled")


@bot.event
async def on_ready():
    print("Bot ready")

@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    embed = nextcord.Embed(color=nextcord.Colour(0xFF0000), title="An error occured", description=error)
    await ctx.send(embed=embed)
    await ctx.message.add_reaction("⚠️")

@bot.event
async def on_typing(channel: nextcord.abc.Messageable, user: nextcord.User, when: datetime):
    return #print("User " + user.name + " started typing")

@bot.event
async def on_message(message: nextcord.Message):
    if message.author.bot:
        return
    await bot.process_commands(message)
    return


bot.run(dotenv.get_key(".env", "TOKEN"))