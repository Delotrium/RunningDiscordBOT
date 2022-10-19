import discord
from discord.ext import commands

class Tools(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["pm"])
    async def dm(self, ctx, member : discord.Member, *, message):
        await member.send(message + f"\n ``From {ctx.author}``")
        Author = ctx.author
        await Author.send("\""+ message + f"\" was sent to {member}!")
        
async def setup(client):
    await client.add_cog(Tools(client))