from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

successful_reg_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='В личный кабинет', url='http://127.0.0.1:8000/')],
        [InlineKeyboardButton(text='В главное меню', callback_data='back_to_home')],
    ]
)