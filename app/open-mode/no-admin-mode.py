import os
from discord.ext import commands
from dotenv import load_dotenv
from reddit_brain import get_memes
import discord
from db_commands import insert_user

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MEME_CHANNEL = os.getenv('MEME_CHANNEL')

bot = commands.Bot(command_prefix='!')

@bot.command(name='memenow', help='Gets a random CS/Cybersecurity meme')
async def meme_generator(ctx):
    """Gets a random CS/Cybersecurity meme from Reddit."""
    
    # Add syntax to see if user is registered, else, display a message to the user
    # explaining this and give him/her the command to register.
    
    meme = get_memes()
    await ctx.author.send('Here is your meme: ')
    await ctx.author.send(meme["meme_title"])
    await ctx.author.send(meme["meme_link"])
    
    text = """Please react to this message with a 👍 if you approve the meme so I can post it on the meme channel. 
    Oherwise, if you think this meme is not appropiate for the club (cursing is fine, 
    we are all adults, but no nudity/racist/discriminative memes should be approved. Basically nothing that you would show to the club in an in-person meeting.) or simply not funny, please
    react to this message with a 👎 and I will add the meme to the disallowed memes database"""
    
    target_message = await ctx.author.send(text)
    @bot.event
    async def on_raw_reaction_add(payload):
        """Determines whether a meme is approved to be sent to the meme channel or not based on a reaction emoji by the bot admin."""
        
        channel = bot.get_channel(int(MEME_CHANNEL))
        current_message = payload.message_id

        if str(payload.emoji) == "👍" and current_message == target_message.id:
            await ctx.author.send("Okay, approved, I will send the meme to the meme channel")
            await channel.send(meme["meme_title"])
            await channel.send(meme["meme_link"])
            await channel.send("Approved by: {author}".format(author = ctx.message.author.name))

        elif str(payload.emoji) == "👎" and current_message == target_message.id:
            await ctx.author.send("Bad Meme! Let me look for another meme.")


@bot.command(name='register', help='Registers a user so this user can perform commands against this bot')
async def register_user(ctx):
    """Registers a user so this user can perform commands against this bot."""
    
    user_id = ctx.message.author.id
    username = ctx.message.author.name
    insert_user(user_id, username, )
    await ctx.author.send('You are now registered!')
    

bot.run(TOKEN)