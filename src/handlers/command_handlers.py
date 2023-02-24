from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from constants.commands import COMMANDS
from constants.inline_keyboards import KEYBOARD1, FIRSTKEYBOARD
from constants.text import WELCOMETEXT
from utils.string_functions import capitalize

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_chat: return
    await context.bot.set_my_commands(COMMANDS)
    await context.bot.send_message(chat_id=update.effective_chat.id, text= WELCOMETEXT, reply_markup= FIRSTKEYBOARD)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if (not context.args or not update.effective_chat): return
    text_caps = capitalize(context.args)
    # text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def show_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_chat or not update.message: return
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Parrot says: Choice one option", 
        reply_markup=KEYBOARD1
    )


start_handler = CommandHandler('start', start)
caps_handler = CommandHandler("caps", caps)
buttons_handler = CommandHandler("buttons", show_button)