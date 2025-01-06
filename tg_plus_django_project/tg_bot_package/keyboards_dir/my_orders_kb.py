from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

my_orders_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Я новый клиент'),
        ],
        [KeyboardButton(text='На главную')],
    ], resize_keyboard=True
)
