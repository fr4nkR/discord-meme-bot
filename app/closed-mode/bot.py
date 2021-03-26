import os
from discord.ext import commands
from dotenv import load_dotenv
from reddit_brain import get_memes
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_DM_USER = os.getenv('DISCORD_DM_USER')
bot = commands.Bot(command_prefix='!')
BOT_OWNER_DM_CHANNEL_ID = os.getenv('BOT_OWNER_DM_CHANNEL_ID')

@bot.command(name='memenow', help='Gets a random CS/Cybersecurity meme')
async def meme_generator(ctx):
    """Gets a random meme from Reddit."""
    
    if str(ctx.channel.id) == str(BOT_OWNER_DM_CHANNEL_ID):
        channel = bot.get_channel(payload.channel_id)
        meme = get_memes()
        await ctx.send('Here is your meme: ')
        await ctx.send(meme["meme_title"])
        target_message = await ctx.send(meme["meme_link"])
        
        @bot.event
        async def on_raw_reaction_add(payload):
            """Determines whether a meme is approved to be sent to the meme channel or not based on a reaction emoji by the bot admin."""
            
            channel = bot.get_channel(payload.channel_id)
            current_message = payload.message_id
            if str(payload.emoji) == "👍" and current_message == target_message.id:
                await channel.send("Okay, approved, I will send the meme to the channel")
            elif str(payload.emoji) == "👎" and current_message == target_message.id:
                await channel.send("Denied, let me look for another meme")
    else:
        await ctx.send('This is an admin only command, sorry.')

bot.run(TOKEN)