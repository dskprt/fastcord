class Guild:

    def __init__(self, fastcord, guild):
        self.fastcord = fastcord
        self.id = guild["id"]
        self.name = guild["name"]
        self.icon = f"https://cdn.discordapp.com/icons/{self.id}/{guild['icon']}.png"
        self.owner_id = guild["owner_id"]
