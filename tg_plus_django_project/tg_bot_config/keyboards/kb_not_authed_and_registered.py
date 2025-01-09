from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

not_authed_and_registered_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Зарегистрироваться'),
        ],
        [KeyboardButton(text='На главную')],
    ], resize_keyboard=True
)