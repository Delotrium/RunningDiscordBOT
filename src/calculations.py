from datetime import timedelta
import discord
from discord.ext import commands
import math
from src.common import Q_, U_
from src.common.fmt import fmt_delta, fmt_qty
from src.common.calc import convert, pace, even_splits
from src.common.parse import parse_quantity, parse_time_to_seconds, parse_time_to_timedelta
import logging

logger = logging.getLogger(__name__)

class Calculator(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["splits", "split"])
    async def compute_splits(self, ctx, *, qry):
        """ Like pace, but produces splits
        Ussage:
            r!splits time distance [unit]
        """
        try:
            tokens = qry.split()
            if len(tokens) not in (2, 3):
                pass
            unit = 'mile' if len(tokens) == 3 and tokens[2].startswith('mi') else 'km'
            distance = parse_quantity(tokens[1], U_('km'))
            time = parse_time_to_timedelta(tokens[0])
            logger.info(f"time {time}, distance {distance}, unit {unit}")
            splits = even_splits(distance, time, unit)
            em = discord.Embed(
                title=f"{unit.capitalize()} splits for {tokens[0]} {tokens[1]}",
                colour=discord.Color(0).blurple()
            )
            if len(splits) > 25:
                em.description = "\n".join(str(split) for split in splits)
            else:
                for split in splits:
                    em.add_field(name=split.index +1, value=str(split), inline=True)

            await ctx.send(embed=em)
        except Exception:
            logger.exception("Uh oh")
        

    @commands.command(aliases=["calculate.pace"])
    async def pace(self, ctx, *, parms):
        """
        Usage:
                r!pace distance time
            ex:
                r!pace 10km 50:00min
        """
        try:
            tokens = parms.split()
            if len(tokens) != 2:
                await ctx.send (
                    "Expected 2 or 3 arguments, distance, time and optional unit.\n"
                    "Ex:\n"
                    "\t- r!pace 10km 50min"
                    "\t- r!pace 10km 50min"
                )
                return

            distance = parse_quantity(tokens[0], U_('km'))
            time = parse_time_to_timedelta(tokens[1])
            computed_pace = pace(distance, time)
            km_pace = timedelta(seconds=computed_pace.to('sec/km').m)
            mile_pace = timedelta(seconds=computed_pace.to('sec/mile').m)
       
            em = discord.Embed(
                title=f"Pace calculation for {ctx.message.author.display_name}",
                colour=discord.Color(0).blurple()
            )
            em.add_field(name="Distance", value=distance)
            em.add_field(name="Time", value=time)
            em.add_field(name="Pace (km)", value=fmt_delta(km_pace))
            em.add_field(name="Pace (mi)", value=fmt_delta(mile_pace))

            await ctx.send(embed=em)
            
        except Exception as e:
            print ("An error occured: " + e)

    @commands.command(aliases=["con"])
    async def convert(self, ctx, *, query):
        try:
            logger.info(query)
            qty = parse_quantity(query)

            if qty is None:
                await ctx.send(f"Unrecognized unit {query}")
            conversions = convert(qty)
            
            em = discord.Embed(
                title=f'Conversions for "{query}"',
                colour=discord.Colour.blurple(),
            )

            for converted in conversions:
                
                em.add_field(
                    name=converted.u, 
                    value=fmt_qty(converted), inline=False,
                )
            
            await ctx.send(embed=em)
        except Exception:
            logger.exception("Error performing conversions")

    @convert.error
    async def convert_error(self, ctx, error):
        await ctx.send(f"Unrecognized unit")

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