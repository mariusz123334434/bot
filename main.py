import discord
from discord.ext import commands

# Initialize bot with command prefix
bot = commands.Bot(command_prefix='!')

# Helper function to send help message
def help_message():
    return "Available commands: !ban, !kick, !warn, !mute, !ambulance, !police, !fire, !pomoc, !kod"

# Command to display help
@bot.command()
async def pomoc(ctx):
    await ctx.send(help_message())

# Command to send server code
@bot.command()
async def kod(ctx):
    channel = discord.utils.get(ctx.guild.channels, name='🎮')
    if channel:
        await channel.send('Server code: ru2b00fv')
    else:
        await ctx.send('🎮 channel not found')

# Admin Commands
@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.name}')

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.name}')

@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member: discord.Member, *, reason=None):
    await ctx.send(f'Warning for {member.name}: {reason}')

@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(role)
    await ctx.send(f'Muted {member.name}')

# Emergency Roleplay Commands
@bot.command()
async def ambulance(ctx):
    await ctx.send('🚑 Ambulance on the way!')

@bot.command()
async def police(ctx):
    await ctx.send('🚔 Police assistance requested!')

@bot.command()
async def fire(ctx):
    await ctx.send('🔥 Fire department has been notified!')

# Cooperation Counter System
cooperation_counter = {}

@bot.command()
async def cooperate(ctx):
    user_id = ctx.author.id
    if user_id in cooperation_counter:
        cooperation_counter[user_id] += 1
    else:
        cooperation_counter[user_id] = 1
    await ctx.send(f'{ctx.author.name}, you have cooperated {cooperation_counter[user_id]} times.')

# Slash Commands
@bot.slash_command(name='info', description='Get bot info')
async def info(ctx):
    await ctx.send('This is a Discord bot with various commands!')

# Bot Token
bot.run('YOUR_BOT_TOKEN')
