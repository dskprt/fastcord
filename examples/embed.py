import fastcord

token = ""

def on_message(msg):
    if msg["content"] == "!ping":
        # https://discordapp.com/developers/docs/resources/channel#embed-object
        bot.send_message(None, msg["channel_id"], embed={
            "title": "Embed title",
            "description": "Embed description"
        })

bot = fastcord.Fastcord(token, on_message=on_message)
bot.run()
