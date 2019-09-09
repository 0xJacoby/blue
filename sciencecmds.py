import discord
from discord.ext import commands
import asyncio
import json
import aiohttp

class sciencecmds:
    def __init__(self,client):
        self.client = client

# CPP COMPILING
    async def on_reaction_add(self, reaction, user):
        if str(reaction.emoji) == "\U00002795":
            code = str(reaction.message.content)
            if code.startswith("```") or code.endswith("```") or code.startswith("```") and code.endswith("```"):
                code = code.replace("```","")
            cm = "g++ -std=c++17 -O2 -Wall -pedantic -pthread main.cpp && ./a.out"
            di = {'cmd': cm, 'src': code}
            d = json.dumps(di)
            async with aiohttp.ClientSession() as session:
                async with session.post("http://coliru.stacked-crooked.com/compile", data=d) as r:
                    response = await r.text()
            await reaction.message.channel.send("***Compiled C++ code:***\n```fix\n{}\n```".format(str(response)))
# Python Comping
        elif str(reaction.emoji) == "\U0001f40d":
            code = str(reaction.message.content)
            if code.startswith("```") or code.endswith("```") or code.startswith("```") and code.endswith("```"):
                code = code.replace("```","")
            cm = "python3 main.cpp"
            di = {'cmd': cm, 'src': code}
            d = json.dumps(di)
            async with aiohttp.ClientSession() as session:
                async with session.post("http://coliru.stacked-crooked.com/compile", data=d) as r:
                    response = await r.text()
            await reaction.message.channel.send("***Interpreted Python code:***\n```fix\n{}\n```".format(str(response)))










def setup(client):
    client.add_cog(sciencecmds(client))
