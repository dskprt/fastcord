import platform
import websocket
import json
import time
import re
import importlib
from threading import Thread
from .utils.events import Events
from .utils.http import *
from .objects.message import Message
from .objects.channel import Channel
from .objects.guild import Guild
from .objects.user import User
from .objects.activity import Activity
from .objects.presence import Presence
from .command.command import Command

class Fastcord:

    api = "https://discordapp.com/api"

    def __init__(self, token, prefix=None, verbose=False):
        self.token = token
        self.prefix = prefix
        self.verbose = verbose
        self.ws = websocket.WebSocketApp("wss://gateway.discord.gg/?v=6&encoding=json",
            on_message=lambda ws, msg: self.on_message(ws, msg), on_close=lambda ws: self.on_close(ws))
        self.resume = False
        self.seq = None
        self.last_msg = None
        self.interval = None
        self.session_id = None
        self.ready = False
        self.events = Events(verbose)
        self.on_event = self.events.on_event()
        self.commands = {}
    
    def run(self):
        self.ws.run_forever()
    
    def heartbeat(self):
        while True:
            if self.verbose:
                print("[sending heartbeat]")
            
            self.ws.send(json.dumps({ "op": 1, "d": self.seq }))

            time.sleep(self.interval / 1000)
    
    def change_presence(self, presence):
        if(type(presence) == Presence):
            presence = presence.presence
        
        if(presence["status"] == None):
            raise TypeError("Presence status must be defined!")

        self.ws.send(json.dumps({
            "op": 3,
            "d": presence
        }))
    
    def change_activity(self, activity):
        if(type(activity) == Activity):
            activity = activity.activity
        
        if(activity["name"] == None or activity["type"] == None):
            raise TypeError("Activity name and type must be defined!")

        self.ws.send(json.dumps({
            "op": 3,
            "d": {
                "since": None,
                "game": activity,
                "status": "online",
                "afk": False
            }
        }))
    
    def get_user(self, user_id):
        return User(self, get(f"{self.api}/users/{user_id}", { "Authorization": "Bot " + self.token }))
    
    def get_guild(self, guild_id):
        return Guild(self, get(f"{self.api}/guilds/{guild_id}", { "Authorization": "Bot " + self.token }))
    
    def get_channel(self, channel_id):
        return Channel(self, get(f"{self.api}/channels/{channel_id}", { "Authorization": "Bot " + self.token }))

    def load_command(self, command):
        self.commands[command.name] = command
    
    def on_message(self, ws, msg):
        if self.verbose:
            print("MESSAGE: " + msg)
        
        msg = json.loads(msg)
        self.last_msg = msg
        
        if msg["s"]:
            self.seq = msg["s"]
        else:
            self.seq = None
        
        if msg["op"] == 0:
            self.events.call("event", msg["t"], msg["d"])

            if msg["t"] == "READY":
                self.session_id = msg["d"]["session_id"]
                self.ready = True

                self.username = msg["d"]["user"]["username"]
                self.id = msg["d"]["user"]["id"]

                self.events.call("ready")
            
            if msg["t"] == "MESSAGE_CREATE":
                msg = Message(self, msg["d"])

                if not self.prefix:
                    s = re.split("\s+", msg.content)

                    if s[0] == f"<@!{self.id}>":
                        for k, v in self.commands.items():
                            if k == s[1]:
                                v.invoke(self, msg)
                                break
                else:
                    s = re.split("\s+", msg.content)

                    if msg.content.startswith(self.prefix):
                        cmd = s[0].replace(self.prefix, "", 1)

                        for k, v in self.commands.items():
                            if k == cmd:
                                v.invoke(self, msg)
                                break

                self.events.call("message", msg)

        if msg["op"] == 9: # opcode 9 invalid session
            time.sleep(5)

            self.interval = msg["d"]["heartbeat_interval"]

            ws.send(json.dumps({
                "op": 2,
                "d": {
                    "token": self.token,
                    "properties": {
                        "$os": platform.system(),
                        "$browser": "fastcord",
                        "$device": "fastcord"
                    }
                }
            }))

        if msg["op"] == 10: # opcode 10 hello
            self.interval = msg["d"]["heartbeat_interval"]

            t = Thread(target=self.heartbeat)
            t.start()

            ws.send(json.dumps({
                "op": 2,
                "d": {
                    "token": self.token,
                    "properties": {
                        "$os": platform.system(),
                        "$browser": "fastcord",
                        "$device": "fastcord"
                    }
                }
            }))

            if self.resume:
                ws.send(json.dumps({
                    "op": 6,
                    "d": {
                        "token": self.token,
                        "session_id": self.session_id,
                        "seq": self.seq
                    }
                }))

                self.resume = False
    
    def on_close(self, ws):
        ws.run_forever()
        ws.send(json.dumps({
            "op": 6,
            "d": {
                "token": self.token,
                "session_id": self.session_id,
                "seq": self.seq
            }
        }))
