import fastcord

token = ""
prefix = "/"
bot = fastcord.Fastcord(token, prefix)

class Ping(fastcord.Command):

    def __init__(self):
        super().__init__("ping", "This is a description. It can be used when making a help command.")
    
    def invoke(self, bot, msg, args):
        msg.channel.send("Pong!")

class Say(fastcord.Command):

    def __init__(self):
        super().__init__("say", args=[ "text" ])

    def invoke(self, bot, msg, args):
        msg.channel.send(args["text"])

class Add(fastcord.Command):

    def __init__(self):
        super().__init__("add", args=[ "one", "two" ])
    
    def invoke(self, bot, msg, args):
        msg.channel.send(f"{args['one']} + {args['two']} = {int(args['one']) + int(args['two'])}")

@bot.on_event("ready")
def on_ready():
    bot.load_command(Ping())
    bot.load_command(Say())
    bot.load_command(Add())

bot.run()
