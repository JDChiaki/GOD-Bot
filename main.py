import os
import discord
from discord.ext import commands
from role import Role
from keep_alive import keep_alive

intents = discord.Intents(messages=True, members=True, guilds=True, reactions=True)
bot = commands.Bot(command_prefix='god! ', case_insensitive=True, help_command=None, intents=intents)

@bot.event
async def on_ready():
	print(f'We have logged in as {bot.user}')


async def setup():
    await bot.wait_until_ready()
    bot.add_cog(Role(bot))

bot.loop.create_task(setup())

keep_alive()
my_secret = os.environ['TOKEN']
bot.run(my_secret)
