import discord
import os

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
	channel = discord.utils.get(client.get_all_channels(), name='bot-log')
	print('We have logged in as {0.user}'.format(client))
	await channel.send('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
	#Get server name
	#Create or get members admin role
	#Get api/servers/
	#Check which server is the one we want and save info
	#If user wants logging -> Get channel with name="bot-log" for logging
	#Get api/{server_id}/users
	#If loged in user is on the list of users then give him the roles from list
	#If not then log info about unwanted user with mention to members admin and the unwanted user. 
	#	(f'{moderator_role.mention} Unknown user: {str(member.mention)}')

	'''organizator_role = discord.utils.get(
		member.guild.roles, id=695296019138609223)
	moderator_role = discord.utils.get(
		member.guild.roles, id=695296022712418384)

	channel = client.get_channel(799960026575536128)

	print(f'{str(member.name)} logged in with display_name: {str(member.display_name)}')
	await channel.send(f'{str(member.name)} logged in with display_name: {str(member.display_name)}')

	lol5v5role = discord.utils.get(
		member.guild.roles, name='LoL 5v5 - Uczestnicy')
	lol1v1role = discord.utils.get(
		member.guild.roles, name='LoL 1v1 - Uczestnicy')
	csgorole = discord.utils.get(
		member.guild.roles, name='CS:GO 1v1 - Uczestnicy')

	username = str(member.name)

	for i, d in enumerate(people):
		if d['username'] == username:
			ranks.append(i)
	for value in ranks:
		if (people[value]['rank'] == 'csgo'):
			await member.add_roles(csgorole)
			print("Added role csgo")
			await channel.send("Added role csgo")
		elif (people[value]['rank'] == 'lol5v5'):
			await member.add_roles(lol5v5role)
			print("Added role lol5v5")
			await channel.send("Added role lol5v5")
		elif (people[value]['rank'] == 'lol1v1'):
			await member.add_roles(lol1v1role)
			print("Added role lol1v1")
			await channel.send("Added role lol1v1")

	if (people[value]['changeUser'] != member.display_name):
		await member.edit(nick=people[value]['changeUser'])
		print("Changed username to: " + member.display_name)
		await channel.send("Changed username to: " + member.display_name)
	if not ranks: 
		print("Unknown user: " + str(member.name))
		await channel.send(f'{organizator_role.mention} {moderator_role.mention} Unknown user: {str(member.mention)}')
	print("")'''

client.run(os.getenv('TOKEN'))
