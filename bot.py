import discord

from discord import app_commands
from discord.ext import commands, tasks

from utils.token import get_token
from commands.info import info_command
from commands.report import report_command

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


@client.tree.command(name="info", description="Information about the Bot")
async def info(interaction: discord.Interaction):
    await info_command(interaction)

@client.tree.command(name="report", description="Report a Bug/Problem")
@app_commands.describe(message="Describe your Bug/Problem")
async def report(interaction: discord.Interaction, message: str):
    await report_command(interaction, message)




token = get_token()
client.run(token)