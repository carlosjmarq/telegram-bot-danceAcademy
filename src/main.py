import logging
import telegram
import os
from dotenv import load_dotenv 
from telegram.ext import ApplicationBuilder
from handlers.callback_handlers import callback_handler
from handlers.command_handlers import start_handler, caps_handler, buttons_handler
from handlers.message_handlers import echo_handler
from db.config import start_db

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
load_dotenv()

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("TELEGRAMTOKEN")).build()
    start_db()

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(buttons_handler)
    application.add_handler(callback_handler)

    application.run_polling()