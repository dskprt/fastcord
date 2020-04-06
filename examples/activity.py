import fastcord

token = ""
bot = fastcord.Fastcord(token)

@bot.on_event("ready")
def on_ready(msg):
    bot.change_activity(fastcord.Activity("Hello world!", fastcord.ActivityType.GAME))

bot.run()
