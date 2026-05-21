import discord
from discord.ext import commands
import os
from datetime import datetime, timezone

TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    raise Exception("DISCORD_TOKEN not found")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# =========================
# ⏱️ TIME SYSTEM (UTC)
# =========================
HARD_INTERVAL_1 = 14 * 60
HARD_INTERVAL_2 = 20 * 60  # example second cycle (change if needed)

HARD_START_1 = datetime(2026, 5, 20, 0, 0, tzinfo=timezone.utc)
HARD_START_2 = datetime(2026, 5, 20, 1, 0, tzinfo=timezone.utc)

def get_remaining(start, interval):
    now = datetime.now(timezone.utc)
    passed = (now - start).total_seconds() % interval
    remaining = interval - passed

    h = int(remaining // 3600)
    m = int((remaining % 3600) // 60)
    s = int(remaining % 60)

    return f"{h}h {m}m {s}s"

@bot.event
async def on_ready():
    print(f"ONLINE: {bot.user}")

# =========================
# 🎮 SINGLE COMMAND SHOW 2 TIMES
# =========================
@bot.command()
async def hard(ctx):
    time1 = get_remaining(HARD_START_1, HARD_INTERVAL_1)
    time2 = get_remaining(HARD_START_2, HARD_INTERVAL_2)

    await ctx.send(
        f"""🦠 **Hard Virus System**

🔥 Hard Virus 1: **{time1}**
🔥 Hard Virus 2: **{time2}**

(UTC Time)"""
    )

# =========================
# 🚀 RUN BOT
# =========================
bot.run(TOKEN)
