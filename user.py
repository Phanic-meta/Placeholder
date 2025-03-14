import discord
from typing import TypedDict, NotRequired

class User(TypedDict):
    _id: discord.User.id
    user: str
    lichessname: str



async def create_user(user: discord.User, lichesname: "str"):
