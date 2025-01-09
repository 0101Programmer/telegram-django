from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

info_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Наш адрес', callback_data='address')],
        [InlineKeyboardButton(text='О нас', callback_data='about')],
        [InlineKeyboardButton(text='Перейти на сайт', url='http://127.0.0.1:8000/')],
    ]
)