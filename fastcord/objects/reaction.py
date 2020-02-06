from .emoji import Emoji

class Reaction:

    def __init__(self, fastcord, obj):
        self.count = obj["count"]
        self.reacted = obj["me"]
        self.emoji = Emoji(fastcord, obj["emoji"])
