from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

fsm_stop_kb_by_message = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Вернуться в главное меню')],
    ], resize_keyboard=True
)

fsm_stop_kb_by_call = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='В главное меню', callback_data='back_to_main_menu')],
    ]
)