import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from tg_plus_django_project.config import *
from tg_plus_django_project.tg_bot_config.fsm.fsm_classes import UserReg, MakeAnOrder
from tg_plus_django_project.tg_bot_config.messages_handlers.active_orders import active_orders_data
from tg_plus_django_project.tg_bot_config.messages_handlers.all_messages import all_messages
from tg_plus_django_project.tg_bot_config.messages_handlers.back_to_main_menu import back_to_main_menu_by_call, \
    back_to_main_menu_by_message
from tg_plus_django_project.tg_bot_config.messages_handlers.info import info_address, general_info, info_about
from tg_plus_django_project.tg_bot_config.messages_handlers.tv_category.tv_order_making import start_ordering, \
    ordering_fsm_handler_step_1, ordering_fsm_handler_step_2, ordering_fsm_handler_step_3, ordering_fsm_handler_step_4, \
    ordering_fsm_handler_step_5, ordering_fsm_handler_step_6, ordering_fsm_handler_step_7, ordering_fsm_handler_step_8
from tg_plus_django_project.tg_bot_config.messages_handlers.product_category_choice import \
    product_category_choice_by_message, product_category_choice_by_call
from tg_plus_django_project.tg_bot_config.messages_handlers.registration import start_reg, reg_fsm_handler_step_1, \
    reg_fsm_handler_step_2, reg_fsm_handler_step_3, reg_fsm_handler_step_4, reg_fsm_handler_step_5, \
    reg_fsm_handler_step_6
from tg_plus_django_project.tg_bot_config.messages_handlers.start_command import start_command
from tg_plus_django_project.tg_bot_config.messages_handlers.tv_category.brand_choice import tv_brand_choice
from tg_plus_django_project.tg_bot_config.messages_handlers.tv_category.samsung.samsung_tv_models import \
    tv_samsung_model_choice, tv_samsung_model_1_choice

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_API)
dp = Dispatcher(bot, storage=MemoryStorage())

# Шаблон:
# < --- --- --- --- --- --- --- --- >

# Команда старт:
dp.register_message_handler(
    start_command, commands=["start"]
)
# < --- --- --- --- --- --- --- --- >

# Вызов клавиатуры главного меню:
dp.register_callback_query_handler(
    back_to_main_menu_by_call, text='back_to_main_menu'
)
dp.register_message_handler(
    back_to_main_menu_by_message, text='Вернуться в главное меню'
)
# < --- --- --- --- --- --- --- --- >

# Инфо о магазине:
dp.register_message_handler(
    general_info, text='Информация о магазине'
)

dp.register_callback_query_handler(
    info_address, text='address'
)

dp.register_callback_query_handler(
    info_about, text='about'
)
# < --- --- --- --- --- --- --- --- >

# Активные заказы:
dp.register_message_handler(
    active_orders_data, text='Мои заказы'
)
# < --- --- --- --- --- --- --- --- >

# Регистрация нового пользователя:
dp.register_message_handler(
    start_reg, text='Зарегистрироваться'
)
dp.register_message_handler(
    reg_fsm_handler_step_1, state=UserReg.email
)
dp.register_message_handler(
    reg_fsm_handler_step_2, state=UserReg.password
)
dp.register_message_handler(
    reg_fsm_handler_step_3, state=UserReg.repeat_password
)
dp.register_message_handler(
    reg_fsm_handler_step_4, state=UserReg.phone_number
)
dp.register_message_handler(
    reg_fsm_handler_step_5, state=UserReg.name
)
dp.register_message_handler(
    reg_fsm_handler_step_6, state=UserReg.date_of_birth
)
# < --- --- --- --- --- --- --- --- >

# Оформление заказа для категории телевизоры:
dp.register_message_handler(
    start_ordering, text='Оформить заказ'
)
dp.register_callback_query_handler(
    ordering_fsm_handler_step_1, state=MakeAnOrder.category
)
dp.register_callback_query_handler(
    ordering_fsm_handler_step_2, state=MakeAnOrder.brand
)
dp.register_callback_query_handler(
    ordering_fsm_handler_step_3, state=MakeAnOrder.name
)
dp.register_callback_query_handler(
    ordering_fsm_handler_step_4, state=MakeAnOrder.amount
)
dp.register_message_handler(
    ordering_fsm_handler_step_5, state=MakeAnOrder.card_number
)
dp.register_message_handler(
    ordering_fsm_handler_step_6, state=MakeAnOrder.card_date
)
dp.register_message_handler(
    ordering_fsm_handler_step_7, state=MakeAnOrder.card_cvc
)
dp.register_message_handler(
    ordering_fsm_handler_step_8, state=MakeAnOrder.save_card_option
)
# < --- --- --- --- --- --- --- --- >

# Выбор категории товара:
dp.register_message_handler(
    product_category_choice_by_message, text='Открыть каталог'
)
dp.register_callback_query_handler(
    product_category_choice_by_call, text='to_categories'
)
dp.register_callback_query_handler(
    tv_brand_choice, text='tv'
)
# --- --- --- --- --- --- --- ---

# Категория телевизоры. Бренды:
dp.register_callback_query_handler(
    tv_samsung_model_choice, text='samsung_tv'
)
# < --- --- --- --- --- --- --- --- >

# Категория телевизоры. Бренд Samsung:
dp.register_callback_query_handler(
    tv_samsung_model_1_choice, text='QE65Q70DAU'
)
# < --- --- --- --- --- --- --- --- >

# Все сообщения:
dp.register_message_handler(
    all_messages
)
# < --- --- --- --- --- --- --- --- >

executor.start_polling(dp, skip_updates=True)