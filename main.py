import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands

import tournament
import user
# Load Toaken from Safe File
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Intents Setup
intents = discord.Intents.all()
discordclient = discord.Client(intents=intents, command_prefix="uwu")
tree = app_commands.CommandTree(discordclient)

# Startup Handling
@discordclient.event
async def on_ready() -> None:
    print(f'{discordclient.user} has connected to Discord!')
    try:
        await tree.sync()  # Sync the Commands
        print("Synced")
    except Exception as e:
        print(e)

# Message Handling
@tree.command(name="create_tournament", description="create a new tournament")
async def create_tournament(interaction: discord.Interaction, name: str):
    try:
        await tournament.create_new_tournament(interaction, name)
        await interaction.response.send_message("Tournament created!", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(e, ephemeral=True)

@tree.command(name="join_tournament", description="join a tournament")
async def create_tournament(interaction: discord.Interaction, name: str):
    try:
        await tournament.join_tournament(interaction, name)
        await interaction.response.send_message("Tournament joind!", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(e, ephemeral=True)


@tree.command(name="create_user", description="create a new User")
async def create_user(interaction: discord.Interaction, lichessusername: str):
    try:
        await user.create_new_user(interaction, lichessusername)
        await interaction.response.send_message("User created", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(e, ephemeral=True)

#Run the Bot
def main() -> None:
    discordclient.run(TOKEN)

if __name__ == '__main__':
    main()