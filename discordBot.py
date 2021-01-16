import discord
import os
from keep_alive import keep_alive

people = [
  {
    "username": "1zY",
    "rank": "csgo",
    "changeUser": "1zY"
  },
  {
    "username": "Daxir",
    "rank": "lol5v5"
  },
  {
    "username": "karowka",
    "rank": "lol5v5"
  },

  {
    "username": "bron99",
    "rank": "csgo",
    "changeUser": "bron99"
  },
  {
    "username": "brzezin",
    "rank": "csgo",
    "changeUser": "Brzezin"
  },
  {
    "username": "Całka z 2x ",
    "rank": "csgo",
    "changeUser": "Całka z 2x"
  },
  {
    "username": "Krzysztof Sobiecki",
    "rank": "csgo",
    "changeUser": "elsav"
  },
  {
    "username": "emeref",
    "rank": "csgo",
    "changeUser": "emeref"
  },
  {
    "username": "Łajtu",
    "rank": "csgo",
    "changeUser": "Łajtu"
  },
  {
    "username": "Plusek ",
    "rank": "csgo",
    "changeUser": "Plusek"
  },
  {
    "username": "Politetrafluoroetylen",
    "rank": "csgo",
    "changeUser": "Politetrafluoroetylen"
  },
  {
    "username": "poopzone",
    "rank": "csgo",
    "changeUser": "poop"
  },
  {
    "username": "ReeiZer84",
    "rank": "csgo",
    "changeUser": "Sernik1337"
  },
  {
    "username": "teq",
    "rank": "csgo",
    "changeUser": "teq"
  },
  {
    "username": "aleksander.brylski",
    "rank": "lol5v5",
    "changeUser": "Aleksander Brylski"
  },

  {
    "username": "Anewil",
    "rank": "lol5v5",
    "changeUser": "Anewil"
  },
  {
    "username": "Anja",
    "rank": "lol5v5",
    "changeUser": "Anja"
  },
  {
    "username": "Kidawa",
    "rank": "lol5v5",
    "changeUser": "Kidawa"
  },
  {
    "username": "macieK",
    "rank": "lol5v5",
    "changeUser": "macieK"
  },
  {
    "username": "MoonGuy",
    "rank": "lol5v5",
    "changeUser": "MoonGuy"
  },
  {
    "username": "Testowe",
    "rank": "lol5v5",
    "changeUser": "PawelMM"
  },
  {
    "username": "Pyssio",
    "rank": "lol5v5",
    "changeUser": "Pyssio"
  },
  {
    "username": "Maciej",
    "rank": "lol5v5",
    "changeUser": "Qutlet"
  },
  {
    "username": "Sahya",
    "rank": "lol5v5",
    "changeUser": "Sahya"
  },
  {
    "username": "VarmM",
    "rank": "lol5v5",
    "changeUser": "VarmΜ"
  },
  {
    "username": "Vejlen",
    "rank": "lol5v5",
    "changeUser": "Vejlen"
  },

  {
    "username": "1ntense",
    "rank": "lol1v1",
    "changeUser": "1ntense"
  },
  {
    "username": "Archér Yuro-",
    "rank": "lol1v1",
    "changeUser": "Archer"
  },
  {
    "username": "Artosz",
    "rank": "lol1v1",
    "changeUser": "Artosz"
  },
  {
    "username": "BrychuTV",
    "rank": "lol1v1",
    "changeUser": "BrychuTV"
  },
  {
    "username": "Burb0N",
    "rank": "lol1v1",
    "changeUser": "Burbon"
  },
  {
    "username": "Cody",
    "rank": "lol1v1",
    "changeUser": "Cody"
  },
  {
    "username": "Fidzii_",
    "rank": "lol1v1",
    "changeUser": "Fidzii"
  },
  {
    "username": "Mako",
    "rank": "lol1v1",
    "changeUser": "Jeff Buckley"
  },
  {
    "username": "Jokalari",
    "rank": "lol1v1",
    "changeUser": "Jokalari"
  },
  {
    "username": "Kotaro",
    "rank": "lol1v1",
    "changeUser": "Kotaro"
  },
  {
    "username": "Kublot8",
    "rank": "lol1v1",
    "changeUser": "Kublot"
  },
  {
    "username": "Kowal",
    "rank": "lol1v1",
    "changeUser": "Mequ"
  },
  {
    "username": "Monika123",
    "rank": "lol1v1",
    "changeUser": "Neas"
  },
  {
    "username": "Myhauuuu",
    "rank": "lol1v1",
    "changeUser": "Piponsz"
  },
  {
    "username": "Potuś",
    "rank": "lol1v1",
    "changeUser": "Potuś"
  },
  {
    "username": "DeathTrailer",
    "rank": "lol1v1",
    "changeUser": "SkyDogPL"
  },
  {
    "username": "taboretoo",
    "rank": "lol1v1",
    "changeUser": "taboretoo"
  },
  {
    "username": "Vaxoru",
    "rank": "lol1v1",
    "changeUser": "Vados"
  },
  {
    "username": "Vulpus",
    "rank": "lol1v1",
    "changeUser": "Vulpus"
  },
  {
    "username": "wilkieł",
    "rank": "lol1v1",
    "changeUser": "wilkieł"
  },
  {
    "username": "Rinisis",
    "rank": "lol1v1",
    "changeUser": "yetiyku"
  },
  {
    "username": "ZielaQ",
    "rank": "lol1v1",
    "changeUser": "ZielaQ"
  },
  {
    "username": "incRe.",
    "rank": "lol1v1",
    "changeUser": "incRe."
  },
  {
    "username": "Vertix",
    "rank": "lol1v1",
    "changeUser": "Vertix"
  },
  {
    "username": "Rega",
    "rank": "lol1v1",
    "changeUser": "Rega9"
  },
  {
    "username": "Wasil17",
    "rank": "lol1v1",
    "changeUser": "Wasil"
  },

  {
    "username": "Wasil17",
    "rank": "lol5v5",
    "changeUser": "Wasil"
  },
  {
    "username": "Rega",
    "rank": "lol5v5",
    "changeUser": "Rega9"
  },
  {
    "username": "Vertix",
    "rank": "csgo",
    "changeUser": "Vertix"
  },
  {
    "username": "incRe.",
    "rank": "csgo",
    "changeUser": "incRe."
  }]

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
  channel = client.get_channel(799960026575536128)
  print('We have logged in as {0.user}'.format(client))
  await channel.send('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
  organizator_role = discord.utils.get(member.guild.roles, id=695296019138609223)
  moderator_role = discord.utils.get(member.guild.roles, id=695296022712418384)
  channel = client.get_channel(799960026575536128)
  print(f'{str(member.name)} logged in with display_name: {str(member.display_name)}')
  await channel.send(f'{str(member.name)} logged in with display_name: {str(member.display_name)}')
  lol5v5role = discord.utils.get(member.guild.roles, name='LoL 5v5 - Uczestnicy')
  lol1v1role = discord.utils.get(member.guild.roles, name='LoL 1v1 - Uczestnicy')
  csgorole = discord.utils.get(member.guild.roles, name='CS:GO 1v1 - Uczestnicy')

  username = str(member.name)

  ranks = []
  
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
    await channel.send(f'{organizator_role.mention} {moderator_role.mention} Unknown user: {str(member.name)}')
  print("")
    
keep_alive()
client.run(os.getenv('TOKEN'))