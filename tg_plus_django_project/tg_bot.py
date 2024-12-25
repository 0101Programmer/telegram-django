import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from config import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_API)
dp = Dispatcher(bot, storage=MemoryStorage())

# block
# end block

# block клавиатуры

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
            KeyboardButton(text='У меня уже есть личный кабинет')
        ],
        [KeyboardButton(text='На главную')],
    ], resize_keyboard=True
)

new_client_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Зарегистрироваться на сайте', url='http://127.0.0.1:8000/')],
        [InlineKeyboardButton(text='Зарегистрироваться здесь', callback_data='new_client_registration')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_my_orders_kb')],
    ]
)

successful_reg_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='В личный кабинет', url='http://127.0.0.1:8000/')],
        [InlineKeyboardButton(text='В главное меню', callback_data='back_to_home')],
    ]
)

old_client_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Войти в личный кабинет на сайте', url='http://127.0.0.1:8000/')],
        [InlineKeyboardButton(text='Войти в личный кабинет здесь', callback_data='old_client_login')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_my_orders_kb')],
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


# end block

class UserReg(StatesGroup):
    email = State()
    password = State()
    repeat_password = State()
    phone_number = State()
    name = State()
    date_of_birth = State()

class UserLog(StatesGroup):
    email = State()
    password = State()

@dp.message_handler(commands=['start'])
async def start_command(message):
    await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_kb)


@dp.message_handler(text='На главную')
async def back_to_home(message):
    await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_kb)


@dp.callback_query_handler(text='back_to_home')
async def back_to_home(call):
    await call.message.answer(f'Добро пожаловать в "Best Price Hardware Store"!', reply_markup=main_kb)
    await call.answer()


# block инфо

@dp.message_handler(text='Информация о магазине')
async def info(message):
    await message.answer('Что вас интересует?', reply_markup=info_kb)


@dp.callback_query_handler(text='address')
async def info_address(call):
    await call.message.answer('Мы располагаемся по адресу...')
    await call.answer()


# end block

# block выбор категории товара

@dp.message_handler(text='Выбор категории товара')
async def prod_cat_choice(message):
    await message.answer('Что вас интересует?', reply_markup=prod_cat_choice_kb)


# end block

# block телевизоры

@dp.callback_query_handler(text='tv')
async def available_tv_models(call):
    await call.message.answer('У нас есть следующие модели...', reply_markup=tv_models_choice_kb)
    await call.answer()


@dp.callback_query_handler(text='samsung')
async def buy_func(call):
    with open('static/tg_bot_media/tv_models/samsung_tv_01.png', 'rb') as img:
        await call.message.answer_photo(img, 'Хороший тв', reply_markup=buy_tv_kb)
        await call.answer()


@dp.callback_query_handler(text='back_to_tv_models_choice')
async def go_back_func(call):
    await call.message.answer('У нас есть следующие модели...', reply_markup=tv_models_choice_kb)
    await call.answer()


# end block

# block мои заказы

@dp.message_handler(text='Мои заказы')
async def reg_auth_choice(message):
    conn = psycopg2.connect(user="postgres", password=db_password, host="localhost", port="5432", database=db_name)
    with conn.cursor() as curs:
        curs.execute('''Select tg_username from tg_plus_django_app_user where tg_username=%s and is_active=%s''',
                     (message.from_user.username, True))
        is_authed = curs.fetchone()
    conn.close()
    if is_authed:
        await message.answer('Похоже, что вы уже авторизованы', reply_markup=successful_log_kb)
    else:
        await message.answer('Выберите подходящий вариант', reply_markup=my_orders_kb)


@dp.message_handler(text='Я новый клиент')
async def reg_choice(message):
    conn = psycopg2.connect(user="postgres", password=db_password, host="localhost", port="5432", database=db_name)
    with conn.cursor() as curs:
        curs.execute('''Select tg_username from tg_plus_django_app_user where tg_username=%s''', (message.from_user.username,))
        is_registered = curs.fetchone()
        curs.execute('''Select tg_username from tg_plus_django_app_user where tg_username=%s and is_active=%s''',
                     (message.from_user.username, True))
        is_authed = curs.fetchone()
    conn.close()
    if is_authed:
        await message.answer('Похоже, что вы уже авторизованы', reply_markup=successful_log_kb)
    elif is_registered:
        await message.answer('Похоже, что вы уже регистрировались у нас,\nхотите войти в личный кабинет?', reply_markup=old_client_kb)
    else:
        await message.answer('Желаете пройти короткую регистрацию?', reply_markup=new_client_kb)


