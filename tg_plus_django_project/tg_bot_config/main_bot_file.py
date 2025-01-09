import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from tg_plus_django_project.config import *
from tg_plus_django_project.tg_bot_config.fsm.fsm_classes import UserReg
from tg_plus_django_project.tg_bot_config.messages_handlers.active_orders import active_orders_data
from tg_plus_django_project.tg_bot_config.messages_handlers.all_messages import all_messages
from tg_plus_django_project.tg_bot_config.messages_handlers.back_to_main_menu import back_to_main_menu_by_call
from tg_plus_django_project.tg_bot_config.messages_handlers.info import info_address, general_info, info_about
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
    back_to_main_menu_by_call, text='back_to_home'
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