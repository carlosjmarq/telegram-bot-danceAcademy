from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_chat or not update.message: return
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Parrot says: {}".format(update.message.text))

echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)