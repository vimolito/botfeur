import json
from pathlib import Path
import discord

##############

# PATH = Path("/home/aurnytoraink/Bot/Coiffeur")
PATH = Path("/Desktop\Coiffeur-master")
# Insérer l'adresse où se situe votre dossier

TOKEN = "ODg4MzQzODQwNTg5NzYyNTcw.YURUrA.J45xCCfcjet-F0Vor6oPDq9V5vk"


#############
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    # Évite que le bot intercepte ces propres messages
    if message.author == client.user:
        return

    # Prise en charge des majuscules et mininuscules
    # + les textes déformés comme "qUoiiiiiiiiiiiiiiiii ?"
    if message.content.lower().endswith('quoi'):
        await message.channel.send("feur")

    if message.content.lower().endswith('quoi ?'):
        await message.channel.send("feur")

    if message.content.lower().endswith('la'):
        await message.channel.send("brador")

    if message.content.lower().endswith('pq'):
        await message.channel.send("feur")

    if message.content.lower().endswith('pk'):
        await message.channel.send("feur")

    if message.content.lower().endswith('pas'):
        await message.channel.send("lourde")

    if message.content.lower().endswith('pa'):
        await message.channel.send("lourde")

    if message.content.lower().endswith('oui'):
        await message.channel.send("stiti")

    if message.content.lower().endswith('moi'):
        await message.channel.send("sonneuse")

    if message.content.lower().endswith('gorge'):
        await message.channel.send("profonde")

    if message.content.lower().endswith('ouai'):
        await message.channel.send("stern")

    if message.content.lower().endswith('toi'):
        await message.channel.send("lette")

    if message.content.lower().endswith('gout'):
        await message.channel.send("lag")

    if message.content.lower().endswith('rat'):
        await message.channel.send("ciste")

    if message.content.lower().endswith('ok'):
        await message.channel.send("sur glace")

    if message.content.lower().endswith('ça'):
        await message.channel.send("rdoche")

    if message.content.lower().endswith('trop'):
        await message.channel.send("pico")

    if message.content.lower().endswith('fort'):
        await message.channel.send("teresse")

    if message.content.lower().endswith('chaud'):
        await message.channel.send("diere comme @manon_prnr#1333")

    if message.content.lower().endswith('klaim'):
        await message.channel.send("bot")

    if message.content.lower().endswith('vim'):
        await message.channel.send("olito")

    if message.content.lower().endswith('nez'):
        await message.channel.send("gros")

    if message.content.lower().endswith('hein'):
        await message.channel.send("deux")

    if message.content.lower().endswith('bi'):
        await message.channel.send("sexuel")

    if message.content.lower().endswith('tout'):
        await message.channel.send("pie")

    if message.content.lower().endswith('un'):
        await message.channel.send("deux")

    if message.content.lower().endswith('deux'):
        await message.channel.send("trois")

    if message.content.lower().endswith('trois'):
        await message.channel.send("SOLEIL!!!!!!!!!!")

    if message.content.lower().endswith('1'):
        await message.channel.send("2")

    if message.content.lower().endswith('2'):
        await message.channel.send("3")

    if message.content.lower().endswith('3'):
        await message.channel.send("SOLEIL!!!!!!!!!!")

    if message.content.lower().endswith('oe'):
        await message.channel.send("jdene")

    if message.content.lower().endswith('rouge'):
        await message.channel.send("Gorge profonde")

    if message.content.lower().endswith('negro'):
        await message.channel.send("?????????")

    if message.content.lower().endswith('fin'):
        await message.channel.send("frérot")

    if message.content.lower().endswith('bou'):
        await message.channel.send("gnoule")










client.run(TOKEN)