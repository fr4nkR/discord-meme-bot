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



@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
	dice = [
		str(random.choice(range(1, number_of_sides + 1)))
		for _ in range(number_of_dice)
	]
	await ctx.send(', '.join(dice))
	
# @bot.event

bot.run(TOKEN)
