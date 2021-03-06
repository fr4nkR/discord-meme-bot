# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv
from reddit_brain import get_memes
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_DM_USER = os.getenv('DISCORD_DM_USER')
intents = discord.Intents().all()
#bot = commands.Bot(command_prefix='!', intents=intents)
bot = commands.Bot(command_prefix='!')
EMOJI = "👍"
@bot.command(name='memenow!', help='Gets a random CS/Cybersecurity meme')
async def meme_generator(ctx):
	meme = get_memes()

	await ctx.send('Here is your meme: ')
	await ctx.send(meme["meme_title"])
	target_message = await ctx.send(meme["meme_link"])
	async for msg in ctx.history(limit=10000):
		if msg.id == target_message.id:
			# cache_msg = discord.utils.get(bot.messages, id=target_message.id)
			for reaction in msg.reactions:
				print("GOOD!")
				await on_reaction_add(reaction, DISCORD_DM_USER, ctx)

# @bot.event
async def on_reaction_add(reaction, user, ctx, message_id):
    if bot.is_owner(user) and str(reaction.emoji) == '👍':
        await ctx.send("Okay, approved, I will send the meme to the channel")
    elif bot.is_owner(user) and str(reaction.emoji) == '👎':
        await ctx.send("Denied, let me look for another meme")
    else:
        return
  
@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
	dice = [
		str(random.choice(range(1, number_of_sides + 1)))
		for _ in range(number_of_dice)
	]
	await ctx.send(', '.join(dice))
	
# @bot.event

bot.run(TOKEN)
