import asyncio
import discord
from discord.ext import commands

# Set the bot prefix
Bot_Prefix = "xx!"

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
    await client.process_commands(message)


# When new member join, automatically give a role and send message
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='無知之徒')
    await client.add_roles(member, role)
    channel = discord.utils.get(member.server.channels, name='welcome')
    await client.send_message(channel, '{}/{}.'.format('Role has been set up', '已添加身份-無知之徒'))


# For register the item for selling in market
@client.command(pass_context=True)
async def sell(ctx):
    channel = ctx.message.channel
    channel_name = channel.name

    if channel_name != '黑市':
        await client.say('黑市之外無法注冊')
        await delete_message(channel, 2, 3)

    else:
        author = ctx.message.author
        await client.send_message(author, '注冊成功')
        await client.delete_message(ctx.message)


# To add role for players
@client.command(pass_context=True)
async def begin(ctx):
    member = ctx.message.author
    role = discord.utils.get(member.server.roles, name='江湖之人')
    await client.add_roles(member,role)
    await client.say('開始你的修仙之路吧')
    await delete_message(ctx.message.channel, 2, 3)


# To add role for players
@client.command(pass_context=True)
async def chigua(ctx):
    member = ctx.message.author
    role = discord.utils.get(member.server.roles, name='吃瓜群衆')
    await client.add_roles(member, role)
    await client.say('去吃你的瓜吧')
    await delete_message(ctx.message.channel, 2, 3)


# To delete messages
async def delete_message(channel, limit, time):
    messages = []
    async for message in client.logs_from(channel, limit):
        messages.append(message)
    await asyncio.sleep(time)
    await client.delete_messages(messages)

# Run bot with Token
client.run(Token)
