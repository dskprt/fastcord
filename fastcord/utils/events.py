from functools import wraps

class Events:
    def __init__(self, verbose = False):
        self.events = {}
        self.verbose = verbose
    
    def on_event(self, event="__dummy__"):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if func != "__dummy__" and func not in self.events:
                    self.events[func] = args[0]
                
                return args[0]
            return wrapper
        
        decorator.events = self.events
        return decorator

    def call(self, event, *args):
        for k, v in self.events.items():
            if k == "__dummy__":
                continue
            
            if k == event:
                try:
                    self.events[k](*args)
                except TypeError as e:
                    if self.verbose:
                        print("Unable to execute event: " + str(e))

                    continue
