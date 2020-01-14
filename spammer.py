#Coded By Dr3xey From OffensiveEncode Org.
import discord
import asyncio
import sys

                                                  
print("Usage: python spammer.py token channel text")

client = discord.Client()
token = sys.argv[1]
DiscordChannel = sys.argv[2]
spam_text = sys.argv[3]

@client.event
async def on_message(message):
    if message.content == "start":
        while True:
            await message.channel.send(spam_text)
    if message.content == "stop":
        await client.close()
        sys.exit()

client.run(token, bot=False)
