from aiogram import types

def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="📹 144p", callback_data="easy"),
            types.InlineKeyboardButton(text="📹 360p", callback_data="low"),
            types.InlineKeyboardButton(text="📹 720p", callback_data="medium")
        ],
        [types.InlineKeyboardButton(text="🔊 MP3", callback_data="mus")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
