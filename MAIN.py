import discord
import os
from discord.ext import commands
from PIL import Image, ImageFilter
from io import BytesIO
import requests
import random
import aiohttp
import time

Bot = commands.Bot(command_prefix='$')


@Bot.event
async def on_ready():
    print("BELLO NO ERRORS")

@Bot.command()
async def hello(ctx):
  await ctx.send('```SUP```')

@Bot.command()
async def report(ctx, description_report=None):
  embed_report = discord.Embed(title = ":warning:Report Succesfully Sent..:warning:", description = f"Bug = {description_report}", color = discord.Colour.gold())
  embed_report.set_image(url = 'https://www.kindpng.com/picc/m/715-7159386_caution-warning-symbol-hd-png-download.png')
  embed_report.set_footer(text = f"Reported By {ctx.author}")

  await ctx.send(embed=embed_report)

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
        snipeEmbed = discord.Embed(title=f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id], color = discord.Colour.blurple())
        snipeEmbed.set_footer(text=f"Deleted by {snipe_message_author[channel.id]}")
        await ctx.send(embed = snipeEmbed)
    except:
        await ctx.send(f"```There are no deleted messages in #{channel.name}```")


@Bot.command()
async def pfp(ctx, member_pfp: discord.Member=None, *,Size=4060):
  if member_pfp == None:
    member_pfp = ctx.author

  embed_pfp = discord.Embed(title = f"pfp of {member_pfp.name}", description = f"Aww {member_pfp.mention} is Cute", color = discord.Colour.blurple())
  embed_pfp.set_footer(text = f"Asked By {ctx.author}", icon_url = ctx.author.avatar_url)
  embed_pfp.set_image(url = member_pfp.avatar_url)

  await ctx.send(embed = embed_pfp)

@Bot.command()
async def ghost(ctx, member_target_ghost: discord.Member=None, *, value_ghost):
  if member_target_ghost == None:
    member_target_ghost = ctx.author
  
  for ghost in range(int(value_ghost) - 1):
    await ctx.send(member_target_ghost.mention)
    await ctx.channel.purge(limit=1)
  await ctx.channel.purge(limit=1)

  embed_ghost_dms = discord.Embed(title = ":warning:Warning:warning:", description = f"{member_target_ghost.mention} \nYou Have Been Ghost Pinged By \n{ctx.author} \nIn #{ctx.channel.name}", color = discord.Colour.gold())
  embed_ghost_dms.set_image(url = 'https://www.kindpng.com/picc/m/715-7159386_caution-warning-symbol-hd-png-download.png')

  await member_target_ghost.send(embed = embed_ghost_dms)

@Bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, value_clear):

  if value_clear == "all":
    embed_clear = discord.Embed(title = f"Clearing {value_clear} Messages...",color = discord.Colour.blurple())
    embed_clear.set_image(url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSa-ur_UZ1ZM4FgGCC-YFgk_nk5V_0tymQV1w&usqp=CAU')
    embed_clear.set_footer(text = f"Command Requsted By {ctx.author}", icon_url = ctx.author.avatar_url)

    embed_cleared = discord.Embed(title = f"{value_clear} Messages Have Been Deleted...",color = discord.Colour.blurple())

    embed_clear.set_footer(text = f"Command Requsted By {ctx.author}", icon_url = ctx.author.avatar_url)

    await ctx.send(embed = embed_clear)
    time.sleep(1.5)
    await ctx.channel.purge()
    time.sleep(1.5)
    await ctx.send(embed = embed_cleared)
    time.sleep(2)
    await ctx.channel.purge(limit = 1)

  else:
    embed_clear = discord.Embed(title = f"Clearing {value_clear} Messages...",color = discord.Colour.blurple())
    embed_clear.set_image(url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSa-ur_UZ1ZM4FgGCC-YFgk_nk5V_0tymQV1w&usqp=CAU')
    embed_clear.set_footer(text = f"Command Requsted By {ctx.author}", icon_url = ctx.author.avatar_url)

    embed_cleared = discord.Embed(title = f"{value_clear} Messages Have Been Deleted...",color = discord.Colour.purple())

    embed_clear.set_footer(text = f"Command Requsted By {ctx.author}", icon_url = ctx.author.avatar_url)

    await ctx.send(embed = embed_clear)
    time.sleep(1.5)
    await ctx.channel.purge(limit=int(value_clear)+2)
    time.sleep(1.5)
    await ctx.send(embed = embed_cleared)
    time.sleep(2)
    await ctx.channel.purge(limit=1)

@Bot.command()
async def cat(ctx):
  url_cat = requests.get("https://api.thecatapi.com/v1/images/search").json()
  embed_cat = discord.Embed(title = "Meow!", description = "#Love cats", color = discord.Colour.blurple())
  embed_cat.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
  cat = url_cat[0]['url']
  embed_cat.set_image(url = cat)
  await ctx.send(embed = embed_cat)

@Bot.command()
async def kitten(ctx):
  url_kitten = requests.get("https://api.thecatapi.com/v1/images/search").json()
  embed_kitten = discord.Embed(title = "Meow!", description = "#Love cats", color = discord.Colour.blurple())
  embed_kitten.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
  kitten = url_kitten[0]['url']
  embed_kitten.set_image(url = kitten)
  await ctx.send(embed = embed_kitten)

@Bot.command()
async def meow(ctx):
  url_meow = requests.get("https://api.thecatapi.com/v1/images/search").json()
  embed_meow = discord.Embed(title = "Meow!", description = "#Love cats", color = discord.Colour.blurple())
  embed_meow.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
  meow = url_meow[0]['url']
  embed_meow.set_image(url = meow)
  await ctx.send(embed = embed_meow)
  
@Bot.command()
async def dog(ctx):
  url_dog = requests.get("https://api.thedogapi.com/v1/images/search").json()
  embed_dog = discord.Embed(title = "Woof!!", description = "#Love Dogs", color = discord.Colour.blurple())
  embed_dog.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
  dog = url_dog[0]['url']
  embed_dog.set_image(url = dog)
  await ctx.send(embed = embed_dog)

@Bot.command()
async def pup(ctx):
  url_pup = requests.get("https://api.thedogapi.com/v1/images/search").json()
  embed_pup = discord.Embed(title = "Woof!!", description = "#Love pups", color = discord.Colour.blurple())
  embed_pup.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
  pup = url_pup[0]['url']
  embed_pup.set_image(url = pup)
  await ctx.send(embed = embed_pup)

@Bot.command()
async def puppy(ctx):
  url_puppy = requests.get("https://api.thedogapi.com/v1/images/search").json()
  embed_puppy = discord.Embed(title = "Woof!!", description = "#Love puppies", color = discord.Colour.blurple())
  embed_puppy.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
  puppy = url_puppy[0]['url']
  embed_puppy.set_image(url = puppy)
  await ctx.send(embed = embed_puppy)

@Bot.command()
async def woof(ctx):
  url_woof = requests.get("https://api.thedogapi.com/v1/images/search").json()
  embed_woof = discord.Embed(title = "Woof!!", description = "#Love puppies", color = discord.Colour.blurple())
  embed_woof.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
  woof = url_woof[0]['url']
  embed_woof.set_image(url = woof)
  await ctx.send(embed = embed_woof)


player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@Bot.command()
async def ttt(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        num = random.randint(1, 2)
        if num == 1:
          await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
          turn = player1
        elif num == 2:
          await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
          turn = player2
          
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@Bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
                if gameOver == True:
                  await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
            elif turn == player2:
                mark = ":o2:"
                if gameOver == True:
                  await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

            
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                  embed_win_tictactoe = discord.Embed()
                  await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@ttt.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")


my_secret = os.environ['Key']

Bot.run(my_secret)
