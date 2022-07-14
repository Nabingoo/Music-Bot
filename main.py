import dbdmusic
import os, asyncio

import discord


bot_ = dbdmusic.Bot(prefix = "!", lavalinkpass = "yourpass", lavalinkport = 6969)

bot = bot_.bot

@bot.event
async def on_ready():
		await asyncio.sleep(2)
		bot.load_extension("extension")
		print("Extension Loaded.")
		await bot.change_presence(status=discord.Status.dnd,activity=discord.Game(name="!cmd"))
@bot.command()
async def reload(ctx):
	bot.reload_extension("extension")
	await ctx.send("Reloaded Extension.")

bot_.connect(os.environ.get("TOKEN"))
