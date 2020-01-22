import fastcord

token = ""

def on_message(msg):
    if msg["content"] == "!embed":

        # https://discordapp.com/developers/docs/resources/channel#embed-object
        bot.send_message(msg["channel_id"], embed={
            "title": "Embed title",
            "description": "Embed description",
            "image": {
                "url": "https://discordapp.com/assets/28174a34e77bb5e5310ced9f95cb480b.png"
            }
        })

bot = fastcord.Fastcord(token, on_message=on_message)
bot.run()
