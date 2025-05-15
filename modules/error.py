import discord

async def sendError(channel, message):
    try:
        embed = discord.Embed(title=f"{message}", color=discord.Color.red())
        embed.set_footer(text=f"UKN Tracker")
        await channel.send(embed=embed)

    except Exception as e:
        print(f"Sending error message failed: {e}")
        embed = discord.Embed(title="System currently overloaded, please try again later!", color=discord.Color.red()) # More descriptive title
        embed.set_footer(text=f"UKN Tracker")
        try:
            await channel.send(embed=embed)
        except:
            pass