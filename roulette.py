import discord
import discord.ext.commands
import asyncio
import time
import random

roulette_role = {}  # tu crée un dictionaire roulette
timeout_role = {}
timeout_add_role = {}
roulette = {}


async def timeout(message: discord.Message):
    user_id = message.author.id
    timeout_role[user_id] = int(message.content.split(" ")[1])
    await message.channel.send("Le temps à était mis à : " + str(int(message.content.split(" ")[1])))


async def timeout_add(message: discord.Message):
    user_id = message.author.id
    timeout_add_role[user_id] = int(message.content.split(" ")[1])
    await message.channel.send("Le temps à était mis à : " + str(int(message.content.split(" ")[1])))


async def add_element(message):
    v_str = " "
    for i in message.content.split(" ")[1::]:
        v_str += i + " ";
    # pour ajouté un élément
    user_id = message.author.id  # tu récupère l'user id
    if not user_id in roulette_role.keys():
        roulette_role[user_id] = []
    roulette_role[user_id].append(v_str)
    await message.channel.send("Une proposition vient d'être ajouté : " + v_str)


async def send_message(message):
    user_id = message.author.id
    if not user_id in roulette_role:
        return
    ma_liste = roulette_role[user_id]
    del roulette_role[user_id]
    if user_id in timeout_role:
        ma_liste2 = timeout_role[user_id]
        del timeout_role[user_id]
    else:
        ma_liste2 = 30
    if user_id in timeout_add_role:
        ma_liste3 = timeout_add_role[user_id]
        del timeout_add_role[user_id]
    else:
        ma_liste3 = 1
    await message.channel.send(
        "Début de la roulette les récompence sont : " + str(ma_liste) + ", vous avez " + str(ma_liste2))
    roulette[message.guild.id] = {}
    roulette[message.guild.id][message.channel.id] = {}
    roulette[message.guild.id][message.channel.id]["static"] = [ma_liste, ma_liste2+time.time(), ma_liste3]
    roulette[message.guild.id][message.channel.id]["participant"] = []


async def create_roulette(ctx):
    embed = discord.Embed(title="Roulette", color=0x06e02a)
    embed.add_field(name="rp [text]", value="pour rajouté une proposition", inline=False)
    embed.add_field(name="rt [time]", value="pour mettre la durée (30 s) par défaut", inline=False)
    embed.add_field(name="ra [time]", value="pour donné le temps ajouté à chaque moi écrit (1 s par défaut) ",
                    inline=False)
    embed.add_field(name="rend", value="pour terminer", inline=True)
    await ctx.send(embed=embed)


async def on_message(message):
    text = message.content
    if text.startswith("r"):
        if text.startswith("rp"):
            await add_element(message)
        elif text.startswith("rt"):
            await timeout(message)
        elif text.startswith("ra"):
            await timeout_add(message)
        elif text.startswith("rend"):
            await send_message(message)
    if text.startswith("moi") and text.endswith("moi"):
        if message.guild.id in roulette.keys():
            if message.channel.id in roulette[message.guild.id].keys():
                await participation(message)


async def participation(message):
    mon_truc = roulette[message.guild.id][message.channel.id]
    author_id = message.author.id
    if not author_id in mon_truc["participant"]:
        mon_truc["participant"].append(author_id)
        mon_truc["static"][1] += mon_truc["static"][2]
        await message.channel.send("Message")


async def roulette_verif(bot):
    for i in roulette.keys():
        for i2 in roulette[i].keys():
            mon_truc = roulette[i][i2]
        if mon_truc["static"][1]<=time.time():
            for i2 in roulette[i].keys():
                guild = await bot.fetch_guild(i)
                ctx = guild.get_channel(str(i2))
            await ctx.send("Le tirage va commencer dans 3...")
            await asyncio.sleep(1)
            await ctx.send("2")
            await asyncio.sleep(1)
            await ctx.send("1")
            await asyncio.sleep(1)
            loser = random.choice(mon_truc["participant"])
            price = random.choice(mon_truc["static"][0])
            await ctx.send(f"La personne qui a gagnée un {price} est...")
            await asyncio.sleep(1)
            await ctx.send("**" + loser.name + "**" + " !")



