import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit=amount+1)


    @commands.command(aliases=['purge.all', 'clear.all'])
    @commands.has_permissions(manage_messages=True)
    async def clearall(self, ctx):
        await ctx.channel.purge()

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member :discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member} was just kicked for "{reason}"!')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member :discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member} was just banned for "{reason}"!')

def setup(client):
    client.add_cog(Moderation(client))
    
