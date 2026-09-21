import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

# Read DISCORD_TOKEN from the local .env file.
# Never put the real token directly in this Python file.
load_dotenv()

GUILD_ID = 808787224421204029


class Client(commands.Bot):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

        activity = discord.Activity(
            type=discord.ActivityType.watching,
            name="over the TFT realm",
        )
        await self.change_presence(activity=activity)

        try:
            guild = discord.Object(id=GUILD_ID)
            synced = await self.tree.sync(guild=guild)
            print(f"Synced {len(synced)} commands to guild {guild.id}")
        except Exception as error:
            print(f"Error syncing commands: {error}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("hello"):
            await message.channel.send(f"Hi there {message.author}")

    async def on_reaction_add(self, reaction, user):
        if user == self.user:
            return

        await reaction.message.channel.send("You reacted")


intents = discord.Intents.default()
intents.message_content = True

client = Client(command_prefix="!", intents=intents)
GUILD = discord.Object(id=GUILD_ID)


@client.tree.command(
    name="hello",
    description="Say hello!",
    guild=GUILD,
)
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there!")


@client.tree.command(
    name="printer",
    description="I will print whatever you give me!",
    guild=GUILD,
)
async def printer(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(text)


@client.tree.command(
    name="tft_comps",
    description="Best TFT comps",
    guild=GUILD,
)
async def tft_comps(interaction: discord.Interaction):
    await interaction.response.send_message(
        "https://mobalytics.gg/tft/team-comps"
    )


@client.tree.command(
    name="tft_tools",
    description="Stats for TFT items and units",
    guild=GUILD,
)
async def tft_tools(interaction: discord.Interaction):
    await interaction.response.send_message(
        "https://tactics.tools/"
    )


@client.tree.command(
    name="tft_academy",
    description="Best comps from Challenger TFT players Dishsoap and Frodan",
    guild=GUILD,
)
async def tft_academy(interaction: discord.Interaction):
    await interaction.response.send_message(
        "https://tftacademy.com/"
    )


token = os.getenv("DISCORD_TOKEN")

if not token:
    raise RuntimeError(
        "DISCORD_TOKEN was not found. Check that .env is beside main.py "
        "and contains DISCORD_TOKEN=your_new_token"
    )

client.run(token)