import time
import data
import json

def run():
    while True:
        print("sending heartbeat")
        data.ws.send(json.dumps({ "op": 1, "d": None }))
        time.sleep(data.interval / 1000)
