import fastcord

token = ""
bot = fastcord.Fastcord(token)

@bot.on_event("message")
def on_message(msg):
    if msg.content == "!embed":

        # https://discordapp.com/developers/docs/resources/channel#embed-object
        msg.channel.send(embed={
            "title": "Embed title",
            "description": "Embed description",
            "image": {
                "url": "https://discordapp.com/assets/28174a34e77bb5e5310ced9f95cb480b.png"
            }
        })
        
bot.run()
