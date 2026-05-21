import discord
from discord.ext import commands
import os
from datetime import datetime, timezone

# =========================
# 🔐 TOKEN
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
# ⏱️ TIME SYSTEM (UTC)
# =========================
HARD_INTERVAL_1 = 14 * 60
HARD_INTERVAL_2 = 20 * 60

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

# =========================
# 📌 ROOMS (ENV)
# =========================
HARD_ROOM_1 = os.getenv("HARD_ROOM_1")
HARD_ROOM_2 = os.getenv("HARD_ROOM_2")

# =========================
# 📡 READY EVENT
# =========================
@bot.event
async def on_ready():
    print(f"ONLINE: {bot.user}")

# =========================
# 🎮 HARD COMMAND
# =========================
@bot.command()
async def hard(ctx):
    time1 = get_remaining(HARD_START_1, HARD_INTERVAL_1)
    time2 = get_remaining(HARD_START_2, HARD_INTERVAL_2)

    msg = f"""🦠 **Hard Virus System**

🔥 Hard Virus 1: **{time1}**
🔥 Hard Virus 2: **{time2}**

(UTC Time)"""

    # send to room 1
    if HARD_ROOM_1:
        ch1 = bot.get_channel(int(HARD_ROOM_1))
        if ch1:
            await ch1.send(msg)

    # send to room 2
    if HARD_ROOM_2:
        ch2 = bot.get_channel(int(HARD_ROOM_2))
        if ch2:
            await ch2.send(msg)

    # single reply (no duplicate spam)
    await ctx.send("🟢 Hard Virus updated in both rooms")

# =========================
# 🚀 RUN BOT
# =========================
bot.run(TOKEN)
