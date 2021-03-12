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
BOT_OWNER_DM_CHANNEL_ID = os.getenv('BOT_OWNER_DM_CHANNEL_ID')


@bot.command(name='memenow!', help='Gets a random CS/Cybersecurity meme')
async def meme_generator(ctx):
    meme = get_memes()

    await ctx.send('Here is your meme: ')
    await ctx.send(meme["meme_title"])
    target_message = await ctx.send(meme["meme_link"])
    # messages = await ctx.history(limit=10000).flatten()
    # for msg in messages:
    # 	if msg.id == target_message.id:
    # 		cache_msg = discord.utils.get(bot.cached_messages, id=target_message.id)
    # 		print("LINE 28")
    # 		reactions = cache_msg.reactions
    # 		print(len(reactions))
    # 		for reaction in reactions:
    # 			print("reactions!")
    # for reaction in msg.reactions:
    # 	on_reaction_add(reaction, DISCORD_DM_USER)


@bot.event
async def on_raw_reaction_add(payload):
    """Gives a role based on a reaction emoji."""
    channel = bot.get_channel(payload.channel_id)
    if str(payload.emoji) == "👍" and str(payload.channel_id) == str(BOT_OWNER_DM_CHANNEL_ID):
        await channel.send("Okay, approved, I will send the meme to the channel")
    elif str(payload.emoji) == "👎" and str(payload.channel_id) == str(BOT_OWNER_DM_CHANNEL_ID):
        await channel.send("Denied, let me look for another meme")
        
    # Make sure that the message the user is reacting to is the one we care about
    # if payload.message
# @bot.event
# async def on_reaction_add(reaction, user):
# 	if bot.is_owner(user) and str(reaction.emoji) == '👍':
# 		print("Good mesasge")
# 		# await ctx.send("Okay, approved, I will send the meme to the channel")
# 	elif bot.is_owner(user) and str(reaction.emoji) == '👎':
# 		# await ctx.send("Denied, let me look for another meme")
# 		print("Bad Message")
# 	else:
# 		print("BYE!")
# 		return


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

# @bot.event

bot.run(TOKEN)
