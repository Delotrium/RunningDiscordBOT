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

    @commands.command(aliases=["music.cadence", "180bpm", "180", "cadence.music"])
    async def cadence_music(self, ctx):
        await ctx.send(f'{ctx.author.mention} the following playlist contains 180bpm music for cadence runs:\nhttps://open.spotify.com/playlist/5ymkuBk3C1Iu4KTdJBK9vy?si=28300f76ef9744e7\n**Personalised Version 180BPM mix**: https://open.spotify.com/playlist/37i9dQZF1EIerWUrjG2OiJ')

async def setup(client):
    await client.add_cog(Link(client))