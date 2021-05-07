import json
import os
import random
from discord.ext.commands import Context
import discord
from discord.ext import commands
from discord.ext import tasks
import sondage as sond
from importlib import reload
import asyncio
import PIL
import secret
import roulette as rolltime
from math import sqrt

intents = discord.Intents.default()
intents.members = True
reload(sond)

bot = commands.Bot(command_prefix="€", intents=intents)
bot.remove_command('help')


sondages = {}
role = {}

json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
'["foo", {"bar": ["baz", null, 1.0, 2]}]'
print(json.dumps("\"foo\bar"))
"\"foo\bar"
print(json.dumps('\u1234'))
"\u1234"
print(json.dumps('\\'))
"\\"
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
var = {"a": 0, "b": 0, "c": 0}
from io import StringIO

io = StringIO()
json.dump(['streaming API'], io)
io.getvalue()
'["streaming API"]'



def message_to_str(message, one_message):
    if one_message:
        return message.content.split(" ")[1]+" "
    else:
        test = message.content.split(" ")
    test2 = ""
    for i in test:
        test2 += i+" "
    return test2


Dé=["1", "2", "3","4", "5", "6"]
Dé8=["1", "2", "3","4", "5", "6", "7", "8"]
Dé16=["1", "2", "3","4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
Dé20=["1", "2", "3","4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
FunSentence = ["Il fallait savoir que Chuck Norris a compté deux fois jusqu'à l'infini...",
               "Il ne fallait pas diviser par 0",
               "Il ne fallait pas dévelloper",
               "On te l'as déjà dit pourtant... En cartographie, pas de compromit avec la rigueur",
               "Romans number... Bull Sheet!",
               "1 + 1 n'est pas égal à deux... C'est égal à 3",
               "C'est la rue",
               "***Dura Lex Sed Lex***"]
status = ["A friend in need is a friend indeed",
          "Speech is silver, silence is golden",
          "If you need something... DON'T CALL ME",
          "If you want some help, use €help",
          "Yu Gi Oh Duel Links",
          "Je paresse woula"]

Fortune = ["Hell Yeah",
           "Euh.... Non",
           "Pourquoi tout le monde me pose des questions alors que je n'en sait rien?",
           "Probablement",
           "JAMAIS",
           "Tu ma pris pour quoi là? Pour une voyante?",
           "Bien sur que oui... A moins que...",
           "~~Oh no!~~... Fuck it, YOLO!",
           "Pour qui tu me prends? Je ne suis pas Claude Alexis moi!!"]

Fanjaux= ["Bon...Plouf Plouf...",
          "Comment vous vous appelez? Marion... J'adore les Marion!!",
          "Bon... Je vais faire un truc que je n'aime pas vraiment mais je le fais pour gagner du temps... Je vous laisse le cours clé en main",
          "Alors... En fait..."]

Raymond = ["Grrrrrrrrr",
           "Des vecteurs ne sont jamais parallèles. Ils sont collinéaires. Si tu dis que des vecteurs sont parrallèles... Tu passes par la fenêtre!!",
           "Développer... C'est mal",
           "Diviser par 0... ça mérite la peine capital!!",
           "le contraire de la parabole est une fonction chanceuse... C'est l'Hyperbole!",
           "Personne n'as jamais compter jusqu'à l'infini... A part Chuck Norris."]

Quiestu = ["Je suis quelqu'un.",
            "Je suis ton père.",
            "Je suis qui je suis tout en étant la personne que tu veux que je sois.",
            "Non, toi qui es tu?",
           "Je suis personne."
           "Tu sais lire non? Donc regarde mon blaze dans les membres en ligne.",
           "Je suis Sisi Les Zouzoux."]
Angry = ["https://media1.tenor.com/images/3fe790527a5b7bfa085b6ce3e3ccde9d/tenor.gif?itemid=16261546",
         "https://media1.tenor.com/images/2f198dc24f638fc9f16776c8ebd183fd/tenor.gif?itemid=14682313",
         "https://media1.tenor.com/images/68bdb7f778cf76bfaa256ebf53164558/tenor.gif?itemid=5591675",
         "https://media1.tenor.com/images/54d526fd183bb842780b9df05ebf6af6/tenor.gif?itemid=5628546",
         "https://media.discordapp.net/attachments/736258706383175720/736258982913507488/angry.gif",
         "https://media1.tenor.com/images/9c82436239131c92f375995b427f993e/tenor.gif?itemid=13045775",
         "https://media1.tenor.com/images/e56e1ae197ea11668756e6e82407e5c5/tenor.gif?itemid=12679335"]

Blush = ["https://media1.tenor.com/images/6537bbbf7cc5d6b33295abedb9191977/tenor.gif?itemid=14859821",
         "https://media1.tenor.com/images/ff25240fb2e1002a1a2358295fe72ef1/tenor.gif?itemid=14225039",
         "https://media1.tenor.com/images/9fa45bb3af562268984e7d7321f7ca9c/tenor.gif?itemid=17478014",
         "https://media1.tenor.com/images/cbfd2a06c6d350e19a0c173dec8dccde/tenor.gif?itemid=15727535",
         "https://media1.tenor.com/images/60bb9040f3d956d2f76f54b469b4f481/tenor.gif?itemid=16656636",
         "https://media.discordapp.net/attachments/736260129418248242/736260305075830814/blush.gif"]

Cry =["https://media1.tenor.com/images/49e4248f18b359dd46f7b60b01d1a4a0/tenor.gif?itemid=5652241",
      "https://media1.tenor.com/images/e69ebde3631408c200777ebe10f84367/tenor.gif?itemid=5081296",
      "https://media1.tenor.com/images/98466bf4ae57b70548f19863ca7ea2b4/tenor.gif?itemid=14682297",
      "https://media1.tenor.com/images/2e4d11202bf35e6d14d5a58a0a322402/tenor.gif?itemid=17484634",
      "https://media1.tenor.com/images/ce52606293142a2bd11cda1d3f0dc12c/tenor.gif?itemid=5184314",
      "https://media1.tenor.com/images/7ef999b077acd6ebef92afc34690097e/tenor.gif?itemid=10893043",
      "https://media1.tenor.com/images/4b5e9867209d7b1712607958e01a80f1/tenor.gif?itemid=5298257"]

file_name_level_up = "level_up.json"

def isOwner(ctx):
    return ctx.message.author.id == 386526455363928075 or ctx.message.author.id == 578966199212441603


@tasks.loop(minutes= 1)
async def changeStatus():
    game = discord.Game(random.choice(status))
    await bot.change_presence(status=discord.Status.dnd, activity=game)


@bot.event
async def on_ready():
    print("Ready !")
    changeStatus.start()
    roulette_veriication.start()


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Mmmmmmh, j'ai bien l'impression que cette commande n'existe pas :/")

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Il manque un argument.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Vous n'avez pas les permissions pour faire cette commande.")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("Oups vous ne pouvez utilisez cette commande.")
    if isinstance(error, discord.Forbidden):
        await ctx.send("Oups, je n'ai pas les permissions nécéssaires pour faire cette commmande")


@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    member = payload.member
    message = payload.message_id
    channel = payload.channel_id
    await sond.on_sondage_vote(payload, 1)
    await checkEmoji(payload)
    await secret.on_reaction(member,message, channel)

@bot.event
async def on_raw_reaction_remove(payload):
    await sond.on_sondage_vote(payload, -1)


@bot.event
async def on_message(message):
    if not message.author.bot:
        if not os.path.exists("level.json"):
            open("level.json", 'w').close()
        print('function load')
        with open('level.json', 'r') as f:
            users = json.load(f)
            print('file load')
        await update_data(users, message.author, message.guild)
        await add_experience(users, message.author, 4)
        await level_up(users, message.author, message.channel)

        with open('level.json', 'w') as f:
            json.dump(users, f)
    await bot.process_commands(message)
    await sond.on_message(message)
    await rolltime.on_message(message)

async def createNinjaRole(ctx):
    ninjaRole = await ctx.guild.create_role(name="Ninja",
                                            reason="Role montrant que vous avez atteint ou dépassé le niveau 5",
                                            color=0x2ecc71)

async def getNinjaRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Ninja":
            return role

    return await createNinjaRole(ctx)


async def update_data(users, user, server):
    if not str(server.id) in users:
        users[str(server.id)] = {}
        if not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['experience'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1
    elif not str(user.id) in users[str(server.id)]:
        users[str(server.id)][str(user.id)] = {}
        users[str(server.id)][str(user.id)]['experience'] = 0
        users[str(server.id)][str(user.id)]['level'] = 1


async def add_experience(users, user, exp):
    users[str(user.guild.id)][str(user.id)]['experience'] += exp


async def level_up(users, user, channel):
    xp = users[str(user.guild.id)][str(user.id)]['experience']
    lvl_start = users[str(user.guild.id)][str(user.id)]['level']
    lvl_end = int(((sqrt(xp+15312.5)-125/sqrt(2))/(25*sqrt(2)))*15)-14

    if lvl_start < lvl_end:
        await channel.send('{} vient de monter au niveau {}'.format(user.mention, lvl_end))
        #await message.edit(msg)
        users[str(user.guild.id)][str(user.id)]['level'] = lvl_end
    if lvl_start > lvl_end:
        #await message.edit(msgR)
        await channel.send('{} vient de régresser au niveau {}'.format(user.mention, lvl_end))
        users[str(user.guild.id)][str(user.id)]['level'] = lvl_end


@bot.command(aliases=['rank', 'lvl'])
async def level(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
        with open('level.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(ctx.guild.id)][str(member.id)]['level']
        exp = users[str(ctx.guild.id)][str(member.id)]['experience']
        embed = discord.Embed(title='Level {}'.format(lvl), description=f"{exp} XP ", color=discord.Color.green(), timestamp=ctx.message.created_at)
        embed.set_thumbnail(url= ctx.author.avatar_url)
        embed.set_author(name=ctx.author)
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Display Name:", value=member.display_name)
        await ctx.send(embed=embed)
    else:
        with open('level.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(ctx.guild.id)][str(member.id)]['level']
        exp = users[str(ctx.guild.id)][str(member.id)]['experience']
        embed = discord.Embed(title='Level {}'.format(lvl), description=f"{exp} XP", color=discord.Color.green())
        embed.set_author(name=member)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Display Name:", value=member.display_name)
        await ctx.send(embed=embed)

@bot.command()
async def giveXP(ctx, user: discord.Member, xp: int):  #A revoir
    if not isOwner(ctx):
        await ctx.send("Tu n'as pas les permissions... Tricheur!!!")
        return
    if not ctx.message.author.bot:
        if not os.path.exists("level.json"):
            open("level.json", 'w').close()
        print('function load')
        with open('level.json', 'r') as f:
            users = json.load(f)
            print('file load')
        await update_data(users, user, ctx.message.guild)
        await add_experience(users, user, xp)
        await level_up(users, user, ctx.message.channel)
        if xp > 0:
            await ctx.send("Le don à bel et bien eu lieu!!!")
        else:
            await ctx.send("Le retrait à bien eu lieu!!!")

        with open('level.json', 'w') as f:
            json.dump(users, f)


@bot.command()
async def botdescription(ctx):
    embed=discord.Embed(title="**Description du bot**", description="Je ne suis qu'un bot,\nUn simple robot,\nJe ne souhaite que votre bonheur\nEt être votre serviteur\nDu matin,\nJusqu'à la fin.", colour=discord.Colour.dark_orange())
    embed.set_thumbnail(url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4b70e5ec-0e08-49ce-bf70-097f33e91809/d3aawro-df401e06-f08d-413b-b064-9c3b1ee9e904.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNGI3MGU1ZWMtMGUwOC00OWNlLWJmNzAtMDk3ZjMzZTkxODA5XC9kM2Fhd3JvLWRmNDAxZTA2LWYwOGQtNDEzYi1iMDY0LTljM2IxZWU5ZTkwNC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.g1HwSgvprPz3FU-x49cr5NZCPUSBpio_opqUEFue3BY")
    embed.set_footer(text=f'Commande demandé par {ctx.author}')
    await ctx.send(embed=embed)

@bot.command()
async def coucou(ctx):
    await ctx.send("Coucou toi !")


format = "%a, %d %b %Y | %H:%M:%S %ZGMT"
@bot.command()
@commands.guild_only()
async def serverinfo(ctx):
    embed = discord.Embed(
        color = ctx.guild.owner.top_role.color
    )
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    channels = text_channels + voice_channels
    embed.set_thumbnail(url = str(ctx.guild.icon_url))
    embed.add_field(name = f"Information About **{ctx.guild.name}**: ", value = f":white_small_square: ID: **{ctx.guild.id}** \n:white_small_square: Owner: **{ctx.guild.owner}** \n:white_small_square: Location: **{ctx.guild.region}** \n:white_small_square: Creation: **{ctx.guild.created_at.strftime(format)}** \n:white_small_square: Members: **{ctx.guild.member_count}** \n:white_small_square: Channels: **{channels}** \n:white_small_square: Text channels: **{text_channels}** \n:white_small_square: Voice channels: **{voice_channels}** \n:white_small_square: Categories: **{categories}** \n:white_small_square: Description: **{str(ctx.guild.verification_level).upper()}**")
    await ctx.send(embed=embed)




@bot.command()
async def say(ctx, *text):
    await ctx.send(" ".join(text))
    await ctx.message.delete()


@bot.command()
async def info(ctx):
    message2 = f"Voici les informations disponibles: \nname \nmembercount \nnumberofchannels. \nSi vous désirez une information, merci d'entrez la commande €getinfo avec le nom de l'information que vous souhaiter (sans fautes d'orthographes)"
    await ctx.send(message2)


@bot.command()
async def getinfo(ctx, info):
    server = ctx.guild
    if info == "membercount":
        await ctx.send(server.member_count)
    elif info == "numberofchannels":
        await ctx.send(len(server.voice_channels) + len(server.text_channels))
    elif info == "name":
        await ctx.send(server.name)
    else:
        await ctx.send("Etrange... Je ne connais pas cela")


@bot.command()
@commands.has_role("Admin")
async def clear(ctx, nombre: int):
    await ctx.channel.purge(limit=nombre + 1)


@bot.command()
@commands.has_role("Admin")
async def ban(ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason=reason)
    embed = discord.Embed(title="**Banissement**", description="Un modérateur a frappé !", colour=0xad1457)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url, )
    embed.set_thumbnail(url="https://discordemoji.com/assets/emoji/BanneHammer.png")
    embed.add_field(name="Membre banni", value=user.name, inline=True)
    embed.add_field(name="Raison", value=reason, inline=True)
    embed.add_field(name="Modérateur", value=ctx.author.name, inline=True)
    embed.set_footer(text=random.choice(FunSentence))

    await ctx.send(embed=embed)
    await ctx.message.delete()


@bot.command()
@commands.has_role("Admin")
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason=reason)
            await ctx.send(f"{user} à été unban.")
            return
    await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")
    await ctx.message.delete()


@bot.command()
@commands.has_role("Admin")
async def kick(ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason=reason)
    await ctx.send(f"{user} à été kick.")
    await ctx.message.delete()

@bot.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles[1:]]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="\n".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)



@bot.command(aliases=['8ball'])
async def fortune (ctx, *message):
    message = " ".join(message)
    embed = discord.Embed(title="**Fortune**", description=f'***{message}***', color=0x8B0000)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url, )
    embed.set_thumbnail(url="https://clipground.com/images/question-mark-cartoon-clip-art-8.jpg")
    embed.add_field(name="réponse", value=random.choice(Fortune), inline=True)
    embed.set_footer(text=f"Requested by {ctx.author}")

    await ctx.send(embed=embed)


async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name="Muted",
                                            permissions=discord.Permissions(
                                                send_messages=False,
                                                speak=False),
                                            reason="Creation du role Muted pour mute des gens.",
                                            color=0x546e7a)
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages=False, speak=False)
    return mutedRole


