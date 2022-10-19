import discord
from discord.ext import commands

class Development(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("The BOT is online! ")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong {ctx.author.mention}!')

async def setup(client):
    await client.add_cog(Development(client))