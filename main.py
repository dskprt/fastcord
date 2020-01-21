import websocket
import heartbeat
import json
import data
from threading import Thread

def on_message(ws, msg):
    print("MESSAGE: " + msg)
    msg = json.loads(msg)

    if msg["op"] == 10: # opcode 10 hello
        data.interval = msg["d"]["heartbeat_interval"]
        t = Thread(target=heartbeat.run)
        t.start()

        ws.send(json.dumps({
            "op": 2,
            "d": {
                "token": data.config["TOKEN"],
                "properties": {
                    "$os": "android",
                    "$browser": "botnolib",
                    "$device": "botnolib"
                }
            }
        }))

if __name__ == "__main__":
    data.config = json.load(open("config.json", "r"))

    data.ws = websocket.WebSocketApp("wss://gateway.discord.gg/?v=6&encoding=json",
        on_message=on_message)
    data.ws.run_forever()