async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role

    return await createMutedRole(ctx)


@bot.command()
@commands.has_role("Admin")
async def mute(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"{member.mention} a été mute !")
    await ctx.message.delete()


@bot.command()
@commands.has_role("Admin")
async def unmute(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason=reason)
    await ctx.send(f"{member.mention} a été unmute !")
    await ctx.message.delete()


@bot.command(pass_context = True)
@commands.has_role("Admin")
async def clean(ctx):
    amount= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    await ctx.channel.purge(limit=amount)

@bot.command(pass_context = True)
@commands.has_role("Luis")
async def cleanR(ctx):
    amount= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    await ctx.channel.purge(limit=amount)



messageModifHelp = {}



async def checkEmoji(payload: discord.RawReactionActionEvent):
    if not payload.member.guild_permissions.administrator:
        return
    guild = bot.get_guild(payload.guild_id)
    channel = guild.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    reaction = payload.emoji
    member = payload.member
    if message.author == payload.member:
        return
    if str(reaction) == "✅":
        await savePref(guild.id, True, False, channel)
    if str(reaction) == "❌":
        await savePref(guild.id, False, True, channel)
    if str(reaction) == "2️⃣":
        await savePref(guild.id, True, True, channel)

@bot.command()
async def config(ctx: Context, *args):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("Vous n'avez pas les permissions pour faire cette commande.")
        return
    if args[0] == "sondage":
        if args[1]=="set_channel":
            await sond.set_channel_sondage(ctx)
    elif args[0]=="help":
        message = await ctx.send(
             "Si vous voulez que quand un membre utilise une commande help, il recoive la commande en MP, cliquer sur :white_check_mark:. Si vous voulez qu'il le recoive sur le serveur, cliquer sur :x:. Si vous voulez qu'il recoive les deux, cliquer sur :two: ")
        await message.add_reaction("✅")
        await message.add_reaction("❌")
        await message.add_reaction("2️⃣")
        if not message.guild in messageModifHelp.keys():
            messageModifHelp[message.guild.id] = []
        messageModifHelp[message.guild.id].append(message)
    elif args [0]=="level_up_channel":
        with open(file_name_level_up, "r") as f:
            data = json.load(f)
            f.close()
        data[ctx.guild.id] = ctx.channel.id
        with open(file_name_level_up, "w") as f:
            json.dump(data, f)
            f.close()
        await ctx.channel.send("Le salon des messages de level-up est désormais le salon : " + ctx.channel.name)
    elif args[0] == "roles":
        if args[1]=="set_channel":
            await secret.set_channel(ctx)

