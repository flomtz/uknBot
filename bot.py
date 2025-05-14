import discord
from discord.ext import commands

from utils.token import get_token
from commands.ping import ping_command

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.dm_messages = True
intents.guilds = True

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    try:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="at your UKN Stats"))
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@client.tree.command(name="ping", description="Ping Pong")
async def ping(interaction: discord.Interaction):
    await ping_command(interaction)




token = get_token()
client.run(token)