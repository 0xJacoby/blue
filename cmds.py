import discord
from discord.ext import commands
import asyncio
import datetime
import json
import bs4 as bs
import aiohttp


class cmds:
    def __init__(self, client):
        self.client = client

    # TEST COMMAND
    @commands.command()
    async def ping(self, ctx):
        if ctx.message.author.id == 172340872367702016:
            msg = await ctx.channel.send("pong")
            await asyncio.sleep(5)
            await msg.delete()
            await asyncio.sleep(3)
            await ctx.message.delete()

# TEST COMMAND
    @commands.command()
    async def test(self, ctx):
        if ctx.message.author.id == 172340872367702016:
            msg = await ctx.channel.send("warcraft 3 < lego 2")

    # ECHO COMMAND
    @commands.command()
    async def echo(self, ctx):
        if ctx.message.author.id == 172340872367702016:
            msg = await ctx.channel.send(ctx.message.content)
            await asyncio.sleep(5)
            await msg.delete()
            await asyncio.sleep(3)
            await ctx.message.delete()

    # DM COMMAND
    @commands.command()
    async def dm(self, ctx, usr: discord.Member, *, content):
        await ctx.message.delete()
        await usr.send(str(content))


    # Ejecting cogs COMMAND
    @commands.command()
    async def ejectcog(self, ctx, cog):
        if ctx.message.author.id == 172340872367702016:
            if str(cog) == "skolcmds":
                with open("databases/guild_database.json", "r") as f:
                    _guilds = json.load(f)

                if _guilds[str(ctx.message.guild.id)]["skolcmds"]:
                    _guilds[str(ctx.message.guild.id)]["skolcmds"] = False
                    msg = await ctx.channel.send("Skolcmds Ejected.")
                else:
                    msg = await ctx.channel.send("**[Eject failure]** No loaded cog named Skolcmds.")

                with open("databases/guild_database.json", "w") as f:
                    json.dump(_guilds, f)
                await asyncio.sleep(5)
                await ctx.message.delete()
                await msg.delete()
            else:
                msg = await ctx.channel.send("**[Eject failure]** No loaded cog named {}.".format(str(cog)))
                await asyncio.sleep(5)
                await ctx.message.delete()
                await msg.delete()

    # PREFIX CHANGING COMMAND
    @commands.command()
    async def prefix(self, ctx, prfx):
        if ctx.message.guild:
            with open("databases/guild_database.json", "r") as f:
                _guilds = json.load(f)

            _guilds[str(ctx.message.guild.id)]["prefix"] = str(prfx)

            with open("databases/guild_database.json", "w") as f:
                json.dump(_guilds, f)
            msg = await ctx.channel.send(
                embed=discord.Embed(title="Command prefix changed to: '{}'".format(prfx), colour=0x0000FF))
            await asyncio.sleep(5)
            await msg.delete()
        else:
            with open("databases/user_database.json", "r") as f:
                _users = json.load(f)

            _users[str(ctx.message.author.id)]["dm_prefix"] = str(prfx)

            with open("databases/user_database.json", "w") as f:
                json.dump(_users, f)
            msg = await ctx.message.author.send(
                embed=discord.Embed(title="DM prefix changed to: '{}'".format(prfx), colour=0x0000FF))
            await asyncio.sleep(5)
            await msg.delete()

    # coin balance check cmds
    @commands.command()
    async def coins(self, ctx, usr: discord.Member = None):
        with open("databases/user_database.json", "r") as f:
            _users = json.load(f)

        if usr is None:
            user = ctx.message.author
        else:
            user = usr

        msg = await ctx.channel.send(embed=discord.Embed(
            title="{}'s balance: {} coins".format(user.display_name,
                                                  _users[str(user.id)]["coins"]), colour=0x0000FF))
        await asyncio.sleep(7)
        await ctx.message.delete()
        await msg.delete()

        with open("databases/user_database.json", "w") as f:
            json.dump(_users, f)

    @commands.command()
    async def bank(self, ctx, usr: discord.Member = None):
        with open("databases/user_database.json", "r") as f:
            _users = json.load(f)

        if usr is None:
            user = ctx.message.author
        else:
            user = usr

        msg = await ctx.channel.send(embed=discord.Embed(
            title="{}'s balance: {} coins".format(user.display_name,
                                                  _users[str(user.id)]["coins"]), colour=0x0000FF))
        await asyncio.sleep(7)
        await ctx.message.delete()
        await msg.delete()

        with open("databases/user_database.json", "w") as f:
            json.dump(_users, f)

    @commands.command()
    async def wallet(self, ctx, usr: discord.Member = None):
        with open("databases/user_database.json", "r") as f:
            _users = json.load(f)

        if usr is None:
            user = ctx.message.author
        else:
            user = usr

        msg = await ctx.channel.send(embed=discord.Embed(
            title="{}'s balance: {} coins".format(user.display_name,
                                                  _users[str(user.id)]["coins"]), colour=0x0000FF))
        await asyncio.sleep(7)
        await ctx.message.delete()
        await msg.delete()

        with open("databases/user_database.json", "w") as f:
            json.dump(_users, f)

    @commands.command()
    async def balance(self, ctx, usr: discord.Member = None):
        with open("databases/user_database.json", "r") as f:
            _users = json.load(f)

        if usr is None:
            user = ctx.message.author
        else:
            user = usr

        msg = await ctx.channel.send(embed=discord.Embed(
            title="{}'s balance: {} coins".format(user.display_name,
                                                  _users[str(user.id)]["coins"]), colour=0x0000FF))
        await asyncio.sleep(7)
        await ctx.message.delete()
        await msg.delete()

        with open("databases/user_database.json", "w") as f:
            json.dump(_users, f)

    # Coin leaderboard command
    @commands.command()
    async def leaderboard(self,ctx):
        with open("databases/user_database.json", "r") as f:
            _users = json.load(f)

        users = reversed(sorted(_users, key=lambda k: _users[k]["coins"]))

        guildusers = []
        for i in users:
            if ctx.message.guild.get_member(int(i)) is not None:
                guildusers.append(i)

        top10 = ""
        for i in range(10):
            try:
                usr = ctx.message.guild.get_member(int(guildusers[i]))
                if not _users[str(usr.id)]["coins"] == 0:
                    top10 += "{}. {}: {} coins\n".format(i + 1, usr.display_name, _users[str(usr.id)]["coins"])
                else:
                    break
            except IndexError:
                break

        if top10 == "":
            leaderboard = discord.Embed(title="How are we suppose to have a fucking leaderboard if no one has any "
                                              "fucking coins", colour=0x0000FF)
            msg = await ctx.channel.send(embed=leaderboard)
            await asyncio.sleep(5)
            await ctx.message.delete()
            await msg.delete()
        else:
            leaderboard = discord.Embed(title="__**Leaderboard**__", description=top10, colour=0x0000FF)
            msg = await ctx.channel.send(embed=leaderboard)
            await asyncio.sleep(30)
            await ctx.message.delete()
            await msg.delete()

        with open("databases/user_database.json", "w") as f:
            json.dump(_users, f)

    # DAILY COIN Command
    @commands.command()
    async def daily(self, ctx):
        with open("databases/user_database.json", "r") as f:
            _users = json.load(f)

        if not _users[str(ctx.message.author.id)]["used_daily_coin"]:
            _users[str(ctx.message.author.id)]["used_daily_coin"] = True
            _users[str(ctx.message.author.id)]["coins"] += 5
            embed = discord.Embed(timestamp=datetime.datetime.now(), colour=0x0000FF)
            embed.add_field(name="Daily reward claimed!",
                            value="You have claimed your reward of 5 coins.\nCome back tomorrow for more.", inline=True)
            embed.set_footer(text="Claimed by {}".format(ctx.message.author.display_name),
                             icon_url=ctx.message.author.avatar_url)
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(timestamp=datetime.datetime.now(), colour=0xFF0000)
            embed.add_field(name="Daily reward already claimed!",
                            value="You have already claimed your reward today.\nCome back tomorrow for more.",
                            inline=True)
            embed.set_footer(text="Claimed by {}".format(ctx.message.author.display_name),
                             icon_url=ctx.message.author.avatar_url)
            msg = await ctx.channel.send(embed=embed)
            await asyncio.sleep(5)
            await msg.delete()
            await ctx.message.delete()
        with open("databases/user_database.json", "w") as f:
            json.dump(_users, f)

    # VECKA COMMAND
    @commands.command()
    async def vecka(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://www.vecka.nu/') as r:
                res = await r.text()
        soup = bs.BeautifulSoup(res, 'lxml')
        msg = await ctx.channel.send("**{}**".format(str(soup.body.time.string)))
        await asyncio.sleep(7)
        await ctx.message.delete()
        await msg.delete()

    # LICHESS COMMAnd XD

    @commands.command()
    async def lichess(self, ctx, usr="none"):
        if not usr == "none":
            try:
                async with aiohttp.ClientSession() as cs:
                    async with cs.get('https://lichess.org/api/user/' + str(usr)) as r:
                        res = await r.text()
                soup = bs.BeautifulSoup(res, 'lxml')
                info = json.loads(str(soup.body.p.string))
                if not info["online"]:
                    status = "*Offline*"
                else:
                    status = "**Online**"

                ratings = ""

                for i in info["perfs"]:
                    addon = "{}: {}\n".format(i, info["perfs"][str(i)]["rating"])
                    ratings += addon

                totaltime = str(datetime.timedelta(seconds=info["playTime"]["total"])).split(":")
                total_h = ""
                total_m = ""
                if len(totaltime[0]) == 2:
                    if totaltime[0][0] == "0":
                        total_h = totaltime[0][1]
                    else:
                        total_h = totaltime[0]
                else:
                    total_h = totaltime[0]
                if len(totaltime[1]) == 2:
                    if totaltime[1][0] == "0":
                        total_m = totaltime[1][1]
                    else:
                        total_m = totaltime[1]
                else:
                    total_m = totaltime[1]
                if not total_h == "0":
                    playtime = "{} timmar och {} minuter".format(total_h, total_m)
                else:
                    playtime = "{} minuter".format(total_m)

                winrate = int(info["count"]["win"]) / int(info["count"]["all"])
                winrate = round(winrate * 100)

                embed = discord.Embed(title="Profile", url=info["url"], description=status, color=0x0000FF)
                embed.set_author(name="Lichess User: {}".format(info["username"]))
                embed.set_thumbnail(
                    url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Lichess_Logo.svg/2000px-Lichess_Logo.svg.png")
                embed.add_field(name="Ratings:", value=ratings, inline=False)
                embed.add_field(name="Total Wins:", value=info["count"]["win"], inline=False)
                embed.add_field(name="Total Draws:", value=info["count"]["draw"], inline=False)
                embed.add_field(name="Total Loses:", value=info["count"]["loss"], inline=False)
                embed.add_field(name="Winrate:", value="{}%".format(winrate), inline=False)
                embed.add_field(name="Total playtime:", value=playtime, inline=False)

                msg = await ctx.channel.send(embed=embed)
                await asyncio.sleep(30)
                await msg.delete()
                await ctx.message.delete()
            except AttributeError:
                msg = await ctx.channel.send(
                    embed=discord.Embed(title="Användare finns inte på lichess.", colour=0xFF0000))
                await asyncio.sleep(5)
                await msg.delete()
                await ctx.message.delete()
        else:
            msg = await ctx.channel.send(embed=discord.Embed(title="Ange en användare.", colour=0xFF0000))
            await asyncio.sleep(5)
            await msg.delete()
            await ctx.message.delete()


def setup(client):
    client.add_cog(cmds(client))
