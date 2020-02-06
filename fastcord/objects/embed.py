class Embed:

    def __init__(self, fastcord, obj):
        self.title = obj["title"] or None
        self.description = obj["description"] or None
        self.url = obj["url"] or None
        self.color = obj["color"] or None
