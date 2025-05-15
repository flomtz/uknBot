import discord
import uuid
import json

async def createReport(interaction: discord.Interaction, message: str):
    reports_path = "data/reports.json"
    reportChannelID = 1341875988837171323

    try:
        try:
            with open(reports_path, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        reportId = str(uuid.uuid4().fields[-1])[:5]
        while reportId in data:
            reportId = str(uuid.uuid4().fields[-1])[:5]

        channel = interaction.client.get_channel(reportChannelID)
        embed = discord.Embed(title=f"Report #{reportId}", color=0x64a6ff)
        embed.add_field(name=f"{interaction.user.name} from {interaction.guild.name} ({interaction.guild.id})", value=message, inline=False)
        embed.add_field(name=f"", value="", inline=False)
        embed.add_field(name=f"", value=message, inline=False)
        embed.add_field(name=f"", value="", inline=False)
        embed.set_footer(text=f"UKN Tracker")
        message = await channel.send(embed=embed)
        await message.add_reaction("✅")
        await message.add_reaction("❌")


        if reportId not in data:
            data[reportId] = []

        with open(reports_path, "w") as file:
            json.dump(data, file, indent=4)

        return True, None, reportId

    except Exception as e:
        return False, f"Error creating report: {e}", None
