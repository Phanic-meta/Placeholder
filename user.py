import discord
from typing import TypedDict, NotRequired
import mongodb
import lichess

class User(TypedDict):
    _id: int
    name: str
    lichessname: str

async def create_new_user(interaction: discord.Interaction, lichessname: "str"):
    if not lichess.check_user(lichessname):
        raise Exception("This Lichess user does not exist")
    if mongodb.request_user({"lichessname": lichessname}) is not None:
        raise Exception("Someone already claimed this lichess username")
    user: User = User(_id=interaction.user.id, name=interaction.user.name, lichessname=lichessname)
    try:
        mongodb.insert_user(user)
    except Exception as e:
        print(e)
        raise Exception("User already exists")

async def update_user(interaction: discord.Interaction, lichessname: str):
    if not lichess.check_user(lichessname):
        raise Exception("This Lichess user does not exist")
    if mongodb.request_user({"lichessname": lichessname}) is not None:
        raise Exception("Someone already claimed this lichess username")
    mongodb.update_user(interaction.user.id, lichessname)

async def delete_user(interaction: discord.Interaction):
    if mongodb.request_user({"_id": interaction.user.id}) is not None:
        raise Exception("User doesn't exist")
    mongodb.delete_user(interaction.user.id)