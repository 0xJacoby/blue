# By Jacob
import discord
from discord.ext import commands
import asyncio
import json


def get_prefix(client, message):
    if message.guild:
        with open("databases/guild_database.json", "r") as f:
            _guilds = json.load(f)
        prfx = _guilds[str(message.guild.id)]["prefix"]
        with open("databases/guild_database.json", "w") as f:
            json.dump(_guilds, f)
    else:
        with open("databases/user_database.json", "r") as f:
            _users = json.load(f)
        prfx = _users[str(message.author.id)]["dm_prefix"]
        with open("databases/user_database.json", "w") as f:
            json.dump(_users, f)
    return prfx


client = commands.Bot(command_prefix=get_prefix)

extensions = ["cmds", "bgts", "m_cmds", "dm_cmds", "skolcmds", "sciencecmds"]


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

    await client.change_presence(activity=discord.Game(name="By Jacob Sundh"))

    with open("databases/guild_database.json", "r") as f:
        _guilds = json.load(f)

    for guild in client.guilds:
        if not str(guild.id) in _guilds:
            _guilds[str(guild.id)] = {}
            _guilds[str(guild.id)]["prefix"] = '!'
            _guilds[str(guild.id)]["skolcmds"] = False

    with open("databases/guild_database.json", "w") as f:
        json.dump(_guilds, f)

    with open("databases/user_database.json", "r") as f:
        users = json.load(f)

    for guild in client.guilds:
        for user in guild.members:
            if not str(user.id) in users:
                users[str(user.id)] = {}
                users[str(user.id)]["username"] = user.name
                users[str(user.id)]["coins"] = 0
                users[str(user.id)]["dm_prefix"] = '!'
                users[str(user.id)]["used_daily_coin"] = False
                users[str(user.id)]["spam_check"] = []

    with open("databases/user_database.json", "w") as f:
        json.dump(users, f)


if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print("{} cannot be loaded. [{}]".format(extension, error))

client.run("NTAxNjU3NDQ0OTkzNDY2Mzgw.DqeQ9w.6X-NLAi3F9ZjLq2slekozRo-0zw")

# debug NTAxMDQ2MTExMjE0MjM5Nzc0.DqdHvg.n9T-tJcTg9G8frUGhoSaceFfFvY
# main NTAxNjU3NDQ0OTkzNDY2Mzgw.DqeQ9w.6X-NLAi3F9ZjLq2slekozRo-0zw
# https://discordapp.com/oauth2/authorize?&client_id=501657444993466380&scope=bot&permissions=2146958839
