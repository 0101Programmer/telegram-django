from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

tv_samsung_model_choice_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='QE65Q70DAU', callback_data='QE65Q70DAU')],
        [InlineKeyboardButton(text='К выбору бренда', callback_data='tv')],
    ]
)

back_to_tv_samsung_model_choice_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='К выбору модели', callback_data='samsung_tv')],
    ]
)