@dp.message_handler(text='У меня уже есть личный кабинет')
async def auth_choice(message):
    conn = psycopg2.connect(user="postgres", password=db_password, host="localhost", port="5432", database=db_name)
    with conn.cursor() as curs:
        curs.execute('''Select tg_username from tg_plus_django_app_user where tg_username=%s and is_active=%s''',
                     (message.from_user.username, True))
        is_authed = curs.fetchone()
    conn.close()
    if is_authed:
        await message.answer('Похоже, что вы уже авторизованы', reply_markup=successful_log_kb)
    else:
        await message.answer('Хотите войти в личный кабинет?', reply_markup=old_client_kb)


@dp.callback_query_handler(text='back_to_my_orders_kb')
async def go_back_func(call):
    await call.message.answer('Выберите подходящий вариант', reply_markup=my_orders_kb)
    await call.answer()


# end block


# block регистрация

@dp.callback_query_handler(text='new_client_registration')
async def start_reg(call):
    await call.message.answer('Пожалуйста, укажите email в формате example@mail.ru')
    await call.answer()
    await UserReg.email.set()


@dp.message_handler(state=UserReg.email)
async def fsm_handler(message, state):
    if message.text == 'К главному меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_kb)

    else:
        await state.update_data(user_email=message.text)
        data = await state.get_data()
        conn = psycopg2.connect(user="postgres", password=db_password, host="localhost", port="5432",
                                database=db_name)
        with conn.cursor() as curs:
            curs.execute('''Select email from tg_plus_django_app_user where email=%s''', (data['user_email'],))
            is_existed_email = curs.fetchone()
        conn.close()
        if not check_email(data['user_email']):
            await message.answer(f"Некорректный email", reply_markup=stop_fsm_kb)
        elif is_existed_email:
            await message.answer(f"Пользователь с таким email уже существует", reply_markup=stop_fsm_kb)
        else:
            await message.answer(f"Пожалуйста, придумайте надёжный пароль.\nТребования: не менее восьми символов, наличие спецсимволов, а также больших и строчных букв.\n(Пример: -Secr3t.)")
            await UserReg.password.set()


@dp.message_handler(state=UserReg.password)
async def fsm_handler(message, state):
    if message.text == 'К главному меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_kb)

    else:
        await state.update_data(user_password=message.text)
        data = await state.get_data()
        if not password_validate(data['user_password']):
            await message.answer(f"Пароль не соответствует требованиям", reply_markup=stop_fsm_kb)
        elif str(data['user_password']) == '-Secr3t.':
            await message.answer(f"Пожалуйста, не используйте пароль из примера", reply_markup=stop_fsm_kb)
        else:
            await message.answer(f"Пожалуйста, повторите пароль")
            await UserReg.repeat_password.set()


@dp.message_handler(state=UserReg.repeat_password)
async def fsm_handler(message, state):
    if message.text == 'К главному меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_kb)

    else:
        await state.update_data(user_repeat_password=message.text)
        data = await state.get_data()
        if data['user_password'] != data['user_repeat_password']:
            await message.answer(f"Пароли не совпадают", reply_markup=stop_fsm_kb)

        else:
            await state.update_data(user_repeat_password=message.text)
            await message.answer(f"Введите номер телефона в международном формате\n(например, +7 999 999 99 99)")
            await UserReg.phone_number.set()


@dp.message_handler(state=UserReg.phone_number)
async def fsm_handler(message, state):
    if message.text == 'К главному меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_kb)

    else:
        await state.update_data(user_phone_number=message.text)
        data = await state.get_data()
        conn = psycopg2.connect(user="postgres", password=db_password, host="localhost", port="5432",
                                database=db_name)
        with conn.cursor() as curs:
            curs.execute('''Select phone_number from tg_plus_django_app_user where phone_number=%s''', (data['user_phone_number'],))
            is_existed_p_number = curs.fetchone()
        conn.close()

        if not check_phone_number(data['user_phone_number']):
            await message.answer(f"Некорректный телефонный номер", reply_markup=stop_fsm_kb)
        elif is_existed_p_number:
            await message.answer(f"Пользователь с таким номером уже существует", reply_markup=stop_fsm_kb)
        else:
            await message.answer('Введите своё имя')
            await UserReg.name.set()


