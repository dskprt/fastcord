from ..utils.color import rgb_from_int

class Role:

    def __init__(self, fastcord, obj):
        self.id = obj["id"]
        self.name = obj["name"]
        self.color = rgb_from_int(obj["color"])
