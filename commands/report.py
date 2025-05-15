import discord

from modules.createReport import createReport
from modules.error import sendError

async def report_command(interaction: discord.Interaction, message: str):
    channel = interaction.guild.get_channel(int(interaction.channel.id))
    response, message, reportId = await createReport(interaction, message)
    if response == False:
        await sendError(channel, message)
    else:
        embed=discord.Embed(title=f"Report #{reportId} send successfully!", color=0x64a6ff)
        embed.add_field(name="", value="We will message you on Discord as quick as we can", inline=False)
        embed.set_footer(text=f"UKN Tracker")
        await interaction.response.send_message(embed=embed)