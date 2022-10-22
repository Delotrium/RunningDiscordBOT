import discord
from discord.ext import commands, tasks
import os
import asyncio


intents = discord.Intents().all() 
intents.message_content = True
bot = commands.Bot(command_prefix='r!', intents=intents)



@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"src.{extension}")

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"src.{extension}")

async def load_extensions():
    for filename in os.listdir("./src"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"src.{filename[:-3]}")


async def main():
    secret_token = os.environ.get('BOT_TOKEN', '')
    async with bot:
        await load_extensions()
        await bot.start(secret_token)
discord.utils.setup_logging()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Bonking Simulator'))

asyncio.run(main())

