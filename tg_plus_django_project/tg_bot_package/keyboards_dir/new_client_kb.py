from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

new_client_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Зарегистрироваться на сайте', url='http://127.0.0.1:8000/')],
        [InlineKeyboardButton(text='Зарегистрироваться здесь', callback_data='new_client_registration')],
        [InlineKeyboardButton(text='В главное меню', callback_data='back_to_home')],
    ]
)