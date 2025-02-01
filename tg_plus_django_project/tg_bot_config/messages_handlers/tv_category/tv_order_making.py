import asyncio
import datetime

import tzlocal

from tg_plus_django_project.config import is_valid_card_num, is_valid_card_date
from tg_plus_django_project.sqlalchemy_connection_config.existed_db_models import Product, session, User
from tg_plus_django_project.tg_bot_config.fsm.fsm_classes import MakeAnOrder
from tg_plus_django_project.tg_bot_config.keyboards.kb_fsm_stop import fsm_stop_kb_by_call, fsm_stop_kb_by_message
from tg_plus_django_project.tg_bot_config.keyboards.kb_main_menu import main_menu_kb
from tg_plus_django_project.tg_bot_config.keyboards.kb_order_making import product_amount_kb, confirm_or_abort_order_kb
from tg_plus_django_project.tg_bot_config.keyboards.kb_product_categories import product_categories_kb
from tg_plus_django_project.tg_bot_config.keyboards.tv_keyboards.kb_brand_choice import \
    tv_brand_choice_kb_for_ordering_fsm
from tg_plus_django_project.tg_bot_config.keyboards.tv_keyboards.samsung.kb_samsung_tv_models import \
    tv_samsung_model_choice_kb_for_ordering_fsm


async def start_ordering(message):
    await message.answer(
        f'Для возврата в главное меню нажмите кнопку.\nПри этом все заполненные данные по заказу будут '
        f'утеряны!',
        reply_markup=fsm_stop_kb_by_call)
    await asyncio.sleep(0.4)
    await message.answer(f'Пожалуйста, выберите категорию', reply_markup=product_categories_kb)
    await MakeAnOrder.category.set()


async def ordering_fsm_handler_step_1(call, state):
    if call.data == 'back_to_main_menu':
        await call.message.answer(f'Добро пожаловать, {call.from_user.username}!', reply_markup=main_menu_kb)
        await call.answer()
        await state.finish()
    elif call.data == 'tv':
        await state.update_data(order_category=call.data)
        await call.message.answer("Укажите бренд", reply_markup=tv_brand_choice_kb_for_ordering_fsm)
        await call.answer()
        await MakeAnOrder.brand.set()


async def ordering_fsm_handler_step_2(call, state):
    if call.data == 'back_to_main_menu':
        await call.message.answer(f'Добро пожаловать, {call.from_user.username}!', reply_markup=main_menu_kb)
        await call.answer()
        await state.finish()
    elif call.data == 'samsung_tv':
        await state.update_data(order_brand=call.data)
        await call.message.answer("Укажите интересующую модель",
                                  reply_markup=tv_samsung_model_choice_kb_for_ordering_fsm)
        await call.answer()
        await MakeAnOrder.name.set()


async def ordering_fsm_handler_step_3(call, state):
    if call.data == 'back_to_main_menu':
        await call.message.answer(f'Добро пожаловать, {call.from_user.username}!', reply_markup=main_menu_kb)
        await call.answer()
        await state.finish()
    else:
        await state.update_data(order_model=call.data)
        await call.message.answer("Укажите количество, которое вы хотите приобрести",
                                  reply_markup=product_amount_kb)
        await call.answer()
        await MakeAnOrder.amount.set()


