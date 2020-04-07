---
layout: default
---

Welcome to the fastcord website!
**fastcord** is a simple Discord API wrapper for writing bots.

[Documentation](docs.md)

## Installing  
**Python 3.6 or higher is required.**
```
python -m pip install fastcord
```
To install the latest development version (might not be stable):
```
git clone https://github.com/dskprt/fastcord.git
cd fastcord
python -m pip install .
```

## Simple bot
```python
import fastcord

bot = fastcord.Fastcord("TOKEN")

@bot.on_event("message")
def on_message(msg):
    if msg.content == "!ping":
        msg.channel.send("Pong!")

bot.run()
```
More examples are available [here](https://github.com/dskprt/fastcord/tree/master/examples).
