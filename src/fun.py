import discord
from discord.ext import commands
import random
import praw
import time
import os
class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball', '8b'])
    async def eightball(self, ctx, *, question):
        answers = ['It is certain',
                   'It is decidedly so', 
                   'Without a doubt', 
                   'Yes – definitely', 
                   'You may rely on it', 
                   'As I see it, yes', 
                   'Most likely', 
                   'Outlook good', 
                   'Yes Signs point to yes', 
                   'Reply hazy', 
                   'try again', 
                   'Ask again later', 
                   'Better not tell you now', 
                   'Cannot predict now', 
                   'Concentrate and ask again', 
                   'Dont count on it', 
                   'My reply is no', 
                   'My sources say no', 
                   'Outlook not so good', 
                   'Very doubtful']
        await ctx.send(f"{ctx.author.mention} asked: {question}\n My reply is: {answers[random.randint(0, len(answers)-1)]}")


    @commands.command(aliases=['kill', 'hunt'])
    async def shoot(self, ctx, member : discord.Member):
        replies = [f'Damn nice shot {ctx.author.mention}. You shot {member.mention} right in the head....',
                   f'{ctx.author.mention}, did you know that was a water gun? You just got {member.mention} all wet... and not in a good way ;)',
                   f'Uhhh... well done {ctx.author.mention}. The gun was the wrong way.... You are very lucky {member.mention}',
                   f'{ctx.author.mention}, your gun was taken by {member.mention} after their quick karate skills, better luck next time.',
                   f'OMG {ctx.author.mention} JUST HIT A 360, NO-SCOPE, WALL JUMP, EYES CLOSED, PLAYING WITH FEET, BUNNY HOP, SHOT ON {member.mention}... MLG!!!!!',
                   f'{member.mention} ran away... maybe don\'t be so fat {ctx.author.mention}.',
                   f'{member.mention} pulled out a bigger gun, you better run {ctx.author.mention}.',
                   f'{ctx.author.mention} did you just hug {member.mention}? That\'s abit weird...',
                   f'A police officer was looking at you {ctx.author.mention}... you have to pay {member.mention} money...',
                   f'{ctx.author.mention} chose kick! It was highly effective! {member.mention} is now half HP!']
        await ctx.send(replies[random.randint(0, 9)])

    @commands.command()
    async def chance(self, ctx, *, query):
        await ctx.send(f"{ctx.author.mention}, there is a {random.randint(1, 100)}% chance that {query}!")

    @commands.command()
    async def guessnumber(self, ctx, *, setting="normal"):
        if setting == "easy":
            computer = random.randint(1,5)
        elif setting =="normal":
            computer = random.randint(1, 10)        
        elif setting == "hard":
            computer = random.randint(1, 20)
        elif setting == "impossible" or "ultra hard" or "harder" or "difficult":
            computer = random.randint(1,35)
        
        await ctx.send(f'{ctx.author.mention} Guess my number!')
        i=0
        while i < 3:
            def check(msg):
                return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) in ['exit', 'close', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
            msg = await self.client.wait_for("message", check=check)
            if int(msg.content) == computer:
                await ctx.send(f"{ctx.author.mention} is correct!")
            elif i < 2:
                await ctx.send(f"{ctx.author.mention} that is incorrect! You have {2-i} tries left! ")
                i += 1
            elif i == 2:
                await ctx.send(f"Damn {ctx.author.mention}, you are that bad..? (The answer was {computer})")
            elif msg.content == 'exit' or 'close':
                await ctx.send(f'Oh, goodbye then {ctx.author.mention}...')
                break

    @commands.command(aliases=["rps"])
    async def rockpaperscissors(self, ctx):
        listrps = ['rock', 'paper', 'scissors', 'exit', 'close']
        def check(msg):
                return msg.author == ctx.author and msg.channel == ctx.channel and (msg.content) in listrps
        computer = listrps[random.randint(0, 2)]
        await ctx.send(f'{ctx.author.mention} Rock, Paper or Scissors?')
        msg = await self.client.wait_for("message", check=check)
        await ctx.send("3...")
        time.sleep(0.5)
        await ctx.send("2...")
        time.sleep(0.5)
        await ctx.send("1...")
        time.sleep(0.5)    
        await ctx.send(f"I chose {computer}!")
        if computer == msg.content:
            await ctx.send(f'So thats a tie!')
        elif (computer == 'rock') and (msg.content == 'paper'):
            await ctx.send(f"Paper beats rock! Well done {ctx.author.mention}")
        elif (computer == 'rock') and (msg.content == 'scissors'):
            await ctx.send(f'Rock beats scissors, get better {ctx.author.mention}')
        elif (computer == 'paper') and (msg.content == 'rock'):
            await ctx.send(f'Paper beats rock. Boom! I beat you {ctx.author.mention}')
        elif (computer == 'paper') and (msg.content == 'scissors'):
            await ctx.send(f'Welp looks like you won as you cut me in half {ctx.author.mention}.')
        elif (computer == 'scissors') and (msg.content == 'rock'):
            await ctx.send(f'Did you just hit me with a rock!? Damn {ctx.author.mention}, looks like you beat me this time...')
        elif (computer == 'scissors') and (msg.content =='paper'):
            await ctx.send(f'Damn I just cut you up like surgery, nighty night {ctx.author.mention}.')

    @commands.command(aliases=["roll"])
    async def dice(self, ctx):
        dicerolle = random.randint(1, 6)
        embed=discord.Embed(title="Dice", color=0x109319)
        if dicerolle == 1:
            imgurl="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.Fs0So8L1w2Hh71oQdwoM_wHaHa%26pid%3DApi&f=1"
        if dicerolle == 2:
            imgurl="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.AwPg1S8V5KPT0cQgdomKWQHaHa%26pid%3DApi&f=1"
        if dicerolle == 3:
            imgurl="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fclipground.com%2Fimages%2Fnumber-3-dice-clipart-black-and-white-1.png&f=1&nofb=1"
        if dicerolle == 4:
            imgurl="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2Ff%2Ffd%2FDice-4-b.svg%2F1200px-Dice-4-b.svg.png&f=1&nofb=1"
        if dicerolle == 5:
            imgurl="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F0%2F08%2FDice-5-b.svg%2F1024px-Dice-5-b.svg.png&f=1&nofb=1"
        if dicerolle == 6:
            imgurl="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.Cuz64mDr1YUs0epcrqq_BgHaHa%26pid%3DApi&f=1"
        embed.set_author(name="The dice man!", icon_url="https://imgr.search.brave.com/NnwccI1a1h4uef1CiOUxOu2JWSDG3QIOt8pvLjhVqeo/fit/632/225/ce/1/aHR0cHM6Ly90c2Ux/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5P/bkg5cUpaOS1aNWY3/eXhVSVZwNnhnSGFG/aiZwaWQ9QXBp")
        embed.set_image(url=imgurl)
        await ctx.send(embed=embed)

        

def setup(client):
    client.add_cog(Fun(client))
