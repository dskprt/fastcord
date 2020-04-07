---
layout: default
---

# Documentation

- [Fastcord](#fastcord)
- [Events](#events)
  - [Event types](#event-types)
- [Discord Objects](#discord-objects)
  - [Activity](#activity)
  - [Attachment](#attachment)
  - [Channel](#channel)
  - [Embed](#embed)
  - [Emoji](#emoji)
  - [Guild](#guild)
  - [Message](#message)
  - [Presence](#presence)
  - [Reaction](#reaction)
  - [Role](#role)
  - [User](#user)

### Fastcord
`class fastcord.Fastcord(token, verbose=False)`  
Used to create a Fastcord instance to interact with the Discord API  

**Arguments**
  - **token** ([str](https://docs.python.org/3/library/stdtypes.html#str))  
    The Discord application token.
  - **verbose** [Optional] ([bool](https://docs.python.org/3/library/functions.html#bool))  
    Defaults to `False`. When set to `True`, the application will log all messages sent by the websocket.

`token` ([str](https://docs.python.org/3/library/stdtypes.html#str))  
The current bot token.

`verbose` ([bool](https://docs.python.org/3/library/functions.html#bool))  
Whether or not the application should log all the messages sent by the websocket.

`ws` (websocket.WebSocketApp)  
The websocket that is used to communicate with the Discord gateway.

`run()`  
Starts the websocket.

`change_presence(presence)`  
Changes the bots presence. Used to change the bot's status and/or activity.

  - **Arguments**
    - **presence** ([fastcord.Presence](#presence))  
    The presence that should be changed to.

`change_activity(activity)`  
Changes the bots activity.

  - **Arguments**
    - **activity** ([fastcord.Activity](#activity))  
    The activity that should be changed to.

`get_user(user_id)` ([fastcord.User](#user))  
Gets a Discord user by their ID.

  - **Arguments**
    - **user_id** ([int](https://docs.python.org/3/library/functions.html#int))  
    The users ID.

`get_guild(guild_id)` ([fastcord.Guild](#guild))  
Gets a Discord guild by its ID.

  - **Arguments**
    - **guild_id** ([int](https://docs.python.org/3/library/functions.html#int))  
    The guilds ID.

`get_channel(channel_id)` ([fastcord.Channel](#channel))  
Gets a Discord channel by its ID.

  - **Arguments**
    - **channel_id** ([int](https://docs.python.org/3/library/functions.html#int))  
    The channels ID.

### Events
How to use events:
```python
import fastcord

bot = fastcord.Fastcord(TOKEN)

@bot.on_event(EVENT_TYPE)
def on_some_event(ARGS?):
    # do something

bot.run()
```

#### Event types
`message`
Called when a message is sent.
   - **Arguments**
     - ([fastcord.Message](#message))  
     The message.

`ready`
Called when the bot is ready.

### Discord Objects
Note: Discord objects **SHOULD NOT** be created manually!

coming soontm

#### Activity
#### Attachment
#### Channel
#### Embed
#### Emoji
#### Guild
#### Message
#### Presence
#### Reaction
#### Role
#### User
