import discord
import berserk
from dotenv import load_dotenv
import os
from user import User
load_dotenv()
TOKEN = os.getenv("LICHESS_TOKEN")
session = berserk.TokenSession(TOKEN)
lichesclient = berserk.Client(session)
print(lichesclient, "Start")


class Tournament:
    def __init__(self, creator: User, guild: discord.Guild, layout: list):
        self.creator: User = creator
        self.guild: discord.Guild = guild
        self.status = "created"
        self.players: list[User] = []
        self.layout: list = layout
    def add_player(self, player: User):
        self.players.append(player)
    def start_tournament(self):
        self.status = "started"

    class Group:
        def __init__(self, name: str, percent: float, maxplayers: int):
            self.name: str = name
            if percent > 1:
                raise ValueError("Percent must be less than 100")
            self.percent: float = percent
            if maxplayers < 2:
                raise ValueError("Maxplayers must be greater than 2")
            self.maxplayers: int = maxplayers



async def create_tournament(interaction: discord.Interaction) -> None:
    tournament = Tournament()