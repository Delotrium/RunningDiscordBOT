from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import discord
from discord.ext import commands

class Strava(commands.Cog):
    def __init__(self, client):
        self.client = client



async def setup(client):
    await client.add_cog(Strava(client))