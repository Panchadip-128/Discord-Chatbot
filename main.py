# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot
#public keye98c4f770a7brettuu11112314c4af844e54d9b7fcb34068340d56e67038bea3aaf55600bab (Changed for privacy)
#app id 12471422740146422870008 (Changed for privacy)




import os

import discord

class MyClient(discord.Client);
  async def on_ready(self):
      print(f'Logged on as {self.user}!')
  async def on_message(self, message):
      print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True
