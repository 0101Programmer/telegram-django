import tg_plus_django_project.tg_bot_package.keyboards_file as kb_file
from tg_plus_django_project.tg_bot_package.fsm_classes import *
from tg_plus_django_project.config import *
from tg_plus_django_project.sqlalchemy_connection_config.existed_db_models import User, session


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
        is_existed_email = session.query(User).filter(User.email == data['user_email']).one_or_none()
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
        is_existed_p_number = session.query(User).filter(User.phone_number == data['user_phone_number']).one_or_none()
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
            new_user = User(
                name=data['user_name'],
                email=data['user_email'],
                password=data['user_password'],
                tg_username=message.from_user.username,
                phone_number=check_phone_number(data['user_phone_number']),
                date_of_birth=data['user_date_of_birth'],
                orders=None,
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
            )
            session.add(new_user)
            session.commit()
            await message.answer('Спасибо за регистрацию!', reply_markup=kb_file.successful_reg_kb)
            await state.finish()