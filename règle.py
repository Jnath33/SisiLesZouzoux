import discord
import json
import main
from discord.ext.commands import Context


async def create_rules(message: discord.Message, args: list):
    with open(file_name_règle, "r") as f:
        data = json.load(f)
        f.close()
    if not str(message.guild.id) in data.keys():
        await message.channel.send("Le salon de sondage n'as pas été définie **€config sondage set_channel** pour la définir")
        return
    member: discord.Member = message.author
    if not member.guild_permissions.administrator:
        await message.channel.send("Vous n'avez pas la permision neissesaire pour exécuter cette comande")
    embed: discord.Embed = discord.Embed(colour=discord.Colour.blue())
    guild: discord.Guild = message.guild
    channel: discord.TextChannel = guild.get_channel(data[str(guild.id)])
    embed.set_author(name=args[0][0].upper() + args[0][1::])
    embed.add_field(name="**Sondage**", value=args[1][0].upper() + args[1][1::])

    for i in range(min(len(args[2]),26)):
        embed.add_field(value="react to : "+emoji[chr(ord("a")+i)],name="**"+args[2][i][0].upper()+args[2][i][1::]+"**")
    msg: discord.Message = await channel.send(embed=embed)
    with open(file_name_règle, "r") as f:
        servers_sondage = json.load(f)
        f.close()
    if not str(msg.guild.id) in servers_sondage.keys():
        servers_sondage[str(msg.guild.id)] = {}
    servers_sondage[str(msg.guild.id)][str(msg.id)] = {}
    servers_sondage[str(msg.guild.id)][str(msg.id)]["vote"] = {}
    tmp = servers_sondage[str(msg.guild.id)][str(msg.id)]["vote"]
    for i in range(min(len(args[2]),26)):
        letter = chr(ord("a")+i)
        tmp[letter] = [0,min(len(args[2]), 26)+i+1]
        await msg.add_reaction(emoji[letter])
    servers_sondage[str(msg.guild.id)][str(msg.id)]["vote"]=tmp
    total_vote = 0
    for vote in tmp.keys():
        total_vote += tmp[vote][0]
    for vote in tmp.keys():
        if total_vote == 0:
            strt = "□□□□□□□□□□"
        else:
            strt = ""
            for i in range(10):
                if int((tmp[vote][0] * 10) / total_vote) > i:
                    strt += "■"
                else:
                    strt += "□"
        if total_vote == 0:
            str_pourcent = "0%"
        else:
            str_pourcent = str(int((tmp[vote][0] * 100) / total_vote)) + "%"
        embed.add_field(name="**Vote " + vote + "**",
                           value=str(tmp[vote][0]) + "·" + strt + " " + str_pourcent)
    await msg.edit(embed=embed)
    with open(file_name_règle, "w") as f:
        json.dump(servers_sondage, f)

async def on_message(message: discord.Message):
    if not message.author.id in sondage_creation.keys():
        return
    if msg_to_str(message)[0]=="st":
        str=""
        for s in message.content.split(" ")[1::]:
            str+=s
            str+=" "
        if len(str)>33:
            await message.channel.send("Le titre est trop long (32 char max)")
            return
        sondage_creation[message.author.id]["titre"] = str
        await message.delete()
        await message.channel.send("Le message à été set.)
    elif msg_to_str(message)[0]=="rd":
        str=""
        for s in message.content.split(" ")[1::]:
            str+=s
            str+=" "
        sondage_creation[message.author.id]["des"] = str
        await message.delete()
        await message.channel.send("La description du sondage a été set c'est maintenant : "+str)
    elif msg_to_str(message)[0]=="sp":
        if not "proposition" in sondage_creation[message.author.id]:
            sondage_creation[message.author.id]["proposition"] = []
        str=""
        for s in message.content.split(" ")[1::]:
            str+=s
            str+=" "
        sondage_creation[message.author.id]["proposition"].append(str)
        await message.delete()
        await message.channel.send("La proposition "+str+"à été ajouter au sondage")
    elif msg_to_str(message)[0]=="send":
        tmp = sondage_creation[message.author.id]
        if not("titre" in tmp.keys() and "des" in tmp.keys() and "proposition" in tmp.keys() and len(tmp["proposition"])>=2):
            await message.channel.send("vous n'avez pas donner toute les posibiliter")
            return
        await message.delete()
        await create_sondage(message, [tmp["titre"], tmp["des"],tmp["proposition"]])
        del sondage_creation[message.author.id]


