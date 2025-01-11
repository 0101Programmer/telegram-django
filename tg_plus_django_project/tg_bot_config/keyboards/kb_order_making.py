from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


product_amount_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='product_amount_1'),
            InlineKeyboardButton(text='2', callback_data='product_amount_2'),
            InlineKeyboardButton(text='3', callback_data='product_amount_3'),
            InlineKeyboardButton(text='4', callback_data='product_amount_4'),
            InlineKeyboardButton(text='5', callback_data='product_amount_5'),
        ],
        [
            InlineKeyboardButton(text='6', callback_data='product_amount_6'),
            InlineKeyboardButton(text='7', callback_data='product_amount_7'),
            InlineKeyboardButton(text='8', callback_data='product_amount_8'),
            InlineKeyboardButton(text='9', callback_data='product_amount_9'),
            InlineKeyboardButton(text='10', callback_data='product_amount_10'),
        ],
    ]
)

confirm_or_abort_order_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Вернуться в главное меню')],
        [KeyboardButton(text='Оплатить заказ')],
    ], resize_keyboard=True
)