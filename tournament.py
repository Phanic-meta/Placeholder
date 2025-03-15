import discord
from typing import TypedDict, NotRequired
import mongodb

class Tournament(TypedDict):
        _id: NotRequired[str]
        name: str
        creator: dict
        guild: int
        status: str
        players: list[dict]
        layout:  list

async def create_new_tournament(interaction: discord.Interaction, name: str) -> None:
        creator = mongodb.request_user({"_id":interaction.user.id})
        if creator is None:
                raise Exception("You have to create an user first try:\n/create_user")
        check = mongodb.request_tournament({"name":name, "guild":interaction.guild.id})
        if check is None:
                raise Exception("A tournament with that name already exists in your guild")
        tournament: Tournament = Tournament(name=name, creator=creator, guild=interaction.guild.id, status="created", players=[], layout=[])
        mongodb.insert_tournament(tournament)

async def join_tournament(interaction: discord.Interaction, name: str) -> None:
        user = mongodb.request_user({"_id":interaction.user.id})
        if user is None:
                raise Exception("You need to create an user first try: /create_user")
        tournament = mongodb.request_tournament({"name":name, "guild":interaction.guild.id})
        print(tournament)
        if tournament is None:
                raise Exception("This tournament does not exist in your guild")
        if tournament["status"] != "created":
                raise Exception("This tournament already started")
        for player in tournament["players"]:
                if player["_id"] == interaction.user.id:
                        raise Exception("You allready have already joined the tournament")
        tournament["players"].append(user)
