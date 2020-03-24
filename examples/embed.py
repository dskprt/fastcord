import fastcord

token = ""
bot = fastcord.Fastcord(token)

@bot.on_event("message")
def on_message(msg):
    if msg.content == "!embed":
        msg.channel.send(embed=fastcord.Embed()
            .title("Title")
            .description("Description")
            .image("https://discordapp.com/assets/28174a34e77bb5e5310ced9f95cb480b.png")
            .field("Field #1", "Value")
            .field("Inline field #1", "Value", True)
            .field("Inline field #2", "Value", True)
            .footer("Footer"))
        
bot.run()
