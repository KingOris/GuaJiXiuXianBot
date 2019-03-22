import discord
from discord.ext import commands

Bot_Prefix = ('XX')
Token = 'NTU4NDU0MDYwMDAxMzk0Njkx.D3XH7w.fsLJMqlZkznsE_CU0__r6_BxIjs'

client = commands.Bot(command_prefix=Bot_Prefix)


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='挂機修仙'))
    print("Ready")


client.run(Token)
