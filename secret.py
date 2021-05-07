import discord
import json
import discord.ext.commands

file_name_secret= "secret.json"
async def add_message(role: discord.Role, guild: discord.Guild, message: str):
    with open("secret.json", "r") as f:
        data = json.load(f)
        print(str(guild.id) in data.keys())


    if str(guild.id) in data.keys():
        print(True)
        embed = discord.Embed(title="Role", color=0x9236dd)
        print(True)
        embed.add_field(name="Message :", value=message, inline=False)
        print(True)
        embed.add_field(name="Role :", value=role.mention, inline=True)
        print(True)
        embed.add_field(name="Réagi avec l'émoji pour avoir le role :", value=":regional_indicator_a:", inline=True)
        print(True)
        channel = guild.get_channel(data[str(guild.id)])
        print(True)
        msg: discord.Message = await channel.send(embed=embed)
        print(True)
        await msg.add_reaction("🇦")
        if not str(guild.id) in data["message_give_role"]:
            data["message_give_role"][str(guild.id)] = {}
        data["message_give_role"][str(guild.id)][str(msg.id)] = role.id
    print(str(guild.id) in data.keys())
    with open("secret.json", "w") as f:
        json.dump(data, f)
        f.close()


async def on_reaction(member: discord.Member, message: int, channel: int):
    with open("secret.json", "r") as f:
        data = json.load(f)
        f.close()
    guild: discord.Guild = member.guild
    if str(member.guild.id) in data.keys():
        if data[str(guild.id)] == channel:
           await  member.add_roles(guild.get_role(data["message_give_role"][str(guild.id)][str(message)]))


def set_channel(ctx: discord.ext.commands.Context):
    with open(file_name_secret, "r") as f:
        data = json.load(f)
        f.close()
    data[str(ctx.guild.id)] = ctx.channel.id
    with open(file_name_secret, "w") as f:
        json.dump(data, f)
        f.close()
