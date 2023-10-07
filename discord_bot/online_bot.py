import discord
from discord import app_commands
from discord.ext import commands
import json
from server_online import online_check, ping_check

file = open("config.json", 'r')
config = json.load(file)

bot = commands.Bot(command_prefix=config['prefix'], intents=discord.Intents.all())


@bot.event
async def on_ready():
    await bot.tree.sync()


@bot.tree.command(name="online", description="Узнать онлайн на выбраном сервере")
@app_commands.describe(ip="Ip сервера")
async def online(interaction: discord.Interaction, *, ip: str=config['default_ip']):
    await interaction.response.send_message(f"Онлайн на сервере {ip} \t:\t {online_check(ip)}")


# @bot.tree.command(name="ping", description="Узнать пинг на выбраном сервере")
# @app_commands.describe(ip="Ip сервера")
# async def online(interaction: discord.Interaction, *, ip: str=config['default_ip']):
#     await interaction.response.send_message(f"Пинг на сервере {ip} : {ping_check(ip)} ms")


bot.run(config['token'])
