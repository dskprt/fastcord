import fastcord

token = ""
bot = fastcord.Fastcord(token)

@bot.on_event("message")
def on_message(msg):
    if msg.content == "!ping":
        msg.channel.send("Pong!")

bot.run()
