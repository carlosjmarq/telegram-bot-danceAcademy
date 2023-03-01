from typing import Dict, List, Tuple

from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def create_inline_keyboard(options: List[Dict[str, str]]) -> InlineKeyboardMarkup:
	buttons = []
	for option in options:
		buttons.append([InlineKeyboardButton(text=option["text"], callback_data=option["callback_data"])])
	return InlineKeyboardMarkup(buttons)