from ..utils.dict import try_get_value

class User:

    def __init__(self, fastcord, obj):
        self.id = obj["id"]
        self.username = obj["username"]
        self.discriminator = obj["discriminator"]
        self.avatar = f"https://cdn.discordapp.com/avatars/{self.id}/{obj['avatar']}.png"
        
        self.bot = False

        if(try_get_value(obj, "bot") != None):
            self.bot = obj["bot"]
