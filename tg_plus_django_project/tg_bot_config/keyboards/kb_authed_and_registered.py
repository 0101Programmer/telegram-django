from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

authed_and_registered_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Войти в личный кабинет на сайте', url='http://127.0.0.1:8000/')],
        [InlineKeyboardButton(text='Посмотреть каталог и оформить заказ', callback_data='to_catalog')],
        [InlineKeyboardButton(text='В главное меню', callback_data='back_to_main_menu')],
    ]
)