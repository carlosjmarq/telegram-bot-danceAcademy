import logging
import telegram
from telegram.ext import ApplicationBuilder
from handlers.callback_handlers import callback_handler
from handlers.command_handlers import start_handler, caps_handler, buttons_handler
from handlers.message_handlers import echo_handler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token('910583270:AAE9qe3oTvyfM4dargWuJkr1UVplEhHNA3A').build()
    
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(buttons_handler)
    application.add_handler(callback_handler)

    application.run_polling()