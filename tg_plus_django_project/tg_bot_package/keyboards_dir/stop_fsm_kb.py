from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

stop_fsm_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Вернуться в главное меню')],
    ], resize_keyboard=True
)