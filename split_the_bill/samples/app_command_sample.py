import discord
from discord import app_commands

from dotenv import load_dotenv
load_dotenv()

import os
TOKEN = os.getenv('TESTKIRK_TOKEN')


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        
        self.tree = app_commands.CommandTree(self)
        
    async def setup_hook(self):
        # self.tree.copy_global_to()
        await self.tree.sync()

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    
@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')


client.run(TOKEN)