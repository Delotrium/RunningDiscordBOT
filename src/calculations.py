import discord
from discord.ext import commands

numlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]

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
            await ctx.send(f"Conversions for {ctx.author.mention}:\n{query} can be converted to the following (3dp):\nMiles = {miles}mi\nMetres = {metres}m\nFeet = {ft}ft\nNautical Miles = {nm}nm\nYards = {yrd}yrd")
        elif query.lower().__contains__("mi"):
            amount = float(query[:-2])
            km = round(amount * 1.6093, 3)
            metres = round(amount*1609.344,3) 
            ft = round(amount * 5280,3)
            nm = round(amount * 0.869,3)
            yrd = round(amount * 1760,3)
            await ctx.send(f"Conversions for {ctx.author.mention}:\n{query} can be converted to the following (3dp):\nKilometres = {km}km\nMetres = {metres}m\nFeet = {ft}ft\nNautical Miles = {nm}nm\nYards = {yrd}yrd")
        elif query.lower().__contains__("ft"):
            amount = float(query[:-2])
            km = round(amount /3280.8399, 3)
            metres = round(amount/3.2808399,3) 
            mi = round(amount /5280,3)
            nm = round(amount / 6076.11549,3)
            yrd = round(amount /3,3)
            await ctx.send(f"Conversions for {ctx.author.mention}:\n{query} can be converted to the following (3dp):\nKilometres = {km}km\nMetres = {metres}m\nMiles = {mi}mi\nNautical Miles = {nm}nm\nYards = {yrd}yrd")

def setup(client):
    client.add_cog(Calculator(client))
