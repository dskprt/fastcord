import time
from enum import Enum
from ..utils.dict import try_get_value

class Activity():

    def __init__(self, name=None, _type=None, fastcord=None, obj=None):
        if(obj == None):
            self.activity = {}
            self.activity["name"] = "fastcord"
            self.activity["type"] = 0
            
            if(name != None):
                self.activity["name"] = name
            
            if(_type != None):
                self.activity["type"] = _type.value

            return None

        self.activity = obj

        self._name = obj["name"]
        self._type = ActivityType(obj["type"])
        self._url = try_get_value(obj, "url")
        self._start = try_get_value(try_get_value(obj, "timestamps"), "start")
        self._end = try_get_value(try_get_value(obj, "timestamps"), "end")
        self._app_id = try_get_value(obj, "application_id")
        self._details = try_get_value(obj, "details")
        self._state = try_get_value(obj, "state")
        self._large_image = try_get_value(try_get_value(obj, "assets"), "large_image")
        self._large_text = try_get_value(try_get_value(obj, "assets"), "large_text")
        self._small_image = try_get_value(try_get_value(obj, "assets"), "small_image")
        self._small_text = try_get_value(try_get_value(obj, "assets"), "small_text")
    
    def name(self, name):
        self.activity["name"] = name
        return self
    
    def type(self, activity_type):
        self.activity["type"] = activity_type.value
        return self
    
    def url(self, url):
        if(self.activity["type"] != 1): return

        self.activity["url"] = url
        return self

class ActivityType(Enum):

    GAME = 0
    STREAMING = 1
    LISTENING = 2
    CUSTOM = 4