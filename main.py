import dotenv
import math
import sys
from datetime import datetime, date

from nextcord.types import activity
import nextcord.client
import nextcord.abc
import nextcord.types.activity
import nextcord.ext.commands
from nextcord.abc import Snowflake
from nextcord.ext import commands
import nextcord.abc

from version import *

intents = nextcord.Intents.all()

bot = commands.Bot(command_prefix=["$", "\$"], intents=intents)

@bot.command(
    aliases=["getping"],
    help="Returns the ping"
)
async def ping(ctx: commands.context.Context):
    await ctx.send("Pong!\nLatency is " + str(math.floor(bot.latency * 1000) / 1000) + " seconds")

@bot.command()
async def thing(ctx: commands.context.Context):
    await ctx.send('sure')

@bot.command(aliases=["version"])
async def about(ctx: commands.context.Context):
    embed = nextcord.Embed(title = f"About {bot.user.name}", description = format ("""
Running on {0}
Python {1}
Nextcord {2}
    """.format (
        getOSVersion(),
        getPythonVersion(),
        getNextcordVersion()
    )),
    color = nextcord.Colour(0x0088FF)
    )
    
    #embed.set_image(url=f"{bot.user.display_avatar.url}?size=64")
    
    await ctx.send( embed=embed )

bot.remove_command("help") # Remove default help command

@bot.command()
async def help(ctx: commands.context.Context, commandname: str = ""):
    if commandname == "":
        helpstr = ""
        for command in bot.commands:
            if command.name == "help":
                continue
            if len(command.aliases) != 0:
                helpstr += f" - **{command.name}, aliases: ({' | '.join(command.aliases)})**\n"
            else:
                helpstr += f" - **{command.name}**\n"
        embed = nextcord.Embed(
            title = "Commands:",
            description = helpstr,
            color = nextcord.Colour(0x0088FF)
        )
        await ctx.send(embed=embed)
    else:
        helpcommand = None
        for command in bot.commands:
            if command.name == commandname:
                helpcommand = command
            else:
                for alias in command.aliases:
                    if alias == commandname:
                        helpcommand = command
        
        if helpcommand != None:
            embed = nextcord.Embed(
                title = f"Command {helpcommand.name}:",
                description = helpcommand.help,
                color = nextcord.Colour(0x0088FF)
            )
            await ctx.send(embed=embed)
        else:
            embed = nextcord.Embed(
                title = f"Command not found",
                description = "This command doesn't exist, or you might have misspelled it",
                color = nextcord.Colour(0x0088FF)
            )
            await ctx.send(embed=embed)

@bot.command(aliases=["codeformat"])
async def format(ctx: commands.context.Context):
    embed = nextcord.Embed(title = f"How to format code", description = """
Use
\\`\\`\\`<language>

\\`\\`\\`
this will result in
```
print("Hello world!")
```
add syntax highlighting by replacing <language> with for example, for python: python
```python
print("Hello world!")
```
this was achieved by typing
\\`\\`\\`python
print("Hello world!")
\\`\\`\\`
    """
    ,
    color = nextcord.Colour(0x0088FF)
    )
    
    await ctx.send( embed=embed )

@bot.event
async def on_ready():
    print("Bot ready")

    presence = nextcord.Activity()
    presence.application_id = 945283628018057287
    presence.name = "Lmaxplay's server"
    presence.url = "https://example.org"
    presence.type = nextcord.ActivityType.watching
    presence.buttons = nextcord.types.activity.ActivityButton()

    await bot.change_presence(status=nextcord.Status.online, activity=presence)

    embed = nextcord.Embed(color=nextcord.Colour(0xFF0000), title="Started", description="```py\n" + str("Started up MaxBot") + "\n```")
    #await bot.get_guild(945283628018057287).get_channel(945283628018057290).send(embed=embed)

@bot.event
async def on_typing(channel: nextcord.abc.Messageable, user: nextcord.User, when: datetime):
    # print("User " + user.name + " started typing")
    return

@bot.event
async def on_message(message: nextcord.Message):
    if message.author.bot:
        return
    #   await message.channel.send(message.content[::-1])
    await bot.process_commands(message)
    return

@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.errors.CommandNotFound):
        embed = nextcord.Embed(color=nextcord.Colour(0xFF0000), title="Command not found") #,  description=f"Command  not found")
        await ctx.send(embed=embed)
        return
    embed = nextcord.Embed(color=nextcord.Colour(0xFF0000), title="An error occured", description="```py\n" + str(error) + "\n```")
    await ctx.send(embed=embed)
    await ctx.message.add_reaction("⚠️")


bot.run(dotenv.get_key(".env", "TOKEN"))
