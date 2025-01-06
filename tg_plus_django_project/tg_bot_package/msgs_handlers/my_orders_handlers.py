import pandas as pd
from aiogram.types import ParseMode
from tabulate import tabulate

from tg_plus_django_project.sqlalchemy_connection_config.existed_db_models import User, session
from tg_plus_django_project.tg_bot_package.keyboards_dir import main_kb, successful_reg_kb, my_orders_kb, new_client_kb


async def reg_auth_choice(message):
    is_registered = session.query(User).filter(User.tg_username == message.from_user.username).one_or_none()
    if is_registered:
        if is_registered.orders is not None:

            orders_data_df = pd.DataFrame(
                columns=['Номер заказа', 'Статус', 'Товар', 'Цена (за шт.)', 'Кол-во (шт.)', 'Итого, руб.',
                         'Дата обновления', ])
            loc_idx = 0

            for k, v in is_registered.orders.items():

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
            await message.answer(f'<pre>{tabulated_orders_data_df}</pre>', reply_markup=main_kb.main_kb,
                                 parse_mode=ParseMode.HTML)
        else:
            await message.answer('У вас пока нет ни одного заказа', reply_markup=successful_reg_kb.successful_reg_kb)
    else:
        await message.answer('К сожалению, не смогли найти вас в нашей базе данных', reply_markup=my_orders_kb.my_orders_kb)


async def reg_choice(message):
    await message.answer('Желаете пройти короткую регистрацию?', reply_markup=new_client_kb.new_client_kb)
