import discord
from discord.ext import commands


class Calculator(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    ###
    #
    # Takes two values: kilometers and minutes
    #
    ###
    @commands.command(aliases=["calculate.pace"])
    async def pace(self, ctx, *, parms):
        try:
            values = parms.split(" ")
            
            if len(values) < 2:
                await ctx.send ("Pace requires two values for calculation: kilometers and minutes")
            else:
                print (float(values[0]))
                distance = float(values[0])
                time = float(values[1])

                pace = time / distance
                paceMiles = time / (distance * .62137)

                em = discord.Embed()

                # Format the EMBED
                c = discord.Color(0)
                em.set_author(name=ctx.message.author.display_name + " has requested a pace check.")

                em.title = "Pace Calculation"
                em.colour = c.orange()

                em.description = "Distance: " + str(distance) + " km\nTime: " + str(time) + " minutes\nPace (km): " + str(pace) + " minutes/km\nPace (m): " + str(round(paceMiles,1)) + " minutes/mile"

                await ctx.send(embed=em)
            
        except Exception as e:
            print ("An error occured: " + e)

    @commands.command(aliases=["convert.distance"])
    async def distance(self, ctx, *, query):
        
        # Set both as empty string types
        number = ""
        unit = ""

        # Parse the query and break out the unit of measure from the numeric value
        for letter in query:
            if letter.isnumeric():
                number = number + letter
            else:
                unit = unit + letter

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

def setup(client):
    client.add_cog(Calculator(client))
