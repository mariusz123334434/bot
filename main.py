import discord
from discord.ext import commands

# Define your bot and command prefix
bot = commands.Bot(command_prefix='!')

# Command to display help
@bot.command()
async def help(ctx):
    help_message = "This is the help command!\n" \
                   "!emergency - Emergency roleplay commands.\n" \
                   "!admin - Admin commands.\n" \
                   "!code - Server roleplay code display.\n" \
                   "!cooperation - Displays cooperation counter."
    await ctx.send(help_message)

# Admin commands
@bot.command()
@commands.has_permissions(administrator=True)
async def admin(ctx, *, command):
    await ctx.send(f'Executing admin command: {command}')

# Emergency roleplay commands
@bot.command()
async def emergency(ctx):
    await ctx.send("Emergency roleplay commands here!")

# Server code command
@bot.command()
async def code(ctx):
    server_code = 'ABC123'
    await ctx.send(f'Server Roleplay Code: {server_code}')

# Cooperation counter
cooperation_counter = 0
@bot.command()
async def cooperation(ctx):
    global cooperation_counter
    cooperation_counter += 1
    await ctx.send(f'Cooperation count is now: {cooperation_counter}')

# Run the bot (replace 'YOUR_TOKEN' with your bot's actual token)
bot.run('YOUR_TOKEN')