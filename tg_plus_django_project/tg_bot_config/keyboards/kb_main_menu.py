from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Оформить заказ')],
        [
            KeyboardButton(text='Открыть каталог'),
            KeyboardButton(text='Мои заказы'),
            KeyboardButton(text='Информация о магазине')
        ],
    ], resize_keyboard=True
)