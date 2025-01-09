from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

fsm_stop_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Вернуться в главное меню')],
    ], resize_keyboard=True
)