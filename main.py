import discord
from discord.ext import commands
import asyncio
from SpecialRandoms import *
import config as c

sr = SpecialRandoms
prefix = "!"
bot = commands.Bot(command_prefix=prefix)
joinLink = "https://discordapp.com/oauth2/authorize?client_id="+c.ClienId+"&permissions="+c.PermissionsInt+"&scope=bot"


@bot.event
async def on_ready():
    print("Ready")
    print("Join Link: " + joinLink)


@bot.event
async def on_message(message):
    #print("The message's content was", message.content)
    await bot.process_commands(message)
    
@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)

@bot.command()
async def combo(ctx, strLen:int, type:int, count:int):
    '''
    Generates a certain number of username and password combos
    Takes 3 arguments. Length, then type, then count
    Type 1 = formatting. Type 2 = regular combo
    
    
    Example 1:
    !combo 12 1 1               Generates 1 formatted combo of 12 character long user and pass like such:
    ■▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬■
    Username: 5N7vaIBsbt8w
    
    Password: v0<h-$KKZd)2
    ■▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬■
    
    
    Example 2: 
    !combo 12 2 3               Generates 3 formatted combos of 12 character long user and pass like such:
    XKnYhndSnijy:3JEx1l718jlA
    2fNWJGNEej0S:1>u]z[g+kBg]
​    lnTJNHCPPRiH:<3A}k[hDM!8$
    '''
    title = 'Title'
    description = 'Description'
    msg = discord.Embed(title=title, description=description, color=0x00ff00)
    for f in SpecialRandoms.Combo(strLen, type, count):
        msg.add_field(name='\u200b', value=f, inline=False)
    await ctx.send(embed = msg)
    
    #await ctx.send('\u200B'+'```'+sr.Combo(len, type, count)+'```')
    #await ctx.send('You sent {} and {}'.format(len, type))
    

@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

bot.run(c.ClientToken)


#for f in SpecialRandoms.Combo(5, 1, 3):
#        print (f)