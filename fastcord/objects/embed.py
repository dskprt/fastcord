from ..utils.dict import try_get_value
from ..utils.color import int_from_rgb
from ..utils.date import to_iso8601

class Embed:

    def __init__(self, fastcord=None, obj=None):
        if obj == None:
            self.embed = {}
            self.embed["footer"] = {}
            self.embed["author"] = {}
            self.embed["fields"] = []

            return None

        self.embed = obj
        self._title = try_get_value(obj, "title")
        self._description = try_get_value(obj, "description")
        self._url = try_get_value(obj, "url")
        self._color = try_get_value(obj, "color")
        self._timestamp = try_get_value(obj, "timestamp")

        self._footer = None
        self._image = None
        self._thumbnail = None
        self._video = None
        self._provider = None
        self._author = None
        self._fields = []
        
        if try_get_value(obj, "footer") != None:
            self._footer = self.Footer(obj["footer"])

        if try_get_value(obj, "image") != None:
            self._image = self.Image(obj["image"])

        if try_get_value(obj, "thumbnail") != None:
            self._thumbnail = self.Thumbnail(obj["thumbnail"])
        
        if try_get_value(obj, "video") != None:
            self._video = self.Video(obj["video"])
        
        if try_get_value(obj, "provider") != None:
            self._provider = self.Provider(obj["provider"])
        
        if try_get_value(obj, "author") != None:
            self._author = self.Author(obj["author"])
        
        if try_get_value(obj, "fields") != None:
            for item in obj["fields"]:
                self._fields.append(self.Field(item))
    
    def get_title(self):
        return self._title
    
    def get_description(self):
        return self._description
    
    def get_url(self):
        return self._url
    
    def get_color(self):
        return self._color
    
    def get_timestamp(self):
        return self._timestamp

    def get_footer(self):
        return self._footer

    def get_image(self):
        return self._image
    
    def get_thumbnail(self):
        return self._thumbnail
    
    def get_video(self):
        return self._video
    
    def get_provider(self):
        return self._provider
    
    def get_author(self):
        return self._author
    
    def get_fields(self):
        return self._fields
    
    def title(self, text):
        self.embed["title"] = text
        return self
    
    def description(self, text, override=True):
        if override:
            self.embed["description"] = text
        else:
            self.embed["description"] += text

        return self
    
    def url(self, url):
        self.embed["url"] = url
        return self
    
    def color(self, r, g, b):
        self.embed["color"] = int_from_rgb(r, g, b)
        return self
    
    def time(self, year, month, day, hour, minute, second):
        self.embed["timestamp"] = to_iso8601(year, month, day, hour, minute, second)
        return self
    
    def footer(self, text, icon = None, override = True):
        if override:
            self.embed["footer"]["text"] = text
        else:
            self.embed["footer"]["text"] += text

        if icon != None:
            self.embed["footer"]["icon_url"] = icon
        
        return self
    
    def video(self, url):
        self.embed["video"] = { "url": url }
        return self
    
    def image(self, url):
        self.embed["image"] = { "url": url }
        return self
    
    def thumbnail(self, url):
        self.embed["thumbnail"] = { "url": url }
        return self

    def author(self, name, url = None, icon = None):
        self.embed["author"]["name"] = name

        if url != None: self.embed["author"]["url"] = url
        if icon != None: self.embed["author"]["icon_url"] = icon

        return self
    
    def field(self, name, value, inline=False):
        self.embed["fields"].append({ "name": name, "value": value, "inline": inline })
        return self
    
    def update_field(self, index, name=None, value=None, inline=None):
        if name != None: self.embed["fields"][index]["name"] = name
        if value != None: self.embed["fields"][index]["value"] = value
        if inline != None: self.embed["fields"][index]["inline"] = inline

        return self
    
    def remove_field(self, index):
        del self.embed["fields"][index]
        return self

    class Footer:
        
        def __init__(self, obj):
            self.text = obj["text"]
            self.icon = try_get_value(obj, "icon_url")
    
    class Field:
        
        def __init__(self, obj):
            self.name = obj["name"]
            self.value = obj["value"]
            self.inline = try_get_value(obj, "inline")

    class Author:
        
        def __init__(self, obj):
            self.name = try_get_value(obj, "name")
            self.url = try_get_value(obj, "url")
            self.icon = try_get_value(obj, "icon_url")

    class Provider:
        
        def __init__(self, obj):
            self.name = try_get_value(obj, "name")
            self.url = try_get_value(obj, "url")
    
    class Image:
        
        def __init__(self, obj):
            self.url = try_get_value(obj, "url")

    class Video:
        
        def __init__(self, obj):
            self.url = try_get_value(obj, "url")

    class Thumbnail:
        
        def __init__(self, obj):
            self.url = try_get_value(obj, "url")
