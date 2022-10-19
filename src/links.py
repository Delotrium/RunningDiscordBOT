import discord
from discord.ext import commands

class Link(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['link.youtube'])
    async def link_youtube(self, ctx):
        await ctx.send(f'{ctx.author.mention}: https://www.youtube.com')
    
    @commands.command()
    async def link(self, ctx, *, query):
        await ctx.send(f'{ctx.author.mention}: https://{query}.com')

async def setup(client):
    await client.add_cog(Link(client))