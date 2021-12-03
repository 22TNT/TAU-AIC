import json

import discord
from discord.ext import commands

import secret

PREFIX = "!"
TOKEN = secret.token
RIGHT_CODE = "94026501"
LOCATION_FILE = "InSearchOfARescue.json"
with open(LOCATION_FILE, "r", encoding="utf-8") as json_file:
    LOCATION_DATA = json.load(json_file)

bot = commands.Bot(command_prefix=PREFIX)
bot.remove_command("help")


@bot.command()
async def check(ctx, *args):
    if not args or args[0] not in LOCATION_DATA.keys():
        await ctx.send("Use !list to get a list of all places and commands")
    else:
        args = args[0]
        await ctx.send("```\n" + LOCATION_DATA[args] + "\n```")


@bot.command()
async def safe(ctx, code):
    if code != RIGHT_CODE:
        await ctx.send("```\n" + "Вы пытаетесь открыть сейф, но он не поддается. Видимо, код не тот.\n" + "```")
    else:
        await ctx.send("```\n" + "Открыв сейф, вы находите какой-то непонятный ключ, причем довольно больших габаритов."
                                 " Он висит в связке с брелком в виде поезда.\n" + "```")


@bot.command()
async def help(ctx):
    s = " "
    for key in LOCATION_DATA.keys():
        s += key + "\n" + " "
    await ctx.send("```\n" + "Локации для !check:\n" + s + "!safe CODECODE\n " + "```")


@bot.event
async def on_command_error(ctx):
    await ctx.send("Используйте !help.")


bot.run(TOKEN)
