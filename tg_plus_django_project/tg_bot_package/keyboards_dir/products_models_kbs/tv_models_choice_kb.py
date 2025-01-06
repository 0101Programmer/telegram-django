from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

tv_models_choice_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Самсунг', callback_data='samsung')],
        [InlineKeyboardButton(text='Ксяоми', callback_data='xiaomi')],
    ]
)

buy_tv_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Купить', url='http://127.0.0.1:8000/')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_tv_models_choice')],
    ]
)
