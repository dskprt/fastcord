from ..utils.dict import try_get_value

class Embed:

    def __init__(self, fastcord, obj):
        self.title = try_get_value(obj, "title")
        self.description = try_get_value(obj, "description")
        self.url = try_get_value(obj, "url")
        self.color = try_get_value(obj, "color")
        self.timestamp = try_get_value(obj, "timestamp")

        self.footer = None
        self.image = None
        self.thumbnail = None
        self.video = None
        self.provider = None
        self.author = None
        self.fields = []
        
        if(try_get_value(obj, "footer") != None):
            self.footer = self.Footer(obj["footer"])

        if(try_get_value(obj, "image") != None):
            self.image = self.Image(obj["image"])

        if(try_get_value(obj, "thumbnail") != None):
            self.thumbnail = self.Thumbnail(obj["thumbnail"])
        
        if(try_get_value(obj, "video") != None):
            self.video = self.Video(obj["video"])
        
        if(try_get_value(obj, "provider") != None):
            self.provider = self.Provider(obj["provider"])
        
        if(try_get_value(obj, "author") != None):
            self.author = self.Author(obj["author"])
        
        if(try_get_value(obj, "fields") != None):
            for item in obj["fields"]:
                self.fields.append(self.Field(item))

    class Footer:
        
        def __init__(self, obj):
            self.text = obj["text"]
            self.icon = try_get_value(obj, "icon_url")
    
    class Field:
        
        def __init__(self, obj):
            self.name = obj["name"]
            self.value = obj["value"]

    class Author:
        
        def __init__(self, obj):
            self.name = try_get_value(obj, "name")
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
