import discord
from discord.ext import commands
import asyncio


class m_cmds:
    def __init__(self, client):
        self.client = client

    # CLEAR COMMAND
    @commands.command()
    async def clear(self, ctx, amount=None):
        if ctx.message.author.guild_permissions.manage_messages:
            if amount is not None:
                if int(amount) < 100:
                    messages = []
                    async for m in ctx.channel.history(limit=int(amount) + 1):
                        messages.append(m)
                    await ctx.channel.delete_messages(messages)
                    msg = await ctx.channel.send(
                        embed=discord.Embed(title="{} messages were deleted!".format(amount), colour=0x0000FF))
                    await asyncio.sleep(3)
                    await msg.delete()
                else:
                    await ctx.message.delete()
                    msg = await ctx.channel.send(embed=discord.Embed(
                        title="You can only delete a maximum of 99 messages at a time.".format(amount),
                        colour=0x0000FF))
                    await asyncio.sleep(3)
                    await msg.delete()
            else:
                await ctx.message.delete()
                msg = await ctx.channel.send(
                    embed=discord.Embed(title="How many? ex. !clear 3".format(amount), colour=0x0000FF))
                await asyncio.sleep(3)
                await msg.delete()

        else:
            await ctx.message.delete()
            embed = discord.Embed(title="Insufficient permissions", colour=0x0000FF)
            embed.set_image(url="https://i.imgur.com/HuU47bW.png")
            msg = await ctx.message.author.send(embed=embed)
            await asyncio.sleep(45)
            await msg.delete()

    # KICK COMMAND
    @commands.command()
    async def kick(self, ctx, usr: discord.Member = None, *, reason=None):
        if ctx.message.author.guild_permissions.kick_members:
            if usr is not None:
                if usr.id != 172340872367702016:
                    await ctx.message.delete()
                    if reason is None:
                        await ctx.message.guild.kick(usr)
                        msg = await ctx.channel.send(
                            embed=discord.Embed(title="{} has been kicked!".format(usr.name), colour=0x0000FF))
                        await asyncio.sleep(5)
                        await msg.delete()
                    else:
                        await ctx.message.guild.kick(usr, reason=reason)
                        msg = await ctx.channel.send(
                            embed=discord.Embed(title="{} has been kicked! Reason: '{}'".format(usr.name, str(reason)),
                                                colour=0x0000FF))
                        await asyncio.sleep(5)
                        await msg.delete()
                else:
                    await ctx.message.delete()
                    msg = await ctx.channel.send(
                        embed=discord.Embed(title="You cant kick gods".format(usr.name), colour=0x0000FF))
                    await asyncio.sleep(3)
                    await msg.delete()
        else:
            await ctx.message.delete()
            embed = discord.Embed(title="Insufficient permissions", colour=0x0000FF)
            embed.set_image(url="https://i.imgur.com/HuU47bW.png")
            msg = await ctx.message.author.send(embed=embed)
            await asyncio.sleep(45)
            await msg.delete()


def setup(client):
    client.add_cog(m_cmds(client))
