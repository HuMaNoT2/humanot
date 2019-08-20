import discord
from discord.ext import commands
from discord import Game
from discord.ext.commands import Bot
import time


TOKEN = 'NTczOTU2NzA2NDMwNzQ2Njcy.XVp7fg.WLi3jEgQtHs85rSo1NMW7eeMq-8' #8
client = commands.Bot(command_prefix='-')
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='-help | HuMaNoT#9882',type=0))
@client.command()
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Commands list')
    embed.add_field(name='-dm',value='Direct Messaging you text you have writen.', inline=False)
    embed.add_field(name='-avatar',value='Showing mentioned user avatar.', inline=False)
    embed.add_field(name='-fliptable',value='Fliping table.', inline=False)
    embed.add_field(name='-fakekick',value='Kicking member.', inline=False)
    embed.add_field(name='-kill',value='Killing member!', inline=False)
    embed.add_field(name='-bc',value='BroadCasting your text.', inline=False)
    embed.add_field(name='-guilds',value="Show guilds where i'm.", inline=False)
    embed.add_field(name='-ping',value='Ping Pong!', inline=False)
    embed.add_field(name='-render',value='Render growtopia world(Locked by wl etc)', inline=False)
    embed.add_field(name='-invite',value='Link to invite bot.', inline=False)
    embed.add_field(name='-whogay',value='Shows real gay!', inline=False)
    embed.add_field(name='-cat',value='Cute cat gif', inline=False)
    embed.add_field(name='-add',value='Adds the numbers you wrote.', inline=False)
    embed.add_field(name='-cookie',value='Send delicious coockie!', inline=False)
    embed.add_field(name='-say',value='Writing your text you wrote.', inline=False)
    embed.add_field(name='-sayline',value='Writing message you wrote but underline.', inline=False)
    embed.set_author(name='Commands list')

    await ctx.send(author, embed=embed)
    
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.set_author(name='Moderation commands list')
    embed.add_field(name='-ban',value='Ban member.', inline=False)
    embed.add_field(name='-kick',value='Kick member.', inline=False)
    embed.add_field(name='-mute',value='Mute member.', inline=False)
    embed.add_field(name='-unmute',value='Unmuting member.', inline=False)

    await ctx.send(author, embed=embed)

@client.command()
async def render(ctx,*,content):
    '''Render growtopia world(Only locked by wl,dl etc)'''
    await ctx.send("https://s3.amazonaws.com/world.growtopiagame.com/" + content + ".png")
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member = None):
    if not member:
        '''Kick a member'''
        await ctx.send("_Please specify a member_")
        return
    await member.kick()
    await ctx.send(f"{member.mention} Was nuked from orbit. it's the only way to be sure. Play nice everybody.")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to kick people")
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member = None):
    '''Ban a member'''
    if not member:
        await ctx.send("_Please specify a member_")
        return
    await member.ban()
    await ctx.send("{member.mention Was nuked from orbit. it's the only way to be sure. Play nice everybody.")
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to ban people")
    
@client.command()
async def avatar(ctx, member: discord.Member):
    show_avatar = discord.Embed(

        color = discord.Color.dark_blue()
    )
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)
    
@client.command()
async def dm(ctx,*,content):
    await ctx.author.send(content)

@client.command()
async def guilds(ctx):
    await ctx.send(f"I'm now in {client.guilds}!")
@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    '''Mute a member'''
    if not member:
        await ctx.send("_Please specify a member_")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to mute people")
        
@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    '''Unmute a member'''
    if not member:
        await ctx.send("_Please specify a member_")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to unmute people")
@client.command()
async def invite(ctx):
    '''Link to invite bot'''
    await ctx.author.send("invite link: \nhttp://bit.ly/humanot")
@client.command()
async def whogay(ctx):
    '''Shows real gay'''
    await ctx.send(":gay_pride_flag:You gay! :gay_pride_flag: ")
@client.command()
async def cat(ctx):
    '''Cute cat gif'''
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
@client.command()
async def add(ctx, a: int, b: int):
    '''adds the numbers you wrote'''
    await ctx.send(a+b)
@client.command()
async def cookie(ctx):
    '''Send delicious coockie'''
    await ctx.send(":cookie:")
@client.command()
async def say(ctx,*,content:str):
    '''Writing your text you wrote'''
    await ctx.send(content)
@client.command()
async def owner(ctx):
    '''Shows the bot owner'''
    await ctx.send("```fix\nBot owner HuMaNoT#9882!\n```")

@client.command()
async def fakekick(ctx, member:discord.Member = None):
    if not member:
        '''Kick a member'''
        await ctx.send("_Please specify a member_")
        return
    await ctx.send(f"{member.mention} Was nuked from orbit. it's the only way to be sure. Play nice everybody.")

@client.command()
async def ping(ctx):
    '''Ping Pong'''
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='')
    embed.add_field(name='Pong',value=':ping_pong:', inline=True)
    await ctx.send(author, embed=embed)

@client.command()
async def fliptable(ctx):
    await ctx.send("(╯°□°）╯︵ ┻━┻")
    
@client.command()
async def sayline(ctx,*,content:str):
    '''writing message you wrote but underline'''
    await ctx.send("__" + content + "__")
@client.command()
async def bc(ctx,*,content):

    author = ctx.message.author
    
    await ctx.send("```BroadCast from >>>```")
    await ctx.send(author)
    await ctx.send("**" + content + "**")
    await ctx.author.send("Succes BroadCasted!")

client.run(TOKEN)

