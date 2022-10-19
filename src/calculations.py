import discord
from discord.ext import commands

class Calculator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["convert.distance"])
    async def distance(self, ctx, *, query):
        if query.lower().__contains__("km"):
            amount = float(query[:-2])
            miles = round(amount * 0.6214, 3)
            metres = round(amount*1000,3) 
            ft = round(amount * 3280.8399,3)
            nm = round(amount * 0.5399568,3)
            yrd = round(amount * 1093.6133,3)
            await ctx.send(f"Conversions for {ctx.author.mention}:\n{query} Kilometres can be converted to the following (3dp):\nMiles = {miles}mi\nMetres = {metres}m\nFeet = {ft}ft\nNautical Miles = {nm}nm\nYards = {yrd}yrd")

        


def setup(client):
    client.add_cog(Calculator(client))
