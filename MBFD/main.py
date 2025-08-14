import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Crear el bot con todos los intents
client = commands.Bot(command_prefix="?", intents=discord.Intents.all())

async def main():
    async with client:
        # Cargar el cog de música
        await client.load_extension("music")
        # Iniciar el bot
        await client.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
