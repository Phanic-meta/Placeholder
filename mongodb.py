from bson import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()
uri = os.getenv("DB_URI")


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
database = client["tournament"]
dbuser = database["user"]
dbtournament = database["tournament"]
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
#
# User Funktions

def request_user(user: dict):
    return dbuser.find_one(user)
def insert_user(user: dict):
    dbuser.insert_one(user)
def update_user(id: int, lichessname: str):
    dbuser.update_one({"_id": id}, {"lichessname": lichessname})
def delete_user(id: int):
    dbuser.delete_one({"_id": id})

# Tournament Funktions
def insert_tournament(tournament: dict):
    dbtournament.insert_one(tournament)
def request_tournament(tournament: dict):
    return dbtournament.find_one(tournament)
def update_tournament(id: int, tournament: dict):
    dbtournament.update_one({"_id": id}, {"tournament": tournament})
