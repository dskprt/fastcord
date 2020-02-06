class Attachment:

    def __init__(self, fastcord, obj):
        self.id = obj["id"]
        self.name = obj["filename"]
        self.url = obj["url"]
