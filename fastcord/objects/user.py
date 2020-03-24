from ..utils.dict import try_get_value
from ..utils.date import from_iso8601
from ..utils.http import patch
from .role import Role

class User:

    def __init__(self, fastcord, obj):
        self.fastcord = fastcord
        self.id = obj["id"]
        self.username = obj["username"]
        self.discriminator = obj["discriminator"]
        self.avatar = f"https://cdn.discordapp.com/avatars/{self.id}/{obj['avatar']}.png"
        
        self.bot = False

        if(try_get_value(obj, "bot") != None):
            self.bot = obj["bot"]
    
    class Member():

        def __init__(self, fastcord, obj, guild_id):
            self.fastcord = fastcord
            self.guild_id = guild_id
            self.user = User(fastcord, obj["user"])
            self.nick = try_get_value(obj, "nick")
            self.joined_at = from_iso8601(obj["joined_at"])

            # self.roles = []

            # for role in obj["roles"]:
            #     self.roles.append(Role(self.fastcord, role))
        
        def set_nickname(self, nick):
            patch(f"{self.fastcord.api}/guilds/{self.guild_id}/members/{self.user.id}", { "nick": nick },
                { "Authorization": "Bot " + self.fastcord.token })
