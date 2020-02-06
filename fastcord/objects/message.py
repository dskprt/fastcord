from .user import User

class Message:

    def __init__(self, fastcord, msg):
        from .channel import Channel
        from ..http import get

        self.fastcord = fastcord
        self.id = msg["id"]
        self.channel_id = msg["channel_id"]
        self.channel = Channel(fastcord, get("https://discordapp.com/api/channels/" + self.channel_id, { "Authorization": "Bot " + self.fastcord.token }))
        self.author = User(fastcord, msg["author"]) if "webhook_id" not in msg["author"] else None
        self.content = msg["content"]
        self.tts = msg["tts"]
        self.timestamp = msg["timestamp"]
        self.attachments = msg["attachments"]
        self.embed = msg["embeds"]
        #self.reactions = msg["reactions"] or None
        self.pinned = msg["pinned"]
