from enum import Enum
from .user import User
from .guild import Guild
from .embed import Embed
from ..utils.http import post, get
from ..utils.dict import try_get_value

class Channel:

    def __init__(self, fastcord, obj):
        self.fastcord = fastcord
        self.id = obj["id"]
        #self.type = ChannelType(obj["type"]) doesn't work for some reason
        self.nsfw = try_get_value(obj, "nsfw")
        self.name = try_get_value(obj, "name")
        self.slowmode = try_get_value(obj, "rate_limit_per_user")

        self.owner = None
        self.guild = None

        if(try_get_value(obj, "owner_id") != None):
            self.owner = User(self.fastcord, get(f"{fastcord.api}/users/{obj['owner_id']}",
                { "Authorization": "Bot " + self.fastcord.token }))
        
        if(try_get_value(obj, "guild_id") != None):
            self.guild = Guild(self.fastcord, get(f"{fastcord.api}/guilds/{obj['guild_id']}",
                { "Authorization": "Bot " + self.fastcord.token }))
    
    def send(self, content = None, embed = None):
        from .message import Message

        body = {}

        if(content != None): body["content"] = content
        
        if(embed != None):
            if(type(embed) == dict):
                body["embed"] = embed
            elif(type(embed) == Embed):
                body["embed"] = embed.embed

        return Message(self.fastcord, post(f"{self.fastcord.api}/channels/{self.id}/messages",
            body,
            { "Authorization": "Bot " + self.fastcord.token }))

    def get_message(self, message_id):
        from .message import Message

        return Message(self.fastcord, get(f"{self.fastcord.api}/channels/{self.id}/messages/{message_id}",
            { "Authorization": "Bot " + self.fastcord.token }))

    class ChannelType(Enum):

        TEXT = 0
        DM = 1
        VOICE = 2
        GROUP_DM = 3
        CATEGORY = 4
        NEWS = 5
        STORE = 6
