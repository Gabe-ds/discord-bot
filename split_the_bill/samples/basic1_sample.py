import discord

from dotenv import load_dotenv
load_dotenv()

import os
TOKEN = os.getenv('TESTKIRK_TOKEN')


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Loggend on as {self.user}!")
        
    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")
        
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)