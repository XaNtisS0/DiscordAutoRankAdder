import discord
import os
import requests

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

api_server = "http://0.0.0.0:5000"
webpage = ""

#invite link:
#https://discord.com/api/oauth2/authorize?client_id=799365421902987305&permissions=469896208&scope=bot

# Permisions:
#	Manage roles
#	Manage channels
#	View channels
#	Send messages
#	Mention everyone

# What admin should do before adding:
#	Add users and roles to them.
#	Add role with name 'members-admin'
#	Add channel with name 'members-bot-log'


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
    # Get server name
    guild = member.guild
    # Create or get members-admin role
    admin_role = discord.utils.get(guild.roles, name='members-admin')
    if not admin_role:
        await guild.create_role(name='members-admin')
    admin_role = discord.utils.get(guild.roles, name='members-admin')
    # Get api/servers/
    get_servers = requests.get(f'{api_server}/servers/').json()
    print(get_servers)
    # Get channel with name="bot-log" for logging
    logging_channel = discord.utils.get(guild.channels, name="bot-log")
    if not logging_channel:
        await guild.create_channel(name="bot-log")
    logging_channel = discord.utils.get(guild.channels, name="bot-log")
    server = {}
    # Check which server is the one we want and save info
    for i, d in enumerate(get_servers):
        if d['name'] == guild.name:
            server = get_servers[i]
    if server == {}:
        await logging_channel.send(f'{admin_role.mention} go to {webpage} to add server to bot database.')
    # Get api/{server_id}/users
    server_id = server['id']
    get_users = requests.get(f'{api_server}/{server_id}/users').json()
    # If loged in user is on the list of users then give him the roles from list
    db_user = {}
    for user in get_users:
        if user['username'] == member.name:
            db_user = user
    user_ranks = db_user['ranks']
    for rank in user_ranks:
        if rank not in guild.ranks:
            await guild.create_role(rank)
            await member.add_roles(discord.utils.get(guild.roles, name=rank))
        else:
            await member.add_roles(discord.utils.get(guild.roles, name=rank))
    # If not then log info about unwanted user with mention to members admin and the unwanted user.
    #	(f'{moderator_role.mention} Unknown user: {str(member.mention)}')
    #	send information to user that he need to contact administrator to change username in whitelist or manually add role

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
