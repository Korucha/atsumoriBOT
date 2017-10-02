import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!',description='ATSUMORI')

@bot.event
async def on_ready():
 print('起動完了')
 print(bot.user.name)

@bot.command()
async def atsumori():
 await bot.say("http://livedoor.blogimg.jp/jin115/imgs/e/d/edea4633.png")
 print('熱盛されました')

@bot.command()
async def kusamori():
 await bot.say("https://pbs.twimg.com/media/DI5KPyFVAAEgi-2.jpg")
 print('草盛されました')

bot.run('MzY0MjI1MTQxOTY3OTQ1NzI4.DLMqmw.r64q0rbu-0E1k-VOoEBF7xZVY3Q')
