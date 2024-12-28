import tg_plus_django_project.tg_bot_package.keyboards_file as kb_file
from tg_plus_django_project.config import *
from tabulate import tabulate
import pandas as pd
from aiogram.types import ParseMode


async def reg_auth_choice(message):
    conn = psycopg2.connect(user="postgres", password=db_password, host="localhost", port="5432", database=db_name)
    with conn.cursor() as curs:
        curs.execute('''Select * from tg_plus_django_app_user where tg_username=%s''',
                     (message.from_user.username,))
        is_registered = curs.fetchone()
    conn.close()
    if is_registered:
        if is_registered[7] is not None:

            orders_data_df = pd.DataFrame(
                columns=['Номер заказа', 'Статус', 'Товар', 'Цена (за шт.)', 'Кол-во (шт.)', 'Итого, руб.',
                         'Дата обновления', ])
            loc_idx = 0

            for k, v in is_registered[7].items():

                if v["status"] == 'ordered':
                    status_name_for_client = 'Оформлен'
                elif v["status"] == 'canceled':
                    status_name_for_client = 'Отменён'
                else:
                    status_name_for_client = 'Оплачен, ожидается доставка'

                new_row = [k,
                           status_name_for_client,
                           f'{v["model_name_for_client"]}',
                           f'{v["product_price"]}',
                           f'{v["product_amount"]}',
                           f'{v["total"]}',
                           f'{v["updated_at"][:22]}', ]
                orders_data_df.loc[loc_idx] = new_row
                loc_idx += 1

            tabulated_orders_data_df = tabulate(orders_data_df, headers='keys', tablefmt='psql')
            await message.answer(f'<pre>{tabulated_orders_data_df}</pre>', reply_markup=kb_file.main_kb,
                                 parse_mode=ParseMode.HTML)
        else:
            await message.answer('У вас пока нет ни одного заказа', reply_markup=kb_file.successful_log_kb)
    else:
        await message.answer('К сожалению, не смогли найти вас в нашей базе данных', reply_markup=kb_file.my_orders_kb)


async def reg_choice(message):
    await message.answer('Желаете пройти короткую регистрацию?', reply_markup=kb_file.new_client_kb)
