import subprocess
from telegram.ext import Updater, CommandHandler

TOKEN = "7668581329:AAH4cEIQztlM4Cvu85JRtonqVkYsknneku8"

def scan(update, context):
    if not context.args:
        update.message.reply_text("Usage: /scan example.com")
        return

    target = context.args[0]
    cmd = f"./httpx -u {target} -title -sc"
    result = subprocess.getoutput(cmd)

    update.message.reply_text(result[:3500])

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("scan", scan))
updater.start_polling()
updater.idle()
