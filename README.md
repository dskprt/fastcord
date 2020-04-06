![fastcord](../assets/logo.png?raw=true)  
![[PyPI version shields.io](https://img.shields.io/pypi/v/fastcord.svg)](https://pypi.python.org/pypi/fastcord/)  
just another discord api wrapper for writing bots

[Website](https://dskprt.github.io/fastcord) | [Documentation](https://github.com/dskprt/fastcord/wiki/Documentation)

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
More examples are available in the `examples` directory.
