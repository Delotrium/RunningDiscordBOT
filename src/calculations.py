import discord
from discord.ext import commands
import math


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

    @commands.command(aliases=["hr", "maxhr", "heartrate", "max_heartrate", "heartrate.max", "hr.max"])
    async def max_hr(self, ctx, age, gender="male"):
        age = float(age)
        TankaMonahanSeals = 208 - (0.7 * age)
        HaskellFox = 220-age
        RobergsLandwehr = 205.8 - (0.685 * age)
        if gender == "male" or gender == "men" or gender == "man":
            Gellish = 203.7/(1+math.exp(0.033*(age-104.3)))
        else:
            Gellish = 190.2/(1+math.exp(0.0453*(age-107.5)))
        LondereeMoeschberger = 206.3 -(0.711*age)
        Miller = 217 - (0.85*age)
        averageMaxHR = (TankaMonahanSeals + HaskellFox + Gellish + LondereeMoeschberger + Miller + RobergsLandwehr)/6
        embed = discord.Embed()
        colour = discord.Color.from_rgb(255, 0, 0)
        embed.set_author(name="RunBOT Physiologist")
        embed.title = "Max Heartrate Calculations"
        embed.colour = colour
        embed.description = "The list contains different maximum heart rate calculations and the averaging total of the calculations. NOTE; this is only a superficial mathematical calculation and may be greatly incorrect. These calculations are no replacement for laboratory calculations. "
        embed.add_field(name='Tanka, Monahan, and Seals Approximation', value=f"``{round(TankaMonahanSeals, 2)}bpm``", inline=False)
        embed.add_field(name='Haskell and Fox Approximation', value=f"``{round(HaskellFox, 2)}bpm``", inline=False)
        embed.add_field(name='Robergs and Landwehr Approximation', value=f"``{round(RobergsLandwehr,2)}bpm``", inline=False)
        embed.add_field(name='Gellish Approximation', value=f"``{round(Gellish,2)}bpm``", inline=False)
        embed.add_field(name='Londeree and Moeschberger Approximation', value=f"``{round(LondereeMoeschberger,2)}bpm``", inline=False)
        embed.add_field(name='Miller Approximation', value=f"``{round(Miller,2)}bpm``", inline=False)   
        embed.add_field(name=f'The average maximum heart rate for a {age} year old:', value=f"``{round(averageMaxHR)}bpm``", inline=False)   
        await ctx.send(f'{ctx.author.mention} - Heart Rate Calculations for a {age} year old {gender}\n', embed=embed) 
    
    @max_hr.error
    async def max_hr_error(self, ctx, error):
        await ctx.send(f"{ctx.author.mention} invalid command! To use this command use ``r!max_hr <age> <optional: gender (male by default)>``. Aliases for this command are ``r!hr``, ``r!maxhr``, ``r!heartrate``, ``r!max_heartrate``, ``r!heartrate.max``, and ``r!hr.max``.")

async def setup(client):
    await client.add_cog(Calculator(client))