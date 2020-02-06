import fastcord

token = ""
bot = fastcord.Fastcord(token)

@bot.on_event("message")
def on_message(msg):
    if msg.content == "!avatar":
        info = bot.get_user(msg.author.id)

        msg.channel.send(embed={
            "title": f"{info.username}#{info.discriminator}",
            "image": {
                "url": info.avatar + "?size=256"
            }
        })

bot.run()
