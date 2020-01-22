import fastcord

token = ""

def on_message(msg):
    if msg["content"] == "!ping":
        bot.send_message("Pong!", msg["channel_id"])

bot = fastcord.Fastcord(token, on_message=on_message)
bot.run()
