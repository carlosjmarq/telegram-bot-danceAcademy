from telegram import InlineKeyboardButton, InlineKeyboardMarkup

KEYBOARD1 = InlineKeyboardMarkup([[InlineKeyboardButton(text="1", callback_data="c1"), InlineKeyboardButton(text="?", callback_data="c111")], [InlineKeyboardButton(text="2", callback_data="c2")]])