import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents().all() 
client = commands.Bot(command_prefix='r!', intents=intents)


@client.command()
async def load(ctx, extension):
    await client.load_extension(f"src.{extension}")

@client.command()
async def unload(ctx, extension):
    await client.unload_extension(f"src.{extension}")

async def load_extensions():
    for filename in os.listdir("./src"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"src.{filename[:-3]}")


async def main():
    async with client:
        await load_extensions()
        await client.start('')

asyncio.run(main())
