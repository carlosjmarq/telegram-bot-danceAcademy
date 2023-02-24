from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler

async def callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_chat or not update.callback_query: return
    query = update.callback_query
    
    if query.data == "c1":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Parrot says: You pressed the \"1\" button")
    elif query.data == "c2":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Parrot says: You pressed the \"2\" button")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Parrot says: I cannot handle that action, asshole")
    await context.bot.answer_callback_query(query.id, "feedback message")

callback_handler = CallbackQueryHandler(callback_query_handler)