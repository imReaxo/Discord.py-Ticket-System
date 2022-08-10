#----imports & froms----#
import discord
import asyncio
import datetime
import discord_components
from discord.ext import commands
from discord_components import Button, Select, SelectOption, ComponentsBot, interaction
from discord_components.component import ButtonStyle
#----imports & froms----#


#----config----#
TOKEN = "your bot token"
PREFIX = "your bot prefix"


#----core----#
client = ComponentsBot(f"{PREFIX}")
#----core----#

#----on ready----#
@client.command()
async def on_ready():
    print("bot is ready")
    print("code by Reaxo")

#----ticket----#
id_category = #ticket category id#
id_channel_ticket_logs = #ticket log channel id#
embed_color = 0xfcd005 


@client.command()
@commands.has_permissions(administrator=True)
async def ticket(ctx):
    await ctx.message.delete()


    embed = discord.Embed(title ='Tickets', description ="Welcome to tickets system :ticket:", color=embed_color) 

    await ctx.send(
        embed = embed,

        components = [
            Button(
                custom_id = 'Ticket',
                label = "Create a ticket",
                style = ButtonStyle.green,
                emoji ='🔧')
        ]
    )


@client.event
async def on_button_click(interaction):

    canal = interaction.channel
    canal_logs = interaction.guild.get_channel(id_channel_ticket_logs)

    if interaction.component.custom_id == "Ticket":
        await interaction.send(

            components = [
                Select(
                    placeholder = "How can we help you?",
                    options = [
                        SelectOption(label="Question", value="question", description='If you have a simple question.', emoji='❔'),
                        SelectOption(label="Help", value="help", description='If you need help from us.', emoji='🔧'),
                        SelectOption(label="Report", value="report", description='To report a misbehaving user.', emoji='🚫'),
                    ],
                    custom_id = "menu")])



    elif interaction.component.custom_id == 'close_ticket':

        embed_cerrar_ticket = discord.Embed(description=f"⚠️ Are you sure you want to close the ticket?", color=embed_color)
        await canal.send(interaction.author.mention, embed=embed_cerrar_ticket, 
                        components = [[
                        Button(custom_id = 'close_yes', label = "Yes", style = ButtonStyle.green),
                        Button(custom_id = 'close_no', label = "No", style = ButtonStyle.red)]])


    elif interaction.component.custom_id == 'close_yes':

        await canal.delete()
        embed_logs = discord.Embed(title="Tickets", description=f"", timestamp = datetime.datetime.utcnow(), color=embed_color)
        embed_logs.add_field(name="Ticket", value=f"{canal.name}", inline=True)
        embed_logs.add_field(name="Closed by", value=f"{interaction.author.mention}", inline=False)
        embed_logs.set_thumbnail(url=interaction.author.avatar_url)
        await canal_logs.send(embed=embed_logs)


    elif interaction.component.custom_id == 'close_no':
        await interaction.message.delete()

@client.event
async def on_select_option(interaction):
    if interaction.component.custom_id == "menu":

        guild = interaction.guild
        category = discord.utils.get(interaction.guild.categories, id = id_category)


        if interaction.values[0] == 'question':

            channel = await guild.create_text_channel(name=f'❔┃{interaction.author.name}-ticket', category=category)
            

            await channel.set_permissions(interaction.guild.get_role(interaction.guild.id),
                            send_messages=False,
                            read_messages=False)
            await channel.set_permissions(interaction.author, 
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True)
                                                

            await interaction.send(f'> The {channel.mention} channel was created to solve your questions.', delete_after= 3)

            embed_question = discord.Embed(title=f'Question - Hi {interaction.author.name}!', description='In this ticket we have an answer to your question.\n\nIf you cant get someone to help you, Only 1 time mention the staff for `🔔 Call staff', color=embed_color)
            embed_question.set_thumbnail(url=interaction.author.avatar_url)


            await channel.send(interaction.author.mention, embed=embed_question,
            

             components = [[
                    Button(custom_id = 'close_ticket', label = "Close ticket", style = ButtonStyle.red, emoji ='🔐')]])


        elif interaction.values[0] == 'help':

            channel = await guild.create_text_channel(name=f'🔧┃{interaction.author.name}-ticket', category=category)
            

            await channel.set_permissions(interaction.guild.get_role(interaction.guild.id),
                            send_messages=False,
                            read_messages=False)
            await channel.set_permissions(interaction.author, 
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True)



            await interaction.send(f'> The {channel.mention} channel was created to help you.', delete_after= 3)

            embed_question = discord.Embed(title=f'Help - ¡Hi {interaction.author.name}!', description='In this ticket we can help you with whatever you need.\n\nIf you cant get someone to help you, Only 1 time mention the staff for `🔔 Call staff`.', color=embed_color)
            embed_question.set_thumbnail(url=interaction.author.avatar_url)


            await channel.send(interaction.author.mention, embed=embed_question, 

            components = [[
                    Button(custom_id = 'close_ticket', label = "Close ticket", style = ButtonStyle.red, emoji ='🔐')]])



        elif interaction.values[0] == 'report':


            channel = await guild.create_text_channel(name=f'🚫┃{interaction.author.name}-ticket', category=category)


            await channel.set_permissions(interaction.guild.get_role(interaction.guild.id),
                            send_messages=False,
                            read_messages=False)
            await channel.set_permissions(interaction.author, 
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True)


            await interaction.send(f'> The {channel.mention} channel was created to report to the user.', delete_after= 3)


            embed_question = discord.Embed(title=f'Report - ¡Hi {interaction.author.name}!', description='In this ticket we can help you with your report.\n\nIf you cant get someone to help you, Only 1 time mention the staff for `🔔 Call staff`.', color=embed_color)
            embed_question.set_thumbnail(url=interaction.author.avatar_url)

            await channel.send(interaction.author.mention, embed=embed_question, 
            

            components = [[
                    Button(custom_id = 'close_ticket', label = "Close ticket", style = ButtonStyle.red, emoji ='🔐')]])
#----ticket----#

client.run(TOKEN)