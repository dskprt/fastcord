import fastcord

token = ""
bot = fastcord.Fastcord(token)

@bot.on_event("message")
def on_message(msg):
    if msg["content"] == "!avatar":
        info = bot.get_user_info(msg["author"]["id"])

        bot.send_message(msg["channel_id"], embed={
            "title": f"{info['username']}#{info['discriminator']}",
            "image": {
                "url": f"https://cdn.discordapp.com/avatars/{info['id']}/{info['avatar']}.png?size=256"
            }
        })

bot.run()