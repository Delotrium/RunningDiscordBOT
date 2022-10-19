import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='r!')


@client.command()
async def load(ctx, extension):
    client.load_extension(f"src.{extension}")

@client.command()
async def   unload(ctx, extension):
    client.unload_extension(f"src.{extension}")

for filename in os.listdir('./src'):
    if filename.endswith('.py'):
        client.load_extension(f"src.{filename[:-3]}")



client.run("")
