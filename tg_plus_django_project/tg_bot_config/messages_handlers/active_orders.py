import pandas as pd
from aiogram.types import ParseMode
from tabulate import tabulate

from tg_plus_django_project.sqlalchemy_connection_config.existed_db_models import User, session
from tg_plus_django_project.tg_bot_config.keyboards.kb_authed_and_registered import authed_and_registered_kb
from tg_plus_django_project.tg_bot_config.keyboards.kb_main_menu import main_menu_kb
from tg_plus_django_project.tg_bot_config.keyboards.kb_not_authed_and_registered import not_authed_and_registered_kb


async def active_orders_data(message):
    is_registered = session.query(User).filter(User.tg_username == message.from_user.username).one_or_none()
    if is_registered:
        if is_registered.orders is not None:
            orders_data_df = pd.DataFrame(
                columns=['Заказ №', 'Статус', 'Товар', 'Кол-во (ед.)', 'Итого, руб.',
                         'Дата обновления', ])
            loc_idx = 0
            for k, v in is_registered.orders.items():
                new_row = [k,
                           v["status"][1],
                           v["product_name"],
                           v["product_amount"],
                           v["product_total"],
                           v["updated_at"][:16]]
                orders_data_df.loc[loc_idx] = new_row
                loc_idx += 1
            tabulated_orders_data_df = tabulate(orders_data_df, headers='keys', tablefmt='psql')
            await message.answer(f'<pre>{tabulated_orders_data_df}</pre>', reply_markup=main_menu_kb,
                                 parse_mode=ParseMode.HTML)
        else:
            await message.answer('У вас пока нет ни одного заказа', reply_markup=authed_and_registered_kb)
    else:
        await message.answer('К сожалению, не смогли найти вас в нашей базе данных', reply_markup=not_authed_and_registered_kb)