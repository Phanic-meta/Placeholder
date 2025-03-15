import berserk
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("LICHESS_TOKEN")
session = berserk.TokenSession(TOKEN)
lichesclient = berserk.Client(session)
print(lichesclient, "Start")

def check_user(username: str) -> bool:
    try:
        lichesclient.users.get_public_data(username)
        return True
    except:
        return False
