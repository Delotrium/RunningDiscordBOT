import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

class Soup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["define.urban", 'urban', 'search.urban', 'uban.dictionary'])
    async def define_urban(self, ctx, *, query):
        url = f"https://www.urbandictionary.com/define.php?term={query}"
        
        result=requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        try:
            article = doc.find('div', class_="meaning").text
            await ctx.send(f"{ctx.author.mention}, The definition of {query} on the urban dictionary is:\n{article}")
        except (TypeError, AttributeError):
            await ctx.send(f"{ctx.author.mention}:\n We could not find \"{query}\" on the urban dictionary!")

    @commands.command(aliases=["def", 'meaning', 'mean'])
    async def define(self, ctx, *, query):
        url = f"https://www.dictionary.com/browse/{query}"
        
        result=requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        class_parse = "css-10ul8x e1q3nk1v2"
        try:
            article = doc.find('div', class_=class_parse).text
            await ctx.send(f"{ctx.author.mention}, The definition of {query} in the dictionary is:\n{article}")
        except (TypeError, AttributeError):
            await ctx.send(f"{ctx.author.mention}:\n We could not find \"{query}\" in the dictionary!")


async def setup(client):
    await client.add_cog(Soup(client))
