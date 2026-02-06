import os
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")  # Render env variable me token dalna

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Httpx Bot Ready\nUse: /scan example.com")

# /scan command
async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /scan example.com")
        return

    target = context.args[0]

    try:
        cmd = f"httpx -u {target} -title -sc"
        result = subprocess.check_output(cmd, shell=True, text=True)
    except Exception as e:
        result = str(e)

    if not result:
        result = "No result."

    await update.message.reply_text(f"```\n{result}\n```", parse_mode="Markdown")

# main bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("scan", scan))

print("Bot running...")
app.run_polling()
