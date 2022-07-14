from discord.ext import commands
import discord
import lavalink
import time
import re
url_rx = re.compile(r'https?://(?:www\.)?.+')
class Exten(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
		self.lavalink = self.bot.get_cog("Music").bot.lavalink

	@commands.command()
	async def volume(self, ctx, vol = None):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")

		if not vol:
			await ctx.send(f"Volume: {player.volume}")
		elif 0 <= int(vol) <= 100:
			await player.set_volume(int(vol))
			await ctx.send(f"Set volume to {vol}")

	@commands.command(aliases = ['ps'])
	async def pause(self, ctx):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")

		await player.set_pause(True)
		await ctx.send("Paused")

	@commands.command(aliases = ['rs'])
	async def resume(self, ctx):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")

		await player.set_pause(False)
		await ctx.send("Resumed")

	@commands.command(aliases = ['np'])
	async def nowplaying(self, ctx):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")

		current = player.current

		iden = current.identifier

		embed = discord.Embed(

			title = "Now Playing",
			url = current.uri,
			description = f"[{current.author}]({current.uri})"
		)

		embed.set_author(name = current.title,icon_url=f"https://img.youtube.com/vi/{iden}/0.jpg")
		embed.set_thumbnail(url = f"https://img.youtube.com/vi/{iden}/0.jpg")
		await ctx.send(embed = embed)

	@commands.command(aliases = ['q'])
	async def queue(self, ctx):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")

		embed = discord.Embed(

			title = "Queue",
			description = f"Current:[{player.current.title}]({player.current.uri})"

		)

		i = 1

		for song in player.queue:
			embed.description += f"\n{i}.) {song.title}"
			i +=1
			
		await ctx.send (embed = embed)

	@commands.command(aliases = ['s'])
	async def skip(self, ctx):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")
		await player.skip()



	@commands.command(aliases = ['r'])
	async def remove(self, ctx, index: int):
		player = self.lavalink.player_manager.get(ctx.guild.id)
		
		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")
		

		print(int)
		del player.queue[index-1]  # Account for 0-index.

		await ctx.send(
            f'Removed #**{index}** from the queue.'
        )

	@commands.command(aliases = ['c'])
	async def clear(self, ctx):
		player = self.lavalink.player_manager.get(ctx.guild.id)
		
		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")
		

		
		player.queue.clear()

		await ctx.send(
            f'Cleared Queue'
        )


	@commands.command(aliases = ['cmd'])
	async def info(self, ctx):


		
		embed = discord.Embed(

				title = "Command List",
				description = "Command prefix is ! \n play (song name) [p] \n queue [q] \n skip [s] \n nowplaying  [np]\n pause [ps] \n resume [rs] \n remove [r] \n clear [c] \n seek [sk] \n disconnect \n Bass boost [bb] \n Revert Boost [ab]\n Super Boost[sb] \n PlaySkip [pk] \n  Boost Insane [ib] \n die [die] \n Getworse [gw] "

			)

		

	
			
		await ctx.send (embed = embed)
	@commands.command(aliases = ['sk'])
	async def seek(self, ctx, position: int):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")
		
		await player.seek(position * 1000)
	
	@commands.command(aliases = ['bb'])
	async def bassboost(self, ctx):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")
		
		await player.set_gain(1,0.1)
		await player.set_gain(2,0.1)
		await player.set_gain(3,0.1)
		await player.set_gain(4,0.05)
		await player.set_gain(5,0.05)
		await player.set_gain(6,0.03)
		
	@commands.command(aliases = ['sb'])
	async def superboost(self, ctx):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")
		
		await player.set_gain(1,0.2)
		await player.set_gain(2,0.2)
		await player.set_gain(3,0.15)
		await player.set_gain(4,0.1)
		await player.set_gain(5,0.1)
		await player.set_gain(6,0.05)
	
	@commands.command(aliases = ['ib'])
	async def insaneboost(self, ctx):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")
		
		await player.set_gain(1,0.5)
		await player.set_gain(2,0.5)
		await player.set_gain(3,0.3)
		await player.set_gain(4,0.2)
		await player.set_gain(5,0.15)
		await player.set_gain(6,0.1)
	@commands.command(aliases = ['ed'])
	async def eardeath(self, ctx):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")
		
		await player.set_gain(1,0.8)
		await player.set_gain(2,0.8)
		await player.set_gain(3,0.5)
		await player.set_gain(4,0.3)
		await player.set_gain(5,0.2)
		await player.set_gain(6,0.2)
	@commands.command(aliases = ['die'])
	async def death(self, ctx):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")
		
		await player.set_gain(1,1)
		await player.set_gain(2,1)
		await player.set_gain(3,1)
		await player.set_gain(4,0.9)
		await player.set_gain(5,0.9)
		await player.set_gain(6,0.9)

	@commands.command(aliases = ['gw'])
	async def getworse(self, ctx):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")
		
		await player.set_gain(1,0)
		await player.set_gain(2,0)
		await player.set_gain(3,0)
		await player.set_gain(4,0)
		await player.set_gain(5,0)
		await player.set_gain(6,0)

		time.sleep(3)

		await player.set_gain(1,0.1)
		await player.set_gain(2,0.1)
		await player.set_gain(3,0.1)
		await player.set_gain(4,0.1)
		await player.set_gain(5,0.1)
		await player.set_gain(6,0.1)

		time.sleep(3)
		await player.set_gain(1,0.2)
		await player.set_gain(2,0.2)
		await player.set_gain(3,0.2)
		await player.set_gain(4,0.2)
		await player.set_gain(5,0.2)
		await player.set_gain(6,0.2)

		time.sleep(3)
		await player.set_gain(1,0.3)
		await player.set_gain(2,0.3)
		await player.set_gain(3,0.3)
		await player.set_gain(4,0.3)
		await player.set_gain(5,0.3)
		await player.set_gain(6,0.3)

		time.sleep(3)
		await player.set_gain(1,0.4)
		await player.set_gain(2,0.4)
		await player.set_gain(3,0.4)
		await player.set_gain(4,0.4)
		await player.set_gain(5,0.4)
		await player.set_gain(6,0.4)

		time.sleep(3)
		await player.set_gain(1,0.5)
		await player.set_gain(2,0.5)
		await player.set_gain(3,0.5)
		await player.set_gain(4,0.5)
		await player.set_gain(5,0.5)
		await player.set_gain(6,0.5)

		time.sleep(3)
		await player.set_gain(1,0.6)
		await player.set_gain(2,0.6)
		await player.set_gain(3,0.6)
		await player.set_gain(4,0.6)
		await player.set_gain(5,0.6)
		await player.set_gain(6,0.6)

		time.sleep(3)
		await player.set_gain(1,0.7)
		await player.set_gain(2,0.7)
		await player.set_gain(3,0.7)
		await player.set_gain(4,0.7)
		await player.set_gain(5,0.7)
		await player.set_gain(6,0.7)

		time.sleep(3)
		await player.set_gain(1,0.8)
		await player.set_gain(2,0.8)
		await player.set_gain(3,0.8)
		await player.set_gain(4,0.8)
		await player.set_gain(5,0.8)
		await player.set_gain(6,0.8)

		time.sleep(3)
		await player.set_gain(1,0.9)
		await player.set_gain(2,0.9)
		await player.set_gain(3,0.9)
		await player.set_gain(4,0.9)
		await player.set_gain(5,0.9)
		await player.set_gain(6,0.9)

		time.sleep(3)
		await player.set_gain(1,1)
		await player.set_gain(2,1)
		await player.set_gain(3,1)
		await player.set_gain(4,1)
		await player.set_gain(5,1)
		await player.set_gain(6,1)

		

	@commands.command(aliases = ['ab'])
	async def antiboost(self, ctx,):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")
		
		await player.reset_equalizer()

	@commands.command(aliases=["pk"])
	async def playskip(self, ctx, *, query:str):
		player = self.bot.lavalink.player_manager.get(ctx.guild.id)
		if not player:
			return await ctx.send("**Nothing is playing right now.**")
			query = query.strip('<>')        
		if not url_rx.match(query):
			query = f'ytsearch:{query}'        
			results = await player.node.get_tracks(query)        
			if not results or not results['tracks']:
			     return await ctx.send('Nothing found!')
			embed = discord.Embed(color=discord.Colour.random())        
			track = results['tracks'][0]      
			player.add(requester=ctx.author.id, track=track, index=0)     
			await player.skip()
			

		
		

	
	#@commands.command(aliases = ['ps'])
	#async def playskip(self, ctx, index: int):
	#	player = self.lavalink.player_manager.get(ctx.guild.id)
		
	#	if not player:
		#	return await ctx.send('Not connected!')
		
	#	elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
		#	return await ctx.send("You are not in my voice channel.")


	 	
def setup(bot):
	bot.add_cog(Exten(bot))