async def savePref(guild_id, mp, serv, ctx):
    with open("helpConfig.json", "r") as f:
        data = json.load(f)
    data[str(guild_id)] = {}
    data[str(guild_id)]['mp'] = mp
    data[str(guild_id)]['serv'] = serv
    with open("helpConfig.json", "w") as f:
        json.dump(data, f)
    if mp:
        mpStr = "activer"
    else:
        mpStr = "désactiver"
    if serv:
        servStr = "activer"
    else:
        servStr = "désactiver"
    await ctx.send(f"Votre demande à bien été prise en compte! L'help en Mp est : {mpStr}, L'help sur le serveur : {servStr}")@bot.command()

@bot.command()
async def help(ctx, *args):
    with open("helpConfig.json", "r") as f:
        data=json.load(f)
        f.close()
    if not str(ctx.guild.id) in data.keys():
        data[str(ctx.guild.id)] = {}
        data[str(ctx.guild.id)]['mp'] = False
        data[str(ctx.guild.id)]['serv'] = True
        with open("helpConfig.json", "w") as f:
            json.dump(data, f)
            f.close()
    if data[str(ctx.guild.id)]['mp']:
        if len(args) == 0:
            member = ctx.message.author
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.set_thumbnail(
                url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4b70e5ec-0e08-49ce-bf70-097f33e91809/d3aawro-df401e06-f08d-413b-b064-9c3b1ee9e904.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNGI3MGU1ZWMtMGUwOC00OWNlLWJmNzAtMDk3ZjMzZTkxODA5XC9kM2Fhd3JvLWRmNDAxZTA2LWYwOGQtNDEzYi1iMDY0LTljM2IxZWU5ZTkwNC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.g1HwSgvprPz3FU-x49cr5NZCPUSBpio_opqUEFue3BY")
            embed.set_author(name='Liste des commandes')
            embed.set_footer(text=f"Commande demandé par {ctx.author}")

            embed.add_field(name="**Modération**", value="\n*€help modération*")
            embed.add_field(name="**Infos**", value="\n*€help infos*")
            embed.add_field(name="**Games**", value="\n*€help games*")
            embed.add_field(name="**Interaction**", value="\n*€help interaction*")


            await ctx.author.send(embed=embed)
        elif args[0] == "modération" or args[0]== "modo":
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.set_thumbnail(
                url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4b70e5ec-0e08-49ce-bf70-097f33e91809/d3aawro-df401e06-f08d-413b-b064-9c3b1ee9e904.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNGI3MGU1ZWMtMGUwOC00OWNlLWJmNzAtMDk3ZjMzZTkxODA5XC9kM2Fhd3JvLWRmNDAxZTA2LWYwOGQtNDEzYi1iMDY0LTljM2IxZWU5ZTkwNC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.g1HwSgvprPz3FU-x49cr5NZCPUSBpio_opqUEFue3BY")
            embed.set_author(name='Liste des commandes de modération')
            embed.set_footer(text=f"Commande demandé par {ctx.author}")
            embed.add_field(name="**config sondage set_channel**", value="Permet de choisir le salon sur lequel chaque sondage sera envoyé.**Attention, commande obligatoire à l'ajout du bot**")
            embed.add_field(name="**config roles set_channel**",
                            value="Permet de choisir le salon sur lequel chaque attribution de role sera envoyé.**Attention, commande obligatoire à l'ajout du bot**")
            embed.add_field(name="**config help**", value="Permet de choisir si la commande help doit être envoyé en MP, sur le serveur ou les deux en même temps.**Attention, commande obligatoire à l'ajout du bot**")
            embed.add_field(name="**kick**", value="Kick un membre du serveur. **Attention, après le nom de l'utilisateur, indiquez la raison!!**")
            embed.add_field(name="**mute**",
                            value="Crée et ajoute le role mute à un utilisateur. Il ne pourra plus parler à l'orale et à l'écrit")
            embed.add_field(name="**unmute**", value="Retire le role mute à un membre")
            embed.add_field(name="**clear**",
                            value="Nettoie le nombre séléctionner de message. **Attention, ne peut pas supprimer les messages de plus de 15 jours**")
            embed.add_field(name="**clean**",
                            value="Nettoie tout les messages d'un salon. **Attention, la commande est longue, les messages seront effacés progressivement. Ne pas spam la commande, l'opération peut prendre plusieurs heures.**")
            embed.add_field(name="**ban**", value="Bannie un membre du serveur. **Attention, après le nom de l'utilisateur, indiquez la raison!!**")
            embed.add_field(name="**unban**",
                            value="Débannie un membre du serveur. Vous devez entrez l'dentifiant du membre bannie.")
            embed.add_field(name="**say**",
                            value="Fait parler le bot")
            embed.add_field(name="**sondage**", value="Est il vraiment nécessaire de dire à quoi sert cette commande?")
            embed.add_field(name="**roles**", value="Donne le role lorsqu'on réagi à l'émojie.")


            await ctx.author.send(embed=embed)

        elif args[0] == "info":
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.set_thumbnail(
                url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4b70e5ec-0e08-49ce-bf70-097f33e91809/d3aawro-df401e06-f08d-413b-b064-9c3b1ee9e904.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNGI3MGU1ZWMtMGUwOC00OWNlLWJmNzAtMDk3ZjMzZTkxODA5XC9kM2Fhd3JvLWRmNDAxZTA2LWYwOGQtNDEzYi1iMDY0LTljM2IxZWU5ZTkwNC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.g1HwSgvprPz3FU-x49cr5NZCPUSBpio_opqUEFue3BY")
            embed.set_author(name='Liste des commandes d\'information')
            embed.set_footer(text=f"Commande demandé par {ctx.author}")
            embed.add_field(name="**botowner**", value="Donne l'identité des propriétaires du bot")
            embed.add_field(name="**serverinfo**", value="Vous donne les infos du server")
            embed.add_field(name="**getinfo**",
                            value="Permet de choisir une info précise")
            embed.add_field(name="**info**", value="Donne les infos disponibles pour le getinfo")
            embed.add_field(name="**userinfo**",
                            value="Donne des infos sur un membre du serveur. Par défaut, elle donnera les infos de la personne qui l'utilise, mais il est possible de de voir l'info de quelqu'un d'autre avec son @")
            embed.add_field(name="**botdescription**",
                            value="Donne la description du bot")
            embed.add_field(name="**ping**",
                            value="Donne le ping du bot")
            await ctx.author.send(embed=embed)

        elif args[0] == "games":
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.set_thumbnail(
                url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4b70e5ec-0e08-49ce-bf70-097f33e91809/d3aawro-df401e06-f08d-413b-b064-9c3b1ee9e904.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNGI3MGU1ZWMtMGUwOC00OWNlLWJmNzAtMDk3ZjMzZTkxODA5XC9kM2Fhd3JvLWRmNDAxZTA2LWYwOGQtNDEzYi1iMDY0LTljM2IxZWU5ZTkwNC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.g1HwSgvprPz3FU-x49cr5NZCPUSBpio_opqUEFue3BY")
            embed.set_author(name='Liste des commandes amusantes')
            embed.set_footer(text=f"Commande demandé par {ctx.author}")
            embed.add_field(name="**fortune**", value="Répond à votre question")
            embed.add_field(name="**prof**",
                            value="Citation de profs. Attention, il s'agit d'un easter egg. Si ça ne vous fait pas rire... C'est normal, vous n'avez pas la référence.")
            embed.add_field(name="**pub**", value="Fait une petite pub gratuite ;)")
            embed.add_field(name="**enigme**", value="Test votre cerveau")
            embed.add_field(name="**quiEsTu**", value="Donne l'indentité du bot (plusieurs réponses disponibles).")
            embed.add_field(name="**dice**", value="Lance un dé.")

            await ctx.author.send(embed=embed)
        elif args[0] == "interaction" or args[0]== "inter":
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.set_thumbnail(
                url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4b70e5ec-0e08-49ce-bf70-097f33e91809/d3aawro-df401e06-f08d-413b-b064-9c3b1ee9e904.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNGI3MGU1ZWMtMGUwOC00OWNlLWJmNzAtMDk3ZjMzZTkxODA5XC9kM2Fhd3JvLWRmNDAxZTA2LWYwOGQtNDEzYi1iMDY0LTljM2IxZWU5ZTkwNC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.g1HwSgvprPz3FU-x49cr5NZCPUSBpio_opqUEFue3BY")
            embed.set_author(name='Liste des commandes interactives')
            embed.set_footer(text=f"Commande demandé par {ctx.author}")
            embed.add_field(name="Bah quoi? On a le droit de faire ce type de commande nan?", value="**:white_small_square: angry\n:white_small_square: blush\n:white_small_square: cry**")

            await ctx.author.send(embed=embed)
    if data[str(ctx.guild.id)]['serv']:
        if len(args) == 0:
            member = ctx.message.author
            embed = discord.Embed(colour=discord.Colour.dark_teal())
            embed.set_thumbnail(
                url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4b70e5ec-0e08-49ce-bf70-097f33e91809/d3aawro-df401e06-f08d-413b-b064-9c3b1ee9e904.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNGI3MGU1ZWMtMGUwOC00OWNlLWJmNzAtMDk3ZjMzZTkxODA5XC9kM2Fhd3JvLWRmNDAxZTA2LWYwOGQtNDEzYi1iMDY0LTljM2IxZWU5ZTkwNC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.g1HwSgvprPz3FU-x49cr5NZCPUSBpio_opqUEFue3BY")
            embed.set_author(name='Liste des commandes')
            embed.set_footer(text=f"Commande demandé par {ctx.author}")

            embed.add_field(name="**Modération**", value="\n*€help modération*")
            embed.add_field(name="**Infos**", value="\n*€help infos*")
            embed.add_field(name="**Games**", value="\n*€help games*")
            embed.add_field(name="**Interaction**", value="\n*€help interaction*")

            await ctx.send(embed=embed)

        elif args[0] == "modération" or args[0]== "modo":
            embed = discord.Embed(colour=discord.Colour.dark_teal())
            embed.set_thumbnail(
                url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4b70e5ec-0e08-49ce-bf70-097f33e91809/d3aawro-df401e06-f08d-413b-b064-9c3b1ee9e904.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNGI3MGU1ZWMtMGUwOC00OWNlLWJmNzAtMDk3ZjMzZTkxODA5XC9kM2Fhd3JvLWRmNDAxZTA2LWYwOGQtNDEzYi1iMDY0LTljM2IxZWU5ZTkwNC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.g1HwSgvprPz3FU-x49cr5NZCPUSBpio_opqUEFue3BY")
            embed.set_author(name='Liste des commandes de modération')
            embed.set_footer(text=f"Commande demandé par {ctx.author}")
            embed.add_field(name="**config sondage set_channel**",
                            value="Permet de choisir le salon sur lequel chaque sondage sera envoyé.**Attention, commande obligatoire à l'ajout du bot**")
            embed.add_field(name="**config roles set_channel**",
                            value="Permet de choisir le salon sur lequel chaque attribution de role sera envoyé.**Attention, commande obligatoire à l'ajout du bot**")
            embed.add_field(name="**config help**",
                            value="Permet de choisir si la commande help doit être envoyé en MP, sur le serveur ou les deux en même temps.**Attention, commande obligatoire à l'ajout du bot**")
            embed.add_field(name="**kick**", value="Kick un membre du serveur. **Attention, après le nom de l'utilisateur, indiquez la raison!!**")
            embed.add_field(name="**mute**",
                            value="Crée et ajoute le role mute à un utilisateur. Il ne pourra plus parler à l'orale et à l'écrit")
            embed.add_field(name="**unmute**", value="Retire le role mute à un membre")
            embed.add_field(name="**clear**",
                            value="Nettoie le nombre séléctionner de message. **Attention, ne peut pas supprimer les messages de plus de 15 jours**")
            embed.add_field(name="**clean**",
                            value="Nettoie tout les messages d'un salon. **Attention, la commande est longue, les messages seront effacés progressivement. Ne pas spam la commande, l'opération peut prendre plusieurs heures.**")
            embed.add_field(name="**ban**", value="Bannie un membre du serveur. **Attention, après le nom de l'utilisateur, indiquez la raison!!**")
            embed.add_field(name="**unban**",
                            value="Débannie un membre du serveur. Vous devez entrez l'dentifiant du membre bannie.")
            embed.add_field(name="**say**",
                            value="Fait parler le bot")
            embed.add_field(name="**sondage**", value="Est il vraiment nécessaire de dire à quoi sert cette commande?")
            embed.add_field(name="**roles**", value="Donne le role lorsqu'on réagi à l'émojie.")

            await ctx.send(embed=embed)

        elif args[0] == "info":
            embed = discord.Embed(colour=discord.Colour.dark_teal())
            embed.set_thumbnail(
                url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4b70e5ec-0e08-49ce-bf70-097f33e91809/d3aawro-df401e06-f08d-413b-b064-9c3b1ee9e904.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNGI3MGU1ZWMtMGUwOC00OWNlLWJmNzAtMDk3ZjMzZTkxODA5XC9kM2Fhd3JvLWRmNDAxZTA2LWYwOGQtNDEzYi1iMDY0LTljM2IxZWU5ZTkwNC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.g1HwSgvprPz3FU-x49cr5NZCPUSBpio_opqUEFue3BY")
            embed.set_author(name='Liste des commandes d\'information')
            embed.set_footer(text=f"Commande demandé par {ctx.author}")
            embed.add_field(name="**botowner**", value="Donne l'identité des propriétaires du bot")
            embed.add_field(name="**serverinfo**", value="Vous donne les infos du server")
            embed.add_field(name="**getinfo**",
                            value="Permet de choisir une info précise")
            embed.add_field(name="**info**", value="Donne les infos disponibles pour le getinfo")
            embed.add_field(name="**userinfo**",
                            value="Donne des infos sur un membre du serveur. Par défaut, elle donnera les infos de la personne qui l'utilise, mais il est possible de de voir l'info de quelqu'un d'autre avec son @")
            embed.add_field(name="**botdescription**",
                            value="Donne la description du bot")
            embed.add_field(name="**ping**",
                            value="Donne le ping du bot")

            await ctx.send(embed=embed)
        elif args[0] == "games":
            embed = discord.Embed(colour=discord.Colour.dark_teal())
            embed.set_thumbnail(
                url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4b70e5ec-0e08-49ce-bf70-097f33e91809/d3aawro-df401e06-f08d-413b-b064-9c3b1ee9e904.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNGI3MGU1ZWMtMGUwOC00OWNlLWJmNzAtMDk3ZjMzZTkxODA5XC9kM2Fhd3JvLWRmNDAxZTA2LWYwOGQtNDEzYi1iMDY0LTljM2IxZWU5ZTkwNC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.g1HwSgvprPz3FU-x49cr5NZCPUSBpio_opqUEFue3BY")
            embed.set_author(name='Liste des commandes amusantes')
            embed.set_footer(text=f"Commande demandé par {ctx.author}")
            embed.add_field(name="**fortune**", value="Répond à votre question")
            embed.add_field(name="**prof**", value="Citation de profs. Attention, il s'agit d'un easter egg. Si ça ne vous fait pas rire... C'est normal, vous n'avez pas la référence.")
            embed.add_field(name="**pub**", value= "Fait une petite pub gratuite ;)")
            embed.add_field(name="**enigme**", value="Test votre cerveau")
            embed.add_field(name="**quiEsTu**", value="Donne l'indentité du bot (plusieurs réponses disponibles).")
            embed.add_field(name="**dice**", value="Lance un dé.")

            await ctx.send(embed=embed)
        elif args[0] == "interaction" or args[0]== "inter":
            embed = discord.Embed(colour=discord.Colour.dark_teal())
            embed.set_thumbnail(
                url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4b70e5ec-0e08-49ce-bf70-097f33e91809/d3aawro-df401e06-f08d-413b-b064-9c3b1ee9e904.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNGI3MGU1ZWMtMGUwOC00OWNlLWJmNzAtMDk3ZjMzZTkxODA5XC9kM2Fhd3JvLWRmNDAxZTA2LWYwOGQtNDEzYi1iMDY0LTljM2IxZWU5ZTkwNC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.g1HwSgvprPz3FU-x49cr5NZCPUSBpio_opqUEFue3BY")
            embed.set_author(name='Liste des commandes interactives')
            embed.set_footer(text=f"Commande demandé par {ctx.author}")
            embed.add_field(name="Bah quoi? On a le droit de faire ce type de commande nan?",
                            value="**:white_small_square: angry\n:white_small_square: blush\n:white_small_square: cry**")


            await ctx.send(embed=embed)


@bot.command()
async def sondage(ctx: discord.ext.commands.Context):
    await sond.realsondage(ctx)

@bot.command()
async def ping(ctx):
    latency = int(bot.latency*1000)
    await ctx.send(f'Pong! {latency} ms')

@bot.command()
async def botowner(ctx):
    await ctx.send("J'appartiens à agent tiger#1299 et au génialissime Jnath#5924. Ce sont eux (surtout Jnath) qui m'ont programmer, moi votre humble serviteur.")




@bot.command(aliases= ["easter_eggs"])
async def prof(ctx, *args):
    if len(args) == 0:
        member = ctx.message.author
        await ctx.send("Merci de rentrer un nom... Vous avez le choix entre Raymond et Fanjeaux.")

    elif args [0]== "Fanjeaux":
        embed = discord.Embed(title="**Easter_Eggs (prof)**", description=f'***Fanjeaux style :joy:***', color=0x71368a)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url, )
        embed.set_thumbnail(url="https://cdn3.iconfinder.com/data/icons/egg-head-emojis-yellow/100/Egg-Head_Emoji-Face-With-Tears-of-Joy-512.png")
        embed.add_field(name="Citation", value=random.choice(Fanjaux), inline=True)
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == "Raymond":
        embed = discord.Embed(title="**Easter_Eggs (prof)**", description=f'***Raymond style :joy:***', color=0x71368a)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url, )
        embed.set_thumbnail(
            url="https://cdn3.iconfinder.com/data/icons/egg-head-emojis-yellow/100/Egg-Head_Emoji-Face-With-Tears-of-Joy-512.png")
        embed.add_field(name="Citation", value=random.choice(Raymond), inline=True)
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)

@bot.command()
async def pub(ctx):
    member = ctx.message.author
    embed=discord.Embed(title="**PUB**", description="Il faut bien faire sa pub non?", color=0xf1c40f)
    embed.set_thumbnail(url= "https://i.pinimg.com/736x/66/f1/41/66f14166ca13bcb3988ba68b7d010d45.jpg")
    embed.add_field(name= "**Wattpad**", value="Abonnez vous à Eldoran Hell (@Eldoran_Hell), je vous recommande également Aélia Nightmare... Très bonne auteure!")
    embed.add_field(name="**Short Edition**",
                    value="Abonnez vous à Eldoran Hell !")
    embed.add_field(name="**Devienart**",
                    value="A réinitialisez")
    embed.add_field(name="**Instagramme**",
                    value="Abonnez vous à @Fabrice le watermelon et @Insta de peach")
    embed.add_field(name="Code épic games", value= "Entrez \"RFP\" dans la boutique Fortnite")
    embed.set_footer(text=f"Requested by {ctx.author}")

    await ctx.send(embed=embed)

@bot.command()
async def quiEsTu(ctx):
    await ctx.send(random.choice(Quiestu))

@bot.command()
async def angry(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=":anger: **Angry**", description=f'{ctx.author} est en colère!!!', color= 0x992d22)
    embed.set_image(url=random.choice(Angry))
    embed.set_footer(text="Nan... Franchement... Si vous regardez ici car vous voulez savoir qui a demandé cette commande, vous m'exaspérer. C'est marqué au début de l'embed!!")

    await ctx.send(embed=embed)

@bot.command()
async def blush(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=":blush: **Blush**", description="Arretes, tu vas me faire rougir >///<", color= 0x992d22)
    embed.set_image(url=random.choice(Blush))
    embed.set_footer(
        text=f'Cette commande concerne {ctx.author}')

    await ctx.send(embed=embed)

@bot.command()
async def cry(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=":sob: **Cry**", description=f'{ctx.author} est très triste maintenant uwu', color= 0x992d22)
    embed.set_image(url=random.choice(Cry))
    embed.set_footer(
        text= "C'est trop triste, moi aussi je vais pleurer...")

    await ctx.send(embed=embed)


@bot.command()
async def dice(ctx, *args):
    if len(args)==0:
        await ctx.send("Quel type de dé voulez vous lancer? Merci de rentré une des valeur suivant: 6, 8, 16 ou bien 20.")
    elif args [0]== "6":
        résultat= random.choice(Dé)
        embed=discord.Embed(colour=discord.Colour.dark_grey())
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/it/4/4f/Duke_Delvin.png")
        embed.set_author(name="Lancé de dé")
        embed.add_field(name="Et tu as obtenu un..", value=f'{résultat}')
        embed.set_footer(text="Alors... es tu la relève de Duke Devlin?")

        await ctx.send(embed=embed)
    elif args[0]=="8":
        résultat = random.choice(Dé8)
        embed = discord.Embed(colour=discord.Colour.dark_grey())
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/it/4/4f/Duke_Delvin.png")
        embed.set_author(name="Lancé de dé")
        embed.add_field(name="Et tu as obtenu un..", value=f'{résultat}')
        embed.set_footer(text="Alors... es tu la relève de Duke Devlin?")

        await ctx.send(embed=embed)
    elif args[0] == "16":
        résultat = random.choice(Dé16)
        embed = discord.Embed(colour=discord.Colour.dark_grey())
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/it/4/4f/Duke_Delvin.png")
        embed.set_author(name="Lancé de dé")
        embed.add_field(name="Et tu as obtenu un..", value=f'{résultat}')
        embed.set_footer(text="Alors... es tu la relève de Duke Devlin?")

        await ctx.send(embed=embed)
    elif args[0] == "20":
        résultat = random.choice(Dé20)
        embed = discord.Embed(colour=discord.Colour.dark_grey())
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/it/4/4f/Duke_Delvin.png")
        embed.set_author(name="Lancé de dé")
        embed.add_field(name="Et tu as obtenu un..", value=f'{résultat}')
        embed.set_footer(text="Alors... es tu la relève de Duke Devlin?")

        await ctx.send(embed=embed)



@bot.command()
async def enigme(ctx, *args):
    if len(args) == 0:
        await ctx.send("Merci de choisir une énigme entre 1 et 13, vous pouvez aussi choisir l'énigme hardcore, qui est la plus dure du monde... Quand vous voudrez la solution, rentrer la commande solution avec le numéro de l'énigme")
    elif args[0] == '1':
        embed=discord.Embed(title="**Enigme**", description="Saurez-vous réfléchir de la bonne façon?", color= 0x99aab5)
        embed.set_thumbnail(url="https://sain-et-naturel.com/wp-content/uploads/2016/03/Enigme.jpg")
        embed.add_field(name="Enigme numéro 1:", value="Pouvez vous me donner trois jours consécutifs, sans utiliser Lundi, Mardi, Mercredi, Jeudi, Vendredi, Samedi, Dimanche et des nombres?")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '2':
        embed=discord.Embed(title="**Enigme**", description="Saurez-vous réfléchir de la bonne façon?", color= 0x99aab5)
        embed.set_thumbnail(url="https://sain-et-naturel.com/wp-content/uploads/2016/03/Enigme.jpg")
        embed.add_field(name="Enigme numéro 2:", value="INE INE INE INE \nMAIS MAIS \n6666666666 \nQui suis-je?\n(indice: je suis une personnage historique)")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '3':
        embed=discord.Embed(title="**Enigme**", description="Saurez-vous réfléchir de la bonne façon?", color= 0x99aab5)
        embed.set_thumbnail(url="https://sain-et-naturel.com/wp-content/uploads/2016/03/Enigme.jpg")
        embed.add_field(name="Enigme numéro 3:", value="Je suis précieux et on me garde avec précaution. Cependant, plus j'ai de gardiens, moins je suis protégé. Qui suis je?")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '4':
        embed=discord.Embed(title="**Enigme**", description="Saurez-vous réfléchir de la bonne façon?", color= 0x99aab5)
        embed.set_thumbnail(url="https://sain-et-naturel.com/wp-content/uploads/2016/03/Enigme.jpg")
        embed.add_field(name="Enigme numéro 4:", value="Quel être, pourvu d'une seule voix, a d'abord quatre jambes le matin, puis deux jambes le midi, et trois jambes le soir ?")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '5':
        embed=discord.Embed(title="**Enigme**", description="Saurez-vous réfléchir de la bonne façon?", color= 0x99aab5)
        embed.set_thumbnail(url="https://sain-et-naturel.com/wp-content/uploads/2016/03/Enigme.jpg")
        embed.add_field(name="Enigme numéro 5:", value="Avant-hier, Catherine avait 17 ans ; l'année prochaine, elle aura 20 ans. Comment est-ce possible ?")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '6':
        embed=discord.Embed(title="**Enigme**", description="Saurez-vous réfléchir de la bonne façon?", color= 0x99aab5)
        embed.set_thumbnail(url="https://sain-et-naturel.com/wp-content/uploads/2016/03/Enigme.jpg")
        embed.add_field(name="Enigme numéro 6:", value="Plus je suis chaud,plus je suis frais. \nQui suis-je ?")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '7':
        embed=discord.Embed(title="**Enigme**", description="Saurez-vous réfléchir de la bonne façon?", color= 0x99aab5)
        embed.set_thumbnail(url="https://sain-et-naturel.com/wp-content/uploads/2016/03/Enigme.jpg")
        embed.add_field(name="Enigme numéro 7:", value="Quand je sèche, je me mouille.\nQui suis-je ?")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == 'hardcore':
        embed=discord.Embed(title="**Enigme**", description="Juste... Bon courage", color= 0x99aab5)
        embed.set_thumbnail(url="https://sain-et-naturel.com/wp-content/uploads/2016/03/Enigme.jpg")
        embed.add_field(name="Enigme la plus dure du monde:", value="Derrière trois personnages A, B et C se cachent les dieux Vrai, Faux et Aléatoire. Vrai répond toujours la vérité, Faux répond toujours le contraire de la vérité, et Aléatoire choisit ses réponses au hasard. Votre tâche est de dévoiler les identités de A, B et C en posant uniquement trois questions dont la réponse est vrai ou faux. Les dieux comprennent le français mais ils répondront à vos questions dans leur propre langue, c'est-à-dire par da et ja. Vous ne savez pas à quoi ces réponses correspondent.\nVous pouvez interroger un dieu plusieurs fois (et alors un dieu ne sera pas du tout questionné).\nLa deuxième question et à qui s'adresse celle-ci peut dépendre de la réponse à la première question. De même pour le choix de la troisième.\nAléatoire peut être considéré comme décidant ses réponses à toute question vrai-faux par un jet à pile ou face : si la pièce tombe sur face, il dira da ; si elle tombe sur pile, ja.")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '8':
        embed = discord.Embed(title="**Enigme**", description="Saurez-vous réfléchir de la bonne façon?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://sain-et-naturel.com/wp-content/uploads/2016/03/Enigme.jpg")
        embed.add_field(name="Enigme numéro 8:",
                        value="Vous êtes devant deux portes, une bonne et une mauvaise. Devant chacune d'entre elles se trouve un garde. L'un dit la vérité et l'autre dit le contraire.\nQuelle question devez vous poser?")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '9':
        embed=discord.Embed(title="**Enigme**", description="Saurez-vous réfléchir de la bonne façon?", color= 0x99aab5)
        embed.set_thumbnail(url="https://sain-et-naturel.com/wp-content/uploads/2016/03/Enigme.jpg")
        embed.add_field(name="Enigme numéro 9:", value="J'ai 192 poule. Poule ne prend pas de 's' pourquoi ?")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '10':
        embed = discord.Embed(title="**Enigme**", description="Saurez-vous réfléchir de la bonne façon?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://sain-et-naturel.com/wp-content/uploads/2016/03/Enigme.jpg")
        embed.add_field(name="Enigme numéro 10:", value="Une école reçoit la visite d'un inspecteur. Celui-ci a comme mission de valider les connaissances des élèves en fin d'année. Une classe l’impressionne particulièrement, chaque fois qu'il pose une question tous les élèves lèvent le bras avec enthousiasme. De plus, l'enseignant choisit chaque fois un élève différent pour répondre, et celui-ci donne toujours la bonne réponse.\nComment est-ce possible ?")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '11':
        embed = discord.Embed(title="**Enigme**", description="Saurez-vous réfléchir de la bonne façon?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://sain-et-naturel.com/wp-content/uploads/2016/03/Enigme.jpg")
        embed.add_field(name="Enigme numéro 11:", value="Il y a 10 rats et 1000 bouteilles de vin dont une empoisonnée. Si un rat boit de la bouteille empoisonnée, il meurt au bout d’une heure. Votre but est de déterminer quelle est la bouteille empoisonnée en donnant aux rats à boire des bouteilles de vin selon la combinaison que vous souhaitez puis en constatant quels sont les rats morts au bout d’une heure. Comment faites-vous ?")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '12':
        embed = discord.Embed(title="**Enigme**", description="Saurez-vous réfléchir de la bonne façon?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://sain-et-naturel.com/wp-content/uploads/2016/03/Enigme.jpg")
        embed.add_field(name="Enigme numéro 12:", value="100 nains sont en file indienne. Chaque nain porte un chapeau, de couleur rouge ou bleue, mais ne le voit pas. Il peut cependant voir les chapeaux de tous les nains devant lui dans la file. Le défi est le suivant : chacun leur tour, et en partant du dernier nain, les nains vont devoir deviner la couleur de leur chapeau et la dire à voie haute. Ils peuvent, avant la pose des chapeaux, se concerter sur une stratégie. Quelle stratégie peuvent-ils adopter pour qu'au moins 99 d'entre eux devinent correctement la couleur de leur chapeau ?")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '13':
        embed=discord.Embed(title="**Enigme**", description="Saurez-vous réfléchir de la bonne façon?", color= 0x99aab5)
        embed.set_thumbnail(url="https://sain-et-naturel.com/wp-content/uploads/2016/03/Enigme.jpg")
        embed.add_field(name="Enigme numéro 13:", value="Il y a 99 loups et 1 mouton. Tout loup veut manger le mouton, mais s'il le mange il se transforme lui-même en mouton, et risque donc d'être mangé à son tour. Les loups ne veulent pas mourir : ils ne vont donc pas manger le mouton s'ils savent qu'ils vont être mangés ensuite. Tous les loups adoptent la meilleure stratégie. Le mouton est-il mangé ?")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    else:
        await ctx.send("Merci de rentrer une valeur valide!! Si vous voulez savoir les valeurs disponibles, merci rentrer la commande énigme sans aucun argument.")
@bot.command()
async def solution(ctx, *args):
    if len(args) == 0:
        await ctx.send("Il manque un élément!!")
    elif args[0] == '1':
        embed = discord.Embed(title="**Solution**", description="Avez vous la bonne réponse?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://www.samrantech.com/wp-content/uploads/2016/01/Solutions1-1.jpg")
        embed.add_field(name="Solution numéro 1:",
                        value="Il fallait dire par exemple: \"Hier, aujourd\'hui et demain\". Il s'agit bien de trois jours consécutifs.")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '2':
        embed = discord.Embed(title="**Solution**", description="Avez vous la bonne réponse?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://www.samrantech.com/wp-content/uploads/2016/01/Solutions1-1.jpg")
        embed.add_field(name="Solution numéro 2:",
                        value="Il y a quatre \"Ine\", deux \"Mais\" et dix \"6\". Donc je suis Catherine de Médicis.")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '3':
        embed = discord.Embed(title="**Solution**", description="Avez vous la bonne réponse?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://www.samrantech.com/wp-content/uploads/2016/01/Solutions1-1.jpg")
        embed.add_field(name="Solution numéro 3:",
                        value="Je suis un secret. En effet je suis précieux, mais plus il y a de monde au courant, moins il est secret.")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '4':
        embed = discord.Embed(title="**Solution**", description="Avez vous la bonne réponse?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://www.samrantech.com/wp-content/uploads/2016/01/Solutions1-1.jpg")
        embed.add_field(name="Solution numéro 4:",
                        value="Oui... Il s'agit de l'énigme du Sphinx à Oedipe... Bon, la réponse est l'Homme... Je vous laisse savoir pourquoi :wink:")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '5':
        embed = discord.Embed(title="**Solution**", description="Avez vous la bonne réponse?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://www.samrantech.com/wp-content/uploads/2016/01/Solutions1-1.jpg")
        embed.add_field(name="Solution numéro 5:",
                        value="Hier, on était le 31 décembre, elle a eu 18 ans. Cette année, elle va avoir 19 ans et l'année prochaine, 20 ans.")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '6':
        embed = discord.Embed(title="**Solution**", description="Avez vous la bonne réponse?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://www.samrantech.com/wp-content/uploads/2016/01/Solutions1-1.jpg")
        embed.add_field(name="Solution numéro 6:",
                        value="Le pain... Rien à rajouter.")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '7':
        embed = discord.Embed(title="**Solution**", description="Avez vous la bonne réponse?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://www.samrantech.com/wp-content/uploads/2016/01/Solutions1-1.jpg")
        embed.add_field(name="Solution numéro 7:",
                        value="Une serviette.")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == 'hardcore':
        embed = discord.Embed(title="**Solution**", description="Si vous avez la réponse... Respect", color=0x99aab5)
        embed.set_thumbnail(url="https://www.samrantech.com/wp-content/uploads/2016/01/Solutions1-1.jpg")
        embed.add_field(name="Solution de l'énigme la plus dure du monde:", value="On déduit le protocole suivant :\nÉtape 1 : Demander à B, « Si je vous demandais \"Est-ce que A est Aléatoire\", répondriez-vous ja ? ». Si B répond ja, alors ou B est Aléatoire (et a répondu au hasard), ou B n'est pas Aléatoire, et sa réponse indique que A l'est ; dans les deux cas, C n'est pas aléatoire. Si B répond da, alors ou B est Aléatoire, ou sa réponse indique que A n'est pas Aléatoire ; dans les deux cas, A n'est pas Aléatoire.\nÉtape 2 : Demander au dieu identifié comme non aléatoire à l'étape 1 (A ou C) : « Si je vous demandais \"Êtes-vous Vrai\", répondriez-vous ja ? ». Comme il n'est pas Aléatoire, s'il répond ja, il est Vrai et sinon il est Faux.\nÉtape 3 : Demander au même dieu : « Si je vous demandais \"Est-ce que B est Aléatoire ?\", répondriez-vous ja ? ». On en déduit si B est Aléatoire ou non puis on finit par élimination.\n Pour plus d'info, allez sur wikipedia, sinon je dépasse les 2000 caractères.")

        await ctx.send(embed=embed)
    elif args[0] == '8':
        embed = discord.Embed(title="**Solution**", description="Avez vous la bonne réponse?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://www.samrantech.com/wp-content/uploads/2016/01/Solutions1-1.jpg")
        embed.add_field(name="Solution numéro 8:",
                        value="La question que vous devez poser est: \"Celui qui dit les vérité est il devant la bonne porte?\"")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '9':
        embed = discord.Embed(title="**Solution**", description="Avez vous la bonne réponse?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://www.samrantech.com/wp-content/uploads/2016/01/Solutions1-1.jpg")
        embed.add_field(name="Solution numéro 9:",
                        value="1 9 2 poule = un oeuf de poule")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '10':
        embed = discord.Embed(title="**Solution**", description="Avez vous la bonne réponse?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://www.samrantech.com/wp-content/uploads/2016/01/Solutions1-1.jpg")
        embed.add_field(name="Solution numéro 10:",
                        value="L'enseignant et les élèves sont de mèche. Le principe est simple: Chaque fois qu'une question est posée, tous les écoliers qui connaissent la réponse lèvent le bras droit et les autres, le gauche.")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '11':
        embed = discord.Embed(title="**Solution**", description="Avez vous la bonne réponse?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://www.samrantech.com/wp-content/uploads/2016/01/Solutions1-1.jpg")
        embed.add_field(name="Solution numéro 11:",
                        value="L'idée ici est de faire correspondre une bouteille de vin avec un sous-ensemble des 10 rats. En effet, il y a 10 rats donc 2^10=1024 sous-ensembles possibles de rats, donc plus que le nombre de bouteilles. En pratique, on numérote les rats de 1 à 10, et les bouteilles de 1 à 1000, puis pour la bouteille numéro k, on écrit k en écriture binaire ; comme k est inférieur à 2^10, son écriture binaire comportera au maximum 10 chiffres et s’écrira donc a_1, a_2,…, a_10, avec a_p valant 0 ou 1. Puis pour chaque entier p entre 1 et 10, on donnera à boire de la bouteille k au rat numéro p si a_p=1. À la fin, on constate quels sont les rats morts, et on trouve ainsi l’écriture binaire associée : b_1, b_2…b_10, avec b_p=1 si le rat p est mort et 0 sinon, puis on convertit ce nombre en base décimale et on trouve ainsi la bouteille empoisonnée.")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '12':
        embed = discord.Embed(title="**Solution**", description="Avez vous la bonne réponse?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://www.samrantech.com/wp-content/uploads/2016/01/Solutions1-1.jpg")
        embed.add_field(name="Solution n°12:",
                        value="La stratégie est la suivante : le premier nain va dire « bleu » si le nombre de chapeaux bleus parmi les 99 nains devant lui est pair, « rouge » sinon. Entendant cela, le deuxième nain va à son tour compter le nombre de chapeaux bleus parmi les 98 nains devant lui. Si celui-ci a la même parité que pour le premier nain, alors le nombre de chapeaux bleus n'a pas varié et le chapeau du deuxième nain est rouge. Sinon, puisque le nombre de chapeaux bleus a varié, c'est que le chapeau du deuxième nain est bleu. Le deuxième nain peut donc deviner correctement la couleur de son chapeau. Puis, ayant entendu l'information donnée par le premier nain et la couleur du chapeau du deuxième nain, le troisième nain va pouvoir connaître la parité du nombre de chapeaux bleus parmi lui et les 97 nains devant lui : il s'agira de celle indiquée par le premier nain si le deuxième nain avait un chapeau rouge, et son inverse sinon. De façon générale, le n-ème nain va pouvoir deviner la couleur de son chapeau.")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    elif args[0] == '13':
        embed = discord.Embed(title="**Solution**", description="Avez vous la bonne réponse?",
                              color=0x99aab5)
        embed.set_thumbnail(url="https://www.samrantech.com/wp-content/uploads/2016/01/Solutions1-1.jpg")
        embed.add_field(name="Solution numéro 13:",
                        value="S'il n'y avait que n=1 loup, le loup mangerait le mouton, car il saurait qu'il ne serait pas mangé ensuite. S'il y avait n=2 loups, aucun ne mangerait le mouton. En effet, si un loup mangeait le mouton, il se transformerait en mouton et serait mangé par le seul loup restant (cas n=1). S'il y avait n=3 loups, un loup mangerait le mouton. En effet, il se transformerait alors en mouton, mais il ne resterait alors que 2 loups. Et on sait que lorsqu'il n'y a que 2 loups et 1 mouton, personne ne mange le mouton (cas n=2). De façon générale, on s'aperçoit que le mouton est mangé lorsque n est impair et qu'il n'est pas mangé lorsque n est pair. Ici, pour n=99, le mouton est mangé.")
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)
    else:
        await ctx.send("Merci de rentrer une valeur valide!!")

@bot.command()
async def roles(ctx: Context,test: discord.Role, *args):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("T'as pas les perms gamin.")
        return
    t = ""
    for i in args:
        print(i)
        t += i + " "
    await secret.add_message(test, ctx.guild, t)

@bot.command()
async def roulette(ctx):
    await rolltime.create_roulette(ctx)




@tasks.loop(seconds= 15)
async def roulette_veriication():
    await rolltime.roulette_verif(bot)




bot.run('ODA2NDU0ODYyMzc5NjE0MjI4.YBprng.l5sAw_Ix24seftwK6ahPeHVRvSE')
