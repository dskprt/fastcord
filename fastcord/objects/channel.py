from enum import Enum
from .guild import Guild
from .message import Message
from ..utils.http import *

class Channel:

    def __init__(self, fastcord, channel):
        self.fastcord = fastcord
        self.id = channel["id"]
        #self.type = ChannelType(int(channel["type"]))
        self.guild_id = channel["guild_id"] or None
        self.position = channel["position"] or None
        self.nsfw = channel["nsfw"] or None
        self.name = channel["name"] or None
        self.topic = channel["topic"] or None
        #self.bitrate = channel["bitrate"] or None
        #self.limit = channel["user_limit"] or None
        #self.slowmode = channel["rate_limit_per_user"] or None
        #self.recipients = channel["recipients"] or None
        #self.owner_id = channel["owner_id"] or None
    
    def get_guild(self):
        return Guild(self.fastcord, get("https://discordapp.com/api/guilds/" + self.guild_id, { "Authorization": "Bot " + self.fastcord.token }))
    
    def send(self, contents = None, embed = {}):
        post("https://discordapp.com/api/channels/" + self.id + "/messages",
            { "content": contents, "embed": embed },
            { "Authorization": "Bot " + self.fastcord.token })

    def get_message(self, message_id):
        return Message(self.fastcord, get("https://discordapp.com/api/channels/" + self.id + "/messages/" + message_id,
            { "Authorization": "Bot " + self.fastcord.token }))

    class ChannelType(Enum):

        TEXT = 0
        DM = 1
        VOICE = 2
        GROUP_DM = 3
        CATEGORY = 4
        NEWS = 5
        STORE = 6
