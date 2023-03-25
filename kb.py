from aiogram import types

def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="📹 360p", callback_data="low"),
            types.InlineKeyboardButton(text="📹 720p", callback_data="medium"),
            types.InlineKeyboardButton(text="📹 1080p", callback_data="high")
        ],
        [types.InlineKeyboardButton(text="🔊 MP3", callback_data="mus")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
