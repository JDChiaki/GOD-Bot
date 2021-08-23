import os
import discord
import random
from keep_alive import keep_alive

client = discord.Client()
res = open('res.txt').read().splitlines()
kws = open('kws.txt').read().splitlines()
cts = open('cts.txt').read().splitlines()
rms = res + cts

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	msg = message.content

	if any(word in msg for word in kws):
		await message.channel.send(random.choice(rms))
	
	if msg.startswith('ca?t '):
		await message.channel.send(random.choice(cts))

my_secret = os.environ['TOKEN']
client.run(my_secret)