async def ordering_fsm_handler_step_4(call, state):
    if call.data == 'back_to_main_menu':
        await call.message.answer(f'Добро пожаловать, {call.from_user.username}!', reply_markup=main_menu_kb)
        await call.answer()
        await state.finish()
    else:
        product_amount = ""
        for i in range(1, 11):
            if call.data == f"product_amount_{i}":
                product_amount = i
        await state.update_data(order_product_amount=product_amount)
        data = await state.get_data()
        await state.update_data(
            order_total=int(session.query(Product).filter(Product.name.contains([data['order_model']])).first().price) * int(
                data['order_product_amount']))
        user_data = session.query(User).filter(
            User.tg_username == call.from_user.username).one_or_none()
        available_cards = {}
        if user_data.orders:
            for k, v in user_data.orders.items():
                if v["card_data"] is not None:
                    if is_valid_card_date(v["card_data"]["card_date"]):
                        available_cards[v["card_data"]["card_number"]] = {"card_date": v["card_data"]["card_date"],
                                                                          "card_cvc": v["card_data"]["card_cvc"]}
        await state.update_data(order_available_cards=available_cards)

        data = await state.get_data()
        await call.message.answer(
            f"Итоговая стоимость вашего заказа:\n{data['order_total']}")
        await asyncio.sleep(0.5)
        if user_data.orders:
            await call.message.answer(f"Вы можете оплатить заказ сохранённой картой:",
                                      reply_markup=fsm_stop_kb_by_message)
            for k, v in data['order_available_cards'].items():
                backslash_for_f_string = "\\"
                await call.message.answer(f'Номер: `{k}`\n\| Срок действия: \|\n||{v["card_date"].replace("-", f"{backslash_for_f_string}-")}||\n\| Код безопасности: \|\n||{v["card_cvc"]}||', parse_mode='MarkdownV2')
            await call.message.answer("Укажите номер новой или сохранённой банковской карты для оплаты",
                                      reply_markup=fsm_stop_kb_by_message)
        else:
            await call.message.answer("Укажите номер банковской карты для оплаты",
                                      reply_markup=fsm_stop_kb_by_message)
        await call.answer()
        await MakeAnOrder.card_number.set()


async def ordering_fsm_handler_step_5(message, state):
    if message.text == 'Вернуться в главное меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_menu_kb)

    else:
        if not is_valid_card_num(message.text):
            await message.answer("Укажите номер банковской карты одной строкой, номер должен содержать только цифры, "
                                 "длина от 13 до 19 цифр", reply_markup=fsm_stop_kb_by_message)
        else:
            await state.update_data(order_card_number=message.text)
            await message.answer('Введите срок действия карты в формате ГГГГ-ММ')
            await MakeAnOrder.card_date.set()


async def ordering_fsm_handler_step_6(message, state):
    if message.text == 'Вернуться в главное меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_menu_kb)
    else:
        if not is_valid_card_date(message.text):
            await message.answer("Введите срок активной карты в формате ГГГГ-ММ", reply_markup=fsm_stop_kb_by_message)
        else:
            await state.update_data(order_card_date=message.text)
            await message.answer('Введите трёхзначный код безопасности')
            await MakeAnOrder.card_cvc.set()


async def ordering_fsm_handler_step_7(message, state):
    if message.text == 'Вернуться в главное меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_menu_kb)
    else:
        if len(message.text) != 3 or not message.text.isnumeric():
            await message.answer('Пожалуйста, введите корректный трёхзначный код безопасности')
        else:
            await state.update_data(order_card_cvc=message.text)
            data = await state.get_data()
            if data["order_card_number"] not in data["order_available_cards"]:
                await message.answer("Желаете сохранить данные карты для будущих заказов? \(`Да`/`Нет`\)", parse_mode='MarkdownV2')
            else:
                await message.answer("Заказ оформлен", reply_markup=confirm_or_abort_order_kb)
            await MakeAnOrder.save_card_option.set()


