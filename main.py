import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True  # ESSENCIAL

bot = commands.Bot(
    command_prefix="hb!",
    intents=intents,
    help_command=commands.DefaultHelpCommand()
)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

async def main():
    async with bot:
        await bot.load_extension("music")
        await bot.start(os.getenv("DISCORD_TOKEN"))

asyncio.run(main())
