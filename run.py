import discord
import json


class database:
    def __init__(self):
        pass

    def add_user_to_game(self, user):
        pass

    def xp_gain(self, user, xp):
        pass

    def increase_level(self, level):
        pass



class Game:
    def __init__(self):
        pass

    def message_written(self, username):
        pass

    def item_dropped(self, item):
        pass

    def increase_level(self, level):
        pass



global last_message
last_message = ""

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        print(message.content)
        if message.content == '!join':

        
            try:
                with open(str(message.author) + ".json") as json_file:
                    await message.channel.send("You already joined the game")

            except:
                xp = 10
                await message.channel.send("You have now joined the game " + str(message.author) + " you gained " + str(xp) + "xp")
                data = {
                    "username": str(message.author),
                    "xp": xp,
                    "level": 1
                }

                userdata = json.dumps(data)
                with open(str(message.author) + ".json" , 'a') as f:
                    f.write(userdata)

        if message.content == '!level':
            with open(str(message.author) + ".json") as json_file:
                userdata = json.load(json_file)
                await message.channel.send("You are level " + str(userdata["level"]) + " and have " + str(userdata["xp"]) + " xp")

        if message.content == '!help':
            await message.channel.send("!join - Join the game | !level - See your level")
        
        if message.content == '!youtube':
            await message.channel.send("Check out my youtube https://www.youtube.com/channel/UC8VKko6LOp8yKkT9NuvLaQw")

        if message.content == '!tiktok':
            await message.channel.send("Check out my tiktok https://www.tiktok.com/@sweetkitten90")

        if message.content != last_message:
            with open(str(message.author) + ".json", "r") as json_file:
                userdata = json.load(json_file)
                xp = {"xp": userdata["xp"] + 1}
                userdata.update(xp)
                data = json.dumps(userdata)
                with open(str(message.author) + ".json", "w") as json_file:
                    json_file.write(data)
                    await message.channel.send("You gained 1 xp")
        
        message.content = last_message

client = MyClient()
client.run('token')
