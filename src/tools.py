import discord
from discord.ext import commands

class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["pm"])
    async def dm(self, ctx, member : discord.Member, *, message):
        await member.send(message + f"\n ``From {ctx.author}``")
        Author = ctx.author
        await Author.send("\""+ message + f"\" was sent to {member}!")
        
async def setup(bot):
    await bot.add_cog(Tools(bot))