import discord
from discord.ext import commands
import os
from datetime import datetime

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

HARD_INTERVAL = 14 * 60
HARD_START = datetime(2026, 5, 20, 0, 0)

NM_INTERVAL = 4 * 60 * 60
NM_START = datetime(2026, 5, 20, 2, 0)

def get_remaining(start, interval):
    now = datetime.now()
    passed = (now - start).total_seconds() % interval
    remaining = interval - passed

    h = int(remaining // 3600)
    m = int((remaining % 3600) // 60)
    s = int(remaining % 60)

    return f"{h}h {m}m {s}s"

@bot.event
async def on_ready():
    print(f"ONLINE: {bot.user}")

@bot.command()
async def hard(ctx):
    await ctx.send(f"🦠 Next Hard Virus in: **{get_remaining(HARD_START, HARD_INTERVAL)}**")

@bot.command()
async def nm(ctx):
    await ctx.send(f"☠️ Next Nightmare Virus in: **{get_remaining(NM_START, NM_INTERVAL)}**")

bot.run(TOKEN)
