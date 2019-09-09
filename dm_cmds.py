import discord
from discord.ext import commands
import asyncio

class dm_cmds:
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def wordcheck(self,ctx):
        if not ctx.message.guild:
            wordcheck_enabled = True
            words1 = []
            words2 = []
            done = False
            async def end30():
                await asyncio.sleep(30)
                wordcheck_enabled = False
            embed = discord.Embed(colour=0x0000FF)
            embed.add_field(name="__Wordcheck__",value="To add words, send the word and the translation with a '=' in between.```Example: hej = hello```When you feel done, type 'start' to start the wordcheck.",inline=True)
            await ctx.message.author.send(embed=embed)
            if wordcheck_enabled == True:
                def check(m):
                    return m.guild == None and m.author == ctx.message.author and wordcheck_enabled == True
                while done == False:
                    msg = await self.client.wait_for('message',check=check)
                    if ' = ' in msg.content:
                        words = msg.content.split(" = ")
                        words1.append(words[0])
                        words2.append(words[1])
                        embed = discord.Embed(colour=0x0000FF)
                        embed.add_field(name="__Word added__",value=msg.content,inline=True)
                        await ctx.message.author.send(embed=embed)
                    elif msg.content == "start":
                        done = True
                    elif msg != None:
                        embed = discord.Embed(colour=0xFF0000)
                        embed.add_field(name="***ERROR***",value="Wrong syntax. Words must be added in this format:```hej = hello```",inline=True)
                        await ctx.message.author.send(embed=embed)
                    else:
                        await end30()
                async def testwords():
                    correct = 0
                    for n in range(int(len(words1))):
                        embed = discord.Embed(colour=0x0000FF)
                        embed.add_field(name="__Question {}__".format(n+1),value="**{} = ?**".format(words1[n]),inline=False)
                        qmsg = await ctx.message.author.send(embed=embed)
                        msg = await self.client.wait_for('message',check=check)
                        if msg.content == words2[n]:
                            correct += 1
                            await msg.add_reaction("\U00002705")
                            embed = discord.Embed(colour=0x0000FF)
                            embed.add_field(name="__Question {}__".format(n+1),value="**{} = {}**".format(words1[n],words2[n]),inline=False)
                            await qmsg.edit(embed=embed)
                        else:
                            await msg.add_reaction("\U0000274c")
                            embed = discord.Embed(colour=0x0000FF)
                            embed.add_field(name="__Question {}__".format(n+1),value="**{} = {}**".format(words1[n],words2[n]),inline=False)
                            await qmsg.edit(embed=embed)
                        await asyncio.sleep(1)
                    if correct == int(len(words1)):
                        embed = discord.Embed(colour=0x0000FF)
                        embed.add_field(name="__Results__",value="You got {}/{} words right. Good job!\nTo try again, type 'again'".format(correct,int(len(words1))))
                        await ctx.message.author.send(embed=embed)
                        msg = await self.client.wait_for('message',check=check)
                        if msg.content == "again":
                            await testwords()
                        elif msg == None:
                            await end30()
                    else:
                        embed = discord.Embed(colour=0x0000FF)
                        embed.add_field(name="__Results__",value="You got {}/{} words right.\nTo try again, type 'again'".format(correct,int(len(words1))))
                        await ctx.message.author.send(embed=embed)
                        msg = await self.client.wait_for('message',check=check)
                        if msg.content == "again":
                            await testwords()
                        elif msg == None:
                            await end30()
                await testwords()



def setup(client):
    client.add_cog(dm_cmds(client))
