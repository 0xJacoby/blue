import discord
from discord.ext import commands
import asyncio
import datetime
import json

class bgts:
    def __init__(self,client):
        self.client = client

    async def update_daily_coin(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            mtime = str(datetime.datetime.now().time())
            if mtime[:5] == "04:00":
                with open("databases/user_database","r") as f:
                    users = json.load(f)
                for user in self.client.get_all_members():
                    users[str(user.id)]["used_daily_coin"] = False
                with open("databases/user_database","w") as f:
                    json.dump(users,f)
            await asyncio.sleep(60)




def setup(client):
    cog = bgts(client)
    client.loop.create_task(cog.update_daily_coin())
    client.add_cog(bgts(client))
