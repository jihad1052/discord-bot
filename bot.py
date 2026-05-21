import discord
from discord.ext import commands
import os
from datetime import datetime, timezone

# =========================
# 🔐 TOKEN (Render ENV)
# =========================
TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    raise Exception("DISCORD_TOKEN not found in environment variables")

# =========================
# 🤖 BOT SETUP
# =========================
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# =========================
# ⏱️ TIME SYSTEM (UTC SAFE)
# =========================
HARD_INTERVAL = 14 * 60
NM_INTERVAL = 4 * 60 * 60

HARD_START = datetime(2026, 5, 20, 0, 0, tzinfo=timezone.utc)
NM_START = datetime(2026, 5, 20, 2, 0, tzinfo=timezone.utc)

def get_remaining(start, interval):
    now = datetime.now(timezone.utc)
    passed = (now - start).total_seconds() % interval
    remaining = interval - passed

    h = int(remaining // 3600)
    m = int((remaining % 3600) // 60)
    s = int(remaining % 60)

    return f"{h}h {m}m {s}s"

# =========================
# 📡 EVENTS
# =========================
@bot.event
async def on_ready():
    print(f"ONLINE: {bot.user}")

# =========================
# 🎮 COMMANDS
# =========================
@bot.command()
async def hard(ctx):
    await ctx.send(f"🦠 Next Hard Virus in: **{get_remaining(HARD_START, HARD_INTERVAL)}** (UTC)")

@bot.command()
async def nm(ctx):
    await ctx.send(f"☠️ Next Nightmare Virus in: **{get_remaining(NM_START, NM_INTERVAL)}** (UTC)")

# =========================
# 🚀 RUN BOT
# =========================
bot.run(TOKEN)
