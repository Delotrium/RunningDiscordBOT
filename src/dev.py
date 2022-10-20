import discord
from discord.ext import commands

class Development(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("The BOT is online! ")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong {ctx.author.mention}!')

async def setup(bot):
    await bot.add_cog(Development(bot))