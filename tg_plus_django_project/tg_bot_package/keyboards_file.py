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

info_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Наш адрес', callback_data='address')],
    ]
)

prod_cat_choice_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Телевизоры', callback_data='tv')],
    ]
)

my_orders_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Я новый клиент'),
        ],
        [KeyboardButton(text='На главную')],
    ], resize_keyboard=True
)

new_client_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Зарегистрироваться на сайте', url='http://127.0.0.1:8000/')],
        [InlineKeyboardButton(text='Зарегистрироваться здесь', callback_data='new_client_registration')],
        [InlineKeyboardButton(text='В главное меню', callback_data='back_to_home')],
    ]
)

successful_reg_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='В личный кабинет', url='http://127.0.0.1:8000/')],
        [InlineKeyboardButton(text='В главное меню', callback_data='back_to_home')],
    ]
)

successful_log_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='В личный кабинет', url='http://127.0.0.1:8000/')],
        [InlineKeyboardButton(text='В главное меню', callback_data='back_to_home')],
    ]
)

stop_fsm_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='К главному меню')],
    ], resize_keyboard=True
)

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