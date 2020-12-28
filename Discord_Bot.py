#Imports
import discord
import asyncio
import random
import segredo

client = discord.Client()

TOKEN = segredo.token()

#Quando o BOT iniciar ira aparecer seus respectivos dados
@client.event
async def on_ready():
    print("BOT ONLINE - OLÁ MUNDO!")
    print(client.user.name)
    print(client.user.id)
    print("----------------------")

#configurando respostas a comandos específicos
@client.event
async def on_message(message):
    if message.content.lower().startswith("!bot"): #comando para o bot
        channel = message.channel
        await channel.send("Estou vivo!") #resposta dada pelo bot ao comando dado a cima

    if message.content.lower().startswith("!magica"): #comando
        channel = message.channel
        await channel.send("não é mágica, é programação!") #resposta

    if message.content.lower().startswith('!moeda'): #comando "jogo da moeda"
            escolha = random.randint(1, 2)
            if escolha == 1:
                await message.add_reaction('😀') #50% de chance de dar cara
            if escolha == 2:
                await message.add_reaction('👑') #50% de chance de dar coroa

client.run(TOKEN) #Aqui é onde o BOT é colocado online através do token de ativação (definido na outra aplicação)






