import discord
from discord.ext import commands
import os
from datetime import datetime

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# =========================
# ⏱️ SIMPLE TIMER
# =========================
HARD_INTERVAL_1 = 14 * 60
HARD_INTERVAL_2 = 20 * 60

HARD_START_1 = datetime(2026, 5, 20, 0, 0)
HARD_START_2 = datetime(2026, 5, 20, 0, 5)

def get_remaining(start, interval):
    now = datetime.now()
    passed = (now - start).total_seconds() % interval
    remaining = interval - passed

    m = int(remaining // 60)
    s = int(remaining % 60)

    return f"{m}m {s}s"

# =========================
# 🎮 COMMAND
# =========================
@bot.command()
async def hard(ctx):
    t1 = get_remaining(HARD_START_1, HARD_INTERVAL_1)
    t2 = get_remaining(HARD_START_2, HARD_INTERVAL_2)

    await ctx.send(
        f"""🦠Hard Virus 1:  {t1}
🦠Hard Virus 2:  {t2}"""
    )

# =========================
# 🚀 RUN
# =========================
bot.run(TOKEN)
