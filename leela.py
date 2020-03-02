import discord, random
from discord.ext import commands
import asyncio
import os

client=commands.Bot(command_prefix='"')
client.remove_command('help')

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name='"help'))


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None):
    if not member:
        await ctx.send('Please mention a member')
        return
    await member.ban()
    await ctx.send(f'{member.display_name} was banned from the server')
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member=None):
    if not member:
        await ctx.send('Please mention a member')
        return
    await member.kick()
    await ctx.send(f'{member.display_name} was kicked from the server      :wave:')
@client.command(aliases=['bc'])
async def broadcast(ctx, *, msg):
    await ctx.send(msg)
    await ctx.message.delete()
@client.command(aliases=['rbc'])
async def richbroadcast(ctx, *, msg):
    embed=discord.Embed()
    embed.title='Broadcast Message'
    embed.description=msg
    await ctx.send(embed=embed)
    await ctx.message.delete()
@client.command()
async def help(ctx):
    embed=discord.Embed()
    embed.title='Help'
    embed.description='Welcome to RedZone! Please read #rules.. Commands are: help, richbroadcast, broadcast, kick, ban, userinfo, settings. '
    await ctx.send(embed=embed)
@client.command()
async def dates(ctx):

  await ctx.send('Sent Dates in DMs!')
  await ctx.author.send('No dates right now!')

@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(client.latency, 1)))

@client.command()
async def userinfo(ctx, member: discord.Member):
 
    roles = [role for role in member.roles]
 
    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
 
    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
 
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Guild name:", value=member.display_name)
 
    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
 
    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top role:", value=member.top_role.mention)
 
    embed.add_field(name="Bot?", value=member.bot)
 
    await ctx.send(embed=embed)

@client.command()
async def settings(ctx):
  await ctx.send("Comming soon!")





client.run(os.getenv('TOKEN'))
