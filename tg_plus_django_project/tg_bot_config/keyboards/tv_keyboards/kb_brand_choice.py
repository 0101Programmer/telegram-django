from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

tv_brand_choice_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Samsung', callback_data='samsung_tv')],
        [InlineKeyboardButton(text='К выбору категории товара', callback_data='to_categories')],
    ]
)

tv_brand_choice_kb_for_ordering_fsm = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Samsung', callback_data='samsung_tv')],
    ]
)