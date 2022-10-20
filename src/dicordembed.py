from ast import alias
import discord
from discord.ext import commands

class DiscordEmbeds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["muscles"])
    async def muscle(self, ctx, *, group="body"):
        if group.lower() == "body" or group.lower() == "whole":
            em = discord.Embed()
            colour = discord.Color(255)
            em.set_author(name="RunBOT Physiology")
            em.title = "Major Muscles Groups (Whole Body)"
            em.colour = colour.red()
            em.description = f"The Major Muscle Groups in the human body are as seen below (click image to expand):\n"
            em.set_image(url = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.wallflexpro.com%2Fwp-content%2Fuploads%2F2015%2F05%2Fmajormusclegroup.jpg&f=1&nofb=1&ipt=fa0bf3c35945cd85c435c7c90ecc85a749d9840db1f2be854b407f31b4e3b65f&ipo=images")
        elif group.lower() == "leg" or group.lower() == "legs" or group.lower() == "lower":
            em = discord.Embed()
            colour = discord.Color.from_rgb(20, 0, 198)
            em.set_author(name="RunBOT Physiology")
            em.title = "Major Muscles (Legs)"
            em.colour = colour
            em.description = f"The Major Muscles in the legs are as seen below (click image to expand):\n"
            em.set_image(url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fdoctorlib.info%2Fanatomy%2Fclassic-human-anatomy-motion%2Fclassic-human-anatomy-motion.files%2Fimage290.jpg&f=1&nofb=1&ipt=ddcee776833be7ca3a1656a26f22ee1ede55bbb3eba8d50030ff99324b35d6de&ipo=images")
            await ctx.send(embed=em)
        elif group.lower() == "chest" or group.lower() == "upper" or group.lower() == "torso" or group.lower() == "waist" or group.lower() == "abdomen":
            em = discord.Embed()
            colour = discord.Color.from_rgb(255, 179, 0)
            em.set_author(name="RunBOT Physiology")
            em.title = "Major Muscles (Torso/Chest/Abdomen)"
            em.colour = colour
            em.description = f"The Major Muscles in the Torso/Chest/Abdomen are as seen below (click image to expand):\n"
            em.set_image(url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fdoctorlib.info%2Fanatomy%2Fclassic-human-anatomy-motion%2Fclassic-human-anatomy-motion.files%2Fimage219.jpg&f=1&nofb=1&ipt=38f259d2c0a5c63c10e3c05618648459dd8bcd24c300b23a4455d64b8aabb5bb&ipo=images")
            await ctx.send(embed=em)
        elif group.lower() == "chest" or group.lower() == "upper" or group.lower() == "torso" or group.lower() == "waist" or group.lower() == "abdomen":
            em = discord.Embed()
            colour = discord.Color.from_rgb(255, 179, 0)
            em.set_author(name="RunBOT Physiology")
            em.title = "Major Muscles (Torso/Chest/Abdomen)"
            em.colour = colour
            em.description = f"The Major Muscles in the Torso/Chest/Abdomen are as seen below (click image to expand):\n"
            em.set_image(url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fdoctorlib.info%2Fanatomy%2Fclassic-human-anatomy-motion%2Fclassic-human-anatomy-motion.files%2Fimage219.jpg&f=1&nofb=1&ipt=38f259d2c0a5c63c10e3c05618648459dd8bcd24c300b23a4455d64b8aabb5bb&ipo=images")
            await ctx.send(embed=em)
        elif group.lower() == "arms" or group.lower() == "limbs" or group.lower() == "upper limbs" or group.lower() == "arm":
            em = discord.Embed()
            colour = discord.Color.from_rgb(236, 0, 245)
            em.set_author(name="RunBOT Physiology")
            em.title = "Major Muscles (Arms)"
            em.colour = colour
            em.description = f"The Major Muscles in the Arms are as seen below (click image to expand):\n"
            em.set_image(url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.tabers.com%2Ftabersonline%2Frepview%3Ftype%3D539-140%26name%3DA38&f=1&nofb=1&ipt=7c57d53adb22b59178b3d6144a470d07c5125781aa4b9c05aa18243e3cc3220f&ipo=images")
            await ctx.send(embed=em)
        elif group.lower() == "back" or group.lower() == "spine":
            em = discord.Embed()
            colour = discord.Color.from_rgb(17, 255, 0)
            em.set_author(name="RunBOT Physiology")
            em.title = "Major Muscles (Back/Spine)"
            em.colour = colour
            em.description = f"The Major Muscles in the Back/Spine are as seen below (click image to expand):\n"
            em.set_image(url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fhealthiack.com%2Fwp-content%2Fuploads%2FPictures-of-back-muscles-36.jpg&f=1&nofb=1&ipt=c8fd4d6d76f5f8c31bf0fcc2afbf7589701beeed5b6d20ed589269e8997ac38c&ipo=images")
            await ctx.send(embed=em)
        elif group.lower() == "head" or group.lower() == "skull":
            em = discord.Embed()
            colour = discord.Color.from_rgb(255, 255, 0)
            em.set_author(name="RunBOT Physiology")
            em.title = "Major Muscles (Head)"
            em.colour = colour
            em.description = f"The Major Muscles in the Head are as seen below (click image to expand):\n"
            em.set_image(url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2F2.bp.blogspot.com%2F-ei0gkJakS9Q%2FWrgu-eV-kUI%2FAAAAAAAAFZY%2FfrLECpnaqhg9ZoCf7X7f5uuKESbtKG2IwCLcBGAs%2Fs1600%2Fmuscles%252B-%252Bfront%252Bview%252Bv2.jpg&f=1&nofb=1&ipt=ff6f38323d7d002c36e3d0fe9d4aa3a7ef6ab5966b9036b1ba1dc60213507b59&ipo=images")
            await ctx.send(embed=em)

async def setup(client):
    await client.add_cog(DiscordEmbeds(client))