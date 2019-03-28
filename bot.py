import discord
from discord.ext import commands

# Set the bot prefix
Bot_Prefix = ('XX')
# Set the bot token
Token = 'NTU4NDU0MDYwMDAxMzk0Njkx.D3XH7w.fsLJMqlZkznsE_CU0__r6_BxIjs'

# Set the bot
client = commands.Bot(command_prefix=Bot_Prefix)

# To remove the default help menu
client.remove_command('help')


# 1. To check if the bot is ready
# 2. To change the bot status
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='挂機修仙'))
    print("Ready")


# Detect the message create and send
@client.event
async def on_message(message):
    content = message.content
    author = message.author
    time = message.timestamp
    print(time)
    print(author)
    print(content)


# When new member join, automatically give a role and send message
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='無知之徒')
    await client.add_roles(member, role)
    channel = discord.utils.get(member.server.channels, name='welcome')
    await client.send_message(channel, '{}/{}.'.format('Role has been set up', '已添加身份'))


# Run bot with Token
client.run(Token)
