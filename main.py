import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = "hb!"

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(
    command_prefix=PREFIX,
    intents=intents
)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

async def main():
    async with bot:
        await bot.load_extension("music")
        await bot.start(TOKEN)

asyncio.run(main())