async def ordering_fsm_handler_step_8(message, state):
    if message.text == 'Вернуться в главное меню':
        await state.finish()
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_menu_kb)
    else:
        data = await state.get_data()
        if data["order_card_number"] in data["order_available_cards"]:
            if message.text == "Оплатить заказ":
                data = await state.get_data()
                await state.update_data(
                    order_card_data={"card_number": data['order_card_number'], "card_date": data['order_card_date'],
                                     "card_cvc": data['order_card_cvc']})
                data = await state.get_data()
                user_data = session.query(User).filter(
                    User.tg_username == message.from_user.username).one_or_none()
                now = datetime.datetime.now(tzlocal.get_localzone())
                user_data.orders = (user_data.orders | {
                    int(max(user_data.orders, key=int)) + 1:
                        {"product_name": data["order_model"],
                         "product_amount": data["order_product_amount"],
                         "product_total": data["order_total"],
                         "status": [
                                 "confirmed",
                                 "Оплачен"
                             ],
                         "updated_at": now.strftime("%Y-%m-%d %H:%M:%S %Z%z"),
                         "card_data": data["order_card_data"]}
                })
                user_data.updated_at = datetime.datetime.now()
                session.add(user_data)
                session.commit()
                await message.answer('Спасибо за ваш заказ', reply_markup=main_menu_kb)
                await state.finish()
        else:
            if message.text != 'Да' and message.text != 'Нет':
                await message.answer("Пожалуйста, укажите ответ в формате '`Да`' или '`Нет`'", parse_mode='MarkdownV2')
            elif message.text == 'Да':
                data = await state.get_data()
                await state.update_data(
                    order_card_data={"card_number": data['order_card_number'], "card_date": data['order_card_date'],
                                     "card_cvc": data['order_card_cvc']})
                data = await state.get_data()
                user_data = session.query(User).filter(
                    User.tg_username == message.from_user.username).one_or_none()
                if not user_data.orders:
                    now = datetime.datetime.now(tzlocal.get_localzone())
                    user_data.orders = ({
                        1:
                            {"product_name": data["order_model"],
                             "product_amount": data["order_product_amount"],
                             "product_total": data["order_total"],
                             "status": [
                                 "confirmed",
                                 "Оплачен"
                             ],
                             "updated_at": now.strftime("%Y-%m-%d %H:%M:%S %Z%z"),
                             "card_data": data["order_card_data"]}
                    })
                    user_data.updated_at = datetime.datetime.now()
                    session.add(user_data)
                    session.commit()
                else:
                    now = datetime.datetime.now(tzlocal.get_localzone())
                    user_data.orders = (user_data.orders | {
                        int(max(user_data.orders, key=int)) + 1:
                            {"product_name": data["order_model"],
                             "product_amount": data["order_product_amount"],
                             "product_total": data["order_total"],
                             "status": [
                                 "confirmed",
                                 "Оплачен"
                             ],
                             "updated_at": now.strftime("%Y-%m-%d %H:%M:%S %Z%z"),
                             "card_data": data["order_card_data"]}
                    })
                    user_data.updated_at = datetime.datetime.now()
                    session.add(user_data)
                    session.commit()
                await message.answer('Спасибо за ваш заказ', reply_markup=main_menu_kb)
                await state.finish()

            elif message.text == 'Нет':
                data = await state.get_data()
                user_data = session.query(User).filter(
                    User.tg_username == message.from_user.username).one_or_none()
                if not user_data.orders:
                    now = datetime.datetime.now(tzlocal.get_localzone())
                    user_data.orders = ({
                        1:
                            {"product_name": data["order_model"],
                             "product_amount": data["order_product_amount"],
                             "product_total": data["order_total"],
                             "status": [
                                 "confirmed",
                                 "Оплачен"
                             ],
                             "updated_at": now.strftime("%Y-%m-%d %H:%M:%S %Z%z"),
                             "card_data": None}
                    })
                    user_data.updated_at = datetime.datetime.now()
                    session.add(user_data)
                    session.commit()
                else:
                    now = datetime.datetime.now(tzlocal.get_localzone())
                    user_data.orders = (user_data.orders | {
                        int(max(user_data.orders, key=int)) + 1:
                            {"product_name": data["order_model"],
                             "product_amount": data["order_product_amount"],
                             "product_total": data["order_total"],
                             "status": [
                                 "confirmed",
                                 "Оплачен"
                             ],
                             "updated_at": now.strftime("%Y-%m-%d %H:%M:%S %Z%z"),
                             "card_data": None}
                    })
                    user_data.updated_at = datetime.datetime.now()
                    session.add(user_data)
                    session.commit()
                await message.answer('Спасибо за ваш заказ', reply_markup=main_menu_kb)
                await state.finish()
