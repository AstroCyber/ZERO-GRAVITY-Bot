import discord
import os
from discord.ext import commands
from PIL import Image, ImageFilter
from io import BytesIO
import requests

Bot = commands.Bot(command_prefix='?')


@Bot.event
async def on_ready():
    print("BELLO NO ERRORS")

@Bot.command()
async def hello(ctx):
  await ctx.send('```SUP```')


snipe_message_author = {}
snipe_message_content = {}
 
@Bot.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]
 
@Bot.command()
async def snipe(ctx):
    channel = ctx.channel 
    try:
        snipeEmbed = discord.Embed(title=f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id], color = discord.Colour.purple())
        snipeEmbed.set_footer(text=f"Deleted by {snipe_message_author[channel.id]}")
        await ctx.send(embed = snipeEmbed)
    except:
        await ctx.send(f"```There are no deleted messages in #{channel.name}```")


@Bot.command()
async def pfp(ctx, member_pfp: discord.Member=None, *,Size=4096):
  if member_pfp == None:
    member_pfp = ctx.author

  embed_pfp = discord.Embed(title = f"pfp of {member_pfp.name}", description = f"Aww {member_pfp.mention} is Cute", color = discord.Colour.purple())
  embed_pfp.set_footer(text = f"Asked By {ctx.author}", icon_url = ctx.author.avatar_url)
  embed_pfp.set_image(url = member_pfp.avatar_url)

  await ctx.send(embed = embed_pfp)

@Bot.command()
async def cat(ctx):
  url_cat = requests.get("https://api.thecatapi.com/v1/images/search").json()
  await ctx.send(url_cat[0]['url'])


@Bot.command()
async def ghost(ctx, member_target_ghost: discord.Member=None, *, value_ghost):
  if member_target_ghost == None:
    member_target_ghost = ctx.author
  
  for ghost in range(int(value_ghost)):
    await ctx.send(member_target_ghost.mention)
    await ctx.channel.purge(limit=1)
  
  
  
  member_target_ghost.send()


Bot.run(my_secret)
