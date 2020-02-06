class User:

    def __init__(self, fastcord, user):
        self.id = user["id"]
        self.username = user["username"]
        self.discriminator = user["discriminator"]
        self.avatar = f"https://cdn.discordapp.com/avatars/{self.id}/{user['avatar']}.png"
        #self.bot = user["bot"] or False
