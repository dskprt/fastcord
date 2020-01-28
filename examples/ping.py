import fastcord

token = ""
bot = fastcord.Fastcord(token)

@bot.on_event("message")
def on_message(msg):
    if msg["content"] == "!ping":
        bot.send_message(msg["channel_id"], "Pong!")

bot.run()
