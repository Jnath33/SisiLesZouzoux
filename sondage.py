import discord
import json
import main
from discord.ext.commands import Context


# sondage.json
# {
#   server_id: channel_id
# }
#
# server_sondage.json
# {
#   server_id: {
#     message_id: {
#       "vote':{
#       'a': [0,2],
#       'b': [0,3]}
#       'end': 10000000
#     }
#   }
# }
emoji={ "a":"🇦", "b":"🇧", "c":"🇨", "d":"🇩", "e":"🇪",  #end
        "f":"🇦", "g":"🇦", "h":"🇦", "i":"🇦", "j":"🇦",  #not end
        "k":"🇦", "l":"🇦", "m":"🇦", "n":"🇦", "o":"🇦",  #not end
        "p":"🇦", "q":"🇦", "r":"🇦", "s":"🇦", "t":"🇦",  #not end
        "u":"🇦", "v":"🇦", "w":"🇦", "x":"🇦", "y":"🇦",
        "z":"🇦",
        "🇦":"a", "🇧":"b", "🇨": "c", "🇩": "d", "🇪": "e"}
file_name_sondage = "sondage.json"
file_name_server_sondage = "server_sondage.json"
sondage_creation = {}


def msg_to_str(message):
    test = message.content.split(" ")
    return test


async def set_channel_sondage(ctx: Context):
    with open(file_name_sondage, "r") as f:
        data = json.load(f)
        f.close()
    data[ctx.guild.id] = ctx.channel.id
    with open(file_name_sondage, "w") as f:
        json.dump(data, f)
        f.close()
    await ctx.channel.send("Le salon de sondage à été mise sur le salon : "+ctx.channel.name)

def test():
    print("test")

async def realsondage(ctx: Context):
    member = ctx.author
    embed = discord.Embed(colour=discord.Colour.dark_gold())
    embed.set_author(name=member.name)
    embed.add_field(name="st <message>", value="utiliser st pour donner un titre a votre sondage (32 max)")
    embed.add_field(name="sd <message>", value="utiliser sd pour sélectioner la description qui va avec votre sondage")
    embed.add_field(name="sp <message>", value="utiliser sp pour ajouter une proposition au sondage")
    embed.add_field(name="send", value="utiliser send pour terminer le sondage")
    if ctx.author.id in sondage_creation.keys():
        await ctx.send("Vous avez deja commencer a crée un sondage. Le sondage est donc réinitialiser")
    sondage_creation[ctx.author.id]={}
    await ctx.send(embed=embed)


async def create_sondage(message: discord.Message, args: list):
    with open(file_name_sondage, "r") as f:
        data = json.load(f)
        f.close()
    if not str(message.guild.id) in data.keys():
        await message.channel.send("Le salon de sondage n'as pas été défini **€config sondage set_channel** pour le définir")
        return
    member: discord.Member = message.author
    if not member.guild_permissions.administrator:
        await message.channel.send("Vous n'avez pas la permision nécesaire pour exécuter cette commande")
    embed: discord.Embed = discord.Embed(colour=discord.Colour.dark_magenta())
    guild: discord.Guild = message.guild
    channel: discord.TextChannel = guild.get_channel(data[str(guild.id)])
    embed.set_author(name=args[0][0].upper() + args[0][1::])
    embed.add_field(name="**Sondage**", value=args[1][0].upper() + args[1][1::])

    for i in range(min(len(args[2]),26)):
        embed.add_field(value="react to : "+emoji[chr(ord("a")+i)],name="**"+args[2][i][0].upper()+args[2][i][1::]+"**")
    msg: discord.Message = await channel.send(embed=embed)
    with open(file_name_server_sondage, "r") as f:
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
    with open(file_name_server_sondage, "w") as f:
        json.dump(servers_sondage, f)


async def on_sondage_vote(payload: discord.RawReactionActionEvent, addQuantitie: int):
    if payload.user_id==806454862379614228:
        return
    channel: discord.TextChannel = main.bot.get_channel(payload.channel_id)
    with open(file_name_sondage, "r") as f:
        data = json.load(f)
        f.close()
    if not str(payload.guild_id) in data.keys():
        return
    if not payload.channel_id == data[str(payload.guild_id)]:
        return
    message: discord.Message = await channel.fetch_message(payload.message_id)

    for embed in message.embeds:
        with open(file_name_server_sondage, "r") as f:
            severs_sondage = json.load(f)
            print(len(severs_sondage))
            f.close()
        for s in severs_sondage.keys():
            print(s)
        if not str(payload.guild_id) in severs_sondage.keys():
            return
        for s in severs_sondage[str(payload.guild_id)].keys():
            print(s)
        if not str(payload.message_id) in severs_sondage[str(payload.guild_id)].keys():
            return
        tmpEmoji: discord.Emoji = payload.emoji
        tmp_vote = severs_sondage[str(payload.guild_id)][str(payload.message_id)]["vote"]
        tmp_vote[emoji[tmpEmoji.name]][0]+=addQuantitie
        with open(file_name_server_sondage, "w") as f:
            json.dump(severs_sondage, f)
        total_vote = 0
        for vote in tmp_vote.keys():
            total_vote+=tmp_vote[vote][0]
        for vote in tmp_vote.keys():
            if total_vote == 0:
                strt="□□□□□□□□□□"
            else:
                strt=""
                for i in range(10):
                    if int((tmp_vote[vote][0]*10)/total_vote)>i:
                        strt+="■"
                    else:
                        strt+="□"
            if total_vote == 0:
                str_pourcent = "0%"
            else:
                str_pourcent = str(int((tmp_vote[vote][0]*100)/total_vote))+"%"
            embed.set_field_at(index=tmp_vote[vote][1],name="**Vote "+vote+"**", value=str(tmp_vote[vote][0])+"·"+strt+" "+str_pourcent)
        await message.edit(embed=embed)



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
        await message.channel.send("Le titre du sondage a été set c'est maintenant : "+str)
    elif msg_to_str(message)[0]=="sd":
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


