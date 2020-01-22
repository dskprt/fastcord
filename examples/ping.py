import fastcord

token = ""

def on_message(msg):
    if msg["content"] == "!ping":
        bot.send_message(msg["channel_id"], "Pong!")

bot = fastcord.Fastcord(token, von_message=on_message)
bot.run()
