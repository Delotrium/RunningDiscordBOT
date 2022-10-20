import discord
from discord.ext import commands

class Running(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["depends"])
    async def depend(self, ctx, member :discord.Member):
        await ctx.send(f"{member.mention} you have been pinged by {ctx.author.mention} because what you said or asked cannot be objectively proven or answered. This probably means that you have asked a very vague or broad question which relies on multiple factors, such as age, sex, medical history, training volume, diet, and other information, which cannot be simplified to give an answer. In short, what might be a PR for one runner, might be a warmup for another runner. All of us in this server care more about percieved effort, than objective times. Asking if ``[x] is a good time for an [y] year old`` simply various too much between person to person for us to answer. For an approimation of what people around your age run, check out ``https://runbundle.com/tools/age-grading-calculator``; however this should be taken with a grain of salt. ")
 

    
async def setup(client):
    await client.add_cog(Running(client))