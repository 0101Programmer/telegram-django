import tg_plus_django_project.tg_bot_package.keyboards_file as kb_file
from tg_plus_django_project.tg_bot_package.fsm_classes import *
from tg_plus_django_project.config import *



async def start_reg(call):
    await call.message.answer('Пожалуйста, укажите email в формате example@mail.ru')
    await call.answer()
    await UserReg.email.set()


async def reg_fsm_handler_step_1(message, state):
    if message.text == 'К главному меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=kb_file.main_kb)

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
            await message.answer(f"Некорректный email", reply_markup=kb_file.stop_fsm_kb)
        elif is_existed_email:
            await message.answer(f"Пользователь с таким email уже существует", reply_markup=kb_file.stop_fsm_kb)
        else:
            await message.answer(f"Пожалуйста, придумайте надёжный пароль.\nТребования: не менее восьми символов, наличие спецсимволов, а также больших и строчных букв.\n(Пример: -Secr3t.)")
            await UserReg.password.set()


async def reg_fsm_handler_step_2(message, state):
    if message.text == 'К главному меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=kb_file.main_kb)

    else:
        await state.update_data(user_password=message.text)
        data = await state.get_data()
        if not password_validate(data['user_password']):
            await message.answer(f"Пароль не соответствует требованиям", reply_markup=kb_file.stop_fsm_kb)
        elif str(data['user_password']) == '-Secr3t.':
            await message.answer(f"Пожалуйста, не используйте пароль из примера", reply_markup=kb_file.stop_fsm_kb)
        else:
            await message.answer(f"Пожалуйста, повторите пароль")
            await UserReg.repeat_password.set()


async def reg_fsm_handler_step_3(message, state):
    if message.text == 'К главному меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=kb_file.main_kb)

    else:
        await state.update_data(user_repeat_password=message.text)
        data = await state.get_data()
        if data['user_password'] != data['user_repeat_password']:
            await message.answer(f"Пароли не совпадают", reply_markup=kb_file.stop_fsm_kb)

        else:
            await state.update_data(user_repeat_password=message.text)
            await message.answer(f"Введите номер телефона в международном формате\n(например, +7 999 999 99 99)")
            await UserReg.phone_number.set()


async def reg_fsm_handler_step_4(message, state):
    if message.text == 'К главному меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=kb_file.main_kb)

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
            await message.answer(f"Некорректный телефонный номер", reply_markup=kb_file.stop_fsm_kb)
        elif is_existed_p_number:
            await message.answer(f"Пользователь с таким номером уже существует", reply_markup=kb_file.stop_fsm_kb)
        else:
            await message.answer('Введите своё имя')
            await UserReg.name.set()


async def reg_fsm_handler_step_5(message, state):
    if message.text == 'К главному меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=kb_file.main_kb)

    else:
        await state.update_data(user_name=message.text)
        await message.answer('Введите дату рождения в формате ГГГГ-ММ-ДД')
        await UserReg.date_of_birth.set()


async def reg_fsm_handler_step_6(message, state):
    if message.text == 'К главному меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=kb_file.main_kb)

    else:
        await state.update_data(user_date_of_birth=message.text)
        data = await state.get_data()
        if not date_of_birth_validate(data['user_date_of_birth']):
            await message.answer(f"Некорректная дата, пожалуйста, введите дату в формате:\nГГГГ-ММ-ДД",
                                 reply_markup=kb_file.stop_fsm_kb)
        elif not is_adult(data['user_date_of_birth']):
            await message.answer(f"Извините, но регистрация у нас возможна только с 18 лет",
                                 reply_markup=kb_file.stop_fsm_kb)
        else:

            conn = psycopg2.connect(user="postgres", password=db_password, host="localhost", port="5432",
                                    database=db_name)
            with conn.cursor() as curs:
                curs.execute('''Insert into tg_plus_django_app_user (name, email, password, tg_username, phone_number, date_of_birth, created_at, updated_at) values (%s, %s, %s, %s, %s, %s, %s, %s)''',
                             (data['user_name'],
                              data['user_email'],
                              data['user_password'],
                              message.from_user.username,
                              data['user_phone_number'],
                              data['user_date_of_birth'],
                              datetime.datetime.now().astimezone().strftime("%Y-%m-%d | %H:%M:%S %z | %Z"),
                              datetime.datetime.now().astimezone().strftime("%Y-%m-%d | %H:%M:%S %z | %Z"),
                              ))
                conn.commit()
            conn.close()

            await message.answer('Спасибо за регистрацию!', reply_markup=kb_file.successful_reg_kb)
            await state.finish()