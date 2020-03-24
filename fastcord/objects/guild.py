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
    
    def get_member(self, member_id):
        return User.Member(self.fastcord, get(f"{self.fastcord.api}/guilds/{self.id}/members/{member_id}",
            { "Authorization": "Bot " + self.fastcord.token }), self.id)
    
    def get_members(self, limit=10):
        members = []
        arr = get(f"{self.fastcord.api}/guilds/{self.id}/members?limit={limit}",
            { "Authorization": "Bot " + self.fastcord.token })
        
        for obj in arr:
            members.append(User.Member(self.fastcord, obj, self.id))
        
        return members
