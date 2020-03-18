from .user import User
from ..utils.http import get

class Guild:

    def __init__(self, fastcord, obj):
        self.fastcord = fastcord
        self.id = obj["id"]
        self.name = obj["name"]
        self.icon = f"https://cdn.discordapp.com/icons/{self.id}/{obj['icon']}.jpg"
        self.owner = User(fastcord, get(f"{fastcord.api}/users/{obj['owner_id']}",
            { "Authorization": "Bot " + fastcord.token }))