@dp.message_handler(state=UserReg.name)
async def fsm_handler(message, state):
    if message.text == 'К главному меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_kb)

    else:
        await state.update_data(user_name=message.text)
        await message.answer('Введите дату рождения в формате ГГГГ-ММ-ДД')
        await UserReg.date_of_birth.set()


@dp.message_handler(state=UserReg.date_of_birth)
async def fsm_handler(message, state):
    if message.text == 'К главному меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_kb)

    else:
        await state.update_data(user_date_of_birth=message.text)
        data = await state.get_data()
        if not date_of_birth_validate(data['user_date_of_birth']):
            await message.answer(f"Некорректная дата, пожалуйста, введите дату в формате:\nГГГГ-ММ-ДД",
                                 reply_markup=stop_fsm_kb)
        elif not is_adult(data['user_date_of_birth']):
            await message.answer(f"Извините, но регистрация у нас возможна только с 18 лет",
                                 reply_markup=stop_fsm_kb)
        else:

            conn = psycopg2.connect(user="postgres", password=db_password, host="localhost", port="5432",
                                    database=db_name)
            with conn.cursor() as curs:
                curs.execute('''Insert into tg_plus_django_app_user (name, email, password, tg_username, phone_number, date_of_birth, created_at, updated_at, is_active) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                             (data['user_name'],
                              data['user_email'],
                              data['user_password'],
                              message.from_user.username,
                              data['user_phone_number'],
                              data['user_date_of_birth'],
                              datetime.datetime.now().astimezone().strftime("%Y-%m-%d | %H:%M:%S %z | %Z"),
                              datetime.datetime.now().astimezone().strftime("%Y-%m-%d | %H:%M:%S %z | %Z"),
                              True,
                              ))
                conn.commit()
            conn.close()

            await message.answer('Спасибо за регистрацию!', reply_markup=successful_reg_kb)
            await state.finish()


# end block


# block логин

@dp.callback_query_handler(text='old_client_login')
async def start_log(call):
    await call.message.answer('Пожалуйста, укажите email в формате example@mail.ru')
    await call.answer()
    await UserLog.email.set()


@dp.message_handler(state=UserLog.email)
async def fsm_handler(message, state):
    if message.text == 'К главному меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_kb)

    else:
        await state.update_data(user_email=message.text)
        data = await state.get_data()
        conn = psycopg2.connect(user="postgres", password=db_password, host="localhost", port="5432", database=db_name)
        with conn.cursor() as curs:
            curs.execute('''Select email from tg_plus_django_app_user where email=%s''', (data['user_email'],))
            is_existed_email = curs.fetchone()
        conn.close()
        if not check_email(data['user_email']):
            await message.answer(f"Неверный email", reply_markup=stop_fsm_kb)
        elif not is_existed_email:
            await message.answer(f"Пользователя с таким email не существует", reply_markup=stop_fsm_kb)
        else:
            await message.answer(f"Пожалуйста, введите пароль")
            await UserLog.password.set()


@dp.message_handler(state=UserLog.password)
async def fsm_handler(message, state):
    if message.text == 'К главному меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_kb)

    else:
        await state.update_data(user_password=message.text)
        data = await state.get_data()
        conn = psycopg2.connect(user="postgres", password=db_password, host="localhost", port="5432", database=db_name)
        with conn.cursor() as curs:
            curs.execute('''Select password from tg_plus_django_app_user where password=%s''', (data['user_password'],))
            password_validator = curs.fetchone()
        conn.close()
        if not password_validator:
            await message.answer(f"Пароль не подходит", reply_markup=stop_fsm_kb)
        else:
            conn = psycopg2.connect(user="postgres", password=db_password, host="localhost", port="5432",
                                    database=db_name)
            with conn.cursor() as curs:
                curs.execute('''Update tg_plus_django_app_user set is_active=%s, updated_at=%s where email=%s''',
                             (True, datetime.datetime.now().astimezone().strftime("%Y-%m-%d | %H:%M:%S %z | %Z"), data['user_email'],))
                conn.commit()
            conn.close()
            await message.answer(f"Успешная авторизация", reply_markup=successful_log_kb)
            await state.finish()

# end block


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение')


executor.start_polling(dp, skip_updates=True)

# if __name__ == "__main__":
#     executor.start_polling(dp, skip_updates=True)
