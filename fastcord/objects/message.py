from .user import User
from .embed import Embed
from .reaction import Reaction
from .attachment import Attachment
from .channel import Channel
from ..utils.dict import try_get_value
from ..utils.http import get, patch

class Message:

    def __init__(self, fastcord, obj):
        from .channel import Channel

        self.fastcord = fastcord
        self.id = obj["id"]
        self.channel = Channel(fastcord, get(f"{fastcord.api}/channels/{obj['channel_id']}",
            { "Authorization": "Bot " + fastcord.token }))
        self.author = User(fastcord, obj["author"]) if "webhook_id" not in obj["author"] else None
        self.content = obj["content"]
        self.tts = obj["tts"]
        self.timestamp = obj["timestamp"]
        self.pinned = obj["pinned"]

        self.attachments = []
        self.embeds = []
        self.reactions = []

        for item in obj["attachments"]:
            self.attachments.append(Attachment(fastcord, item))
        
        for item in obj["embeds"]:
            self.attachments.append(Embed(fastcord, item))

        if try_get_value(obj, "reactions") != None:
            for item in obj["reactions"]:
                self.attachments.append(Reaction(fastcord, item))

    def edit(self, content = None, embed = None):
        body = { }

        if content != None:
            body["content"] = content

        if embed != None:
            if type(embed) == dict:
                body["embed"] = embed
            elif type(embed) == Embed:
                body["embed"] = embed.embed

        return Message(self.fastcord,
            patch(f"{self.fastcord.api}/channels/{self.channel.id}/messages/{self.id}", body, { "Authorization": "Bot " + self.fastcord.token }))
