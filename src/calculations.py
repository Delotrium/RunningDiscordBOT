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
        elif query.lower().__contains__("m") and not query.lower().__contains__("nm"):
            amount = float(query[:-1])
            km = round(amount /1000, 3)
            ft = round(amount*3.2808399, 3) 
            mi = round(amount /1609.344, 3)
            nm = round(amount / 1852,3)
            yrd = round(amount * 1.0936133,3)
            await ctx.send(f"Conversions for {ctx.author.mention}:\n{query} can be converted to the following (3dp):\nKilometres = {km}km\nFeet = {ft}ft\nMiles = {mi}mi\nNautical Miles = {nm}nm\nYards = {yrd}yrd")
        elif query.lower().__contains__("nm"):
            amount = float(query[:-2])
            km = round(amount *1.852, 3)
            ft = round(amount*6076.11549, 3) 
            mi = round(amount *1.15077945, 3)
            m = round(amount * 1852, 3)
            yrd = round(amount * 2025.3718,3)
            await ctx.send(f"Conversions for {ctx.author.mention}:\n{query} can be converted to the following (3dp):\nKilometres = {km}km\nFeet = {ft}ft\nMiles = {mi}mi\nMetres = {m}m\nYards = {yrd}yrd")
        elif query.lower().__contains__("yrd"):
            amount = float(query[:-3])
            km = round(amount /1093.6133, 3)
            ft = round(amount*3, 3) 
            mi = round(amount / 1760, 3)
            m = round(amount * 0.9144, 3)
            nm = round(amount / 2025.37183,3)
            await ctx.send(f"Conversions for {ctx.author.mention}:\n{query} can be converted to the following (3dp):\nKilometres = {km}km\nFeet = {ft}ft\nMiles = {mi}mi\nMetres = {m}m\nNautical Miles = {nm}nm")

async def setup(client):
    await client.add_cog(Calculator(client))