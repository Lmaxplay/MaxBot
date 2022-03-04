import nextcord
import nextcord.client
import dotenv
from nextcord.ext import commands

bot = commands.Bot(command_prefix="$")

@bot.command()
async def ping(ctx: commands.context.Context):
    await ctx.send("Pong!\n" + bot.latency)

bot.run(dotenv.get_key(".env", "TOKEN"))