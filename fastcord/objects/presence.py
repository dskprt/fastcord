import builtins
from enum import Enum
from .activity import Activity
from ..utils.dict import try_get_value

class Presence():

    def __init__(self, fastcord=None, obj=None):
        if(obj == None):
            self.presence = {}
            self.presence["since"] = None
            self.presence["game"] = None
            self.presence["status"] = None
            self.presence["afk"] = False
            return None
        
        self.presence = obj

        self._activity = Activity(fastcord, obj["name"])
        self._status = Status(obj["status"])
    
    def activity(self, activity):
        self.presence["game"] = activity.activity
        return self
    
    def status(self, status):
        self.presence["status"] = status.value
        return self
    
class Status(Enum):

    ONLINE = "online"
    DND = "dnd"
    IDLE = "idle"
    INVISIBLE = "invisible"
    OFFLINE = "offline"
