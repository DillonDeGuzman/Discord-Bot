import discord
from discord.ext import commands
from discord import app_commands

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            guild = discord.Object(id=808787224421204029)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')

        except Exception as e:
            print(f'Error syncing commands: {e}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}')

    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')

intents = discord.Intents.default()
intents.message_content = True    
client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=808787224421204029)

@client.tree.command(name="hello", description="Say hello!", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there!")

@client.tree.command(name="printer", description="I will printer whatever you give me!", guild=GUILD_ID)
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

@client.tree.command(name="tft_comps", description="Best TFT Comps", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("https://mobalytics.gg/tft/team-comps")

@client.tree.command(name="tft_tools", description="Stats for TFT items and units", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("https://tactics.tools/")

@client.tree.command(name="tft_academy", description="Best comps from Challenger TFT players Dishsoap and Frodan", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("https://tftacademy.com/")
client.run('MTM1MTY4NzE4NjAyMTM1NTU3MA.G1-WPt.cq8zdQ9FDsYRmLTrH5hGOQTRZth3cE_-PzyOLI')
