import discord

#TOKEN = ""
#TEXTCHANNEL = ""
client = discord.Client()

text_chat = discord.Object(TEXTCHANNEL)

@client.event
async def on_ready():
    msg = "LOLbotがログインしたよ！"
    await client.send_message(text_chat,msg)

@client.event
async def on_member_update(before, after):
    if before.game != after.game and before.game == None:
        msg = after.display_name + "が" + str(after.game) + "を開始したよ！"
        await client.send_message(text_chat,msg)

@client.event
async def on_voice_state_update(before, after):
    if before.voice_channel == None:
        msg = after.display_name + "が" + after.voice_channel.name + "に参加したよ！"
        await client.send_message(text_chat,msg)

client.run(TOKEN)
