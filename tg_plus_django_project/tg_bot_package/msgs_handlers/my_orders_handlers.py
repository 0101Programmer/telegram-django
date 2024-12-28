import tg_plus_django_project.tg_bot_package.keyboards_file as kb_file
from tg_plus_django_project.config import *


async def reg_auth_choice(message):
    conn = psycopg2.connect(user="postgres", password=db_password, host="localhost", port="5432", database=db_name)
    with conn.cursor() as curs:
        curs.execute('''Select tg_username from tg_plus_django_app_user where tg_username=%s''',
                     (message.from_user.username,))
        is_registered = curs.fetchone()
    conn.close()
    if is_registered:
        await message.answer('Со своими заказами вы можете ознакомиться тут', reply_markup=kb_file.successful_log_kb)
    else:
        await message.answer('К сожалению, не смогли найти вас в нашей базе данных', reply_markup=kb_file.my_orders_kb)


async def reg_choice(message):
    await message.answer('Желаете пройти короткую регистрацию?', reply_markup=kb_file.new_client_kb)

async def go_back_to_my_orders_func(call):
    conn = psycopg2.connect(user="postgres", password=db_password, host="localhost", port="5432", database=db_name)
    with conn.cursor() as curs:
        curs.execute('''Select tg_username from tg_plus_django_app_user where tg_username=%s''',
                     (call.from_user.username,))
        is_registered = curs.fetchone()
    conn.close()
    if is_registered:
        await call.message.answer(reply_markup=kb_file.successful_log_kb)
        await call.answer()
    else:

        await call.message.answer('К сожалению, не смогли найти вас в нашей базе данных', reply_markup=kb_file.my_orders_kb)
        await call.answer()