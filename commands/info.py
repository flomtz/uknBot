import discord

async def info_command(interaction: discord.Interaction):
    embed=discord.Embed(title="Important information", color=0x64a6ff)
    embed.set_thumbnail(url="https://i.ibb.co/bRdZfwY6/pepebusiness.png")
    embed.add_field(name="", value="", inline=False)
    embed.add_field(name="Report", value="If you encounter any bugs or problems, feel free to reach out to me!", inline=False)
    embed.add_field(name="", value="", inline=False)
    embed.add_field(name="Credits", value="This project utilizes data from UKN. Check them out at https://ukn.gg if you haven’t already.", inline=False)
    embed.add_field(name="", value="", inline=False)
    embed.add_field(name="Developer", value="Developed and hosted by Scxptix", inline=False)
    embed.add_field(name="", value="", inline=False)
    embed.add_field(name="Support me", value="Enjoying my work? You can support me by sending Rust skins on Steam! :heart:", inline=False)
    embed.add_field(name="", value="", inline=False)
    embed.set_footer(text=f"UKN Tracker")
    await interaction.response.send_message(embed=embed)