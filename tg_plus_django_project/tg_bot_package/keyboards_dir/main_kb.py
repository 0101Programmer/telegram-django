from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Информация о магазине')],
        [
            KeyboardButton(text='Выбор категории товара'),
            KeyboardButton(text='Мои заказы')
        ],
    ], resize_keyboard=True
)