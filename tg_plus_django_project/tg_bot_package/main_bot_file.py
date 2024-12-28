import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from tg_plus_django_project.config import *
import msgs_handlers.all_messages_handler as amh
import msgs_handlers.start_command_handler as sch
import msgs_handlers.back_to_home_handlers as bth
import msgs_handlers.info_handlers as ih
import msgs_handlers.cat_choice_handler as cch
import msgs_handlers.product_cat_handlers.tv_cat_handlers as tvh
import msgs_handlers.my_orders_handlers as moh
import msgs_handlers.registration_handlers as rh
from fsm_classes import *


# Возврат:
# --- --- --- --- --- --- --- ---

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_API)
dp = Dispatcher(bot, storage=MemoryStorage())

dp.register_message_handler(
    sch.start_command, commands=["start"]
)

# Возврат на главную страницу:
dp.register_message_handler(
    bth.back_to_home_by_message, text='На главную'
)

dp.register_callback_query_handler(
    bth.back_to_home_by_call, text='back_to_home'
)
# --- --- --- --- --- --- --- ---

# Инфо о магазине:
dp.register_message_handler(
    ih.info, text='Информация о магазине'
)

dp.register_callback_query_handler(
    ih.info_address, text='address'
)
# --- --- --- --- --- --- --- ---

# Выбор категории товара:
dp.register_message_handler(
    cch.prod_cat_choice, text='Выбор категории товара'
)
# --- --- --- --- --- --- --- ---

# Категория телевизоры:
dp.register_callback_query_handler(
    tvh.available_tv_models, text='tv'
)
dp.register_callback_query_handler(
    tvh.buy_samsung_func, text='samsung'
)
dp.register_callback_query_handler(
    tvh.go_back_to_tv_models_func, text='back_to_tv_models_choice'
)
# --- --- --- --- --- --- --- ---

# Мои заказы:
dp.register_message_handler(
    moh.reg_auth_choice, text='Мои заказы'
)
dp.register_message_handler(
    moh.reg_choice, text='Я новый клиент'
)
dp.register_callback_query_handler(
    moh.go_back_to_my_orders_func, text='back_to_my_orders_kb'
)
# --- --- --- --- --- --- --- ---

# Регистрация нового пользователя:
dp.register_callback_query_handler(
    rh.start_reg, text='new_client_registration'
)
dp.register_message_handler(
    rh.reg_fsm_handler_step_1, state=UserReg.email
)
dp.register_message_handler(
    rh.reg_fsm_handler_step_2, state=UserReg.password
)
dp.register_message_handler(
    rh.reg_fsm_handler_step_3, state=UserReg.repeat_password
)
dp.register_message_handler(
    rh.reg_fsm_handler_step_4, state=UserReg.phone_number
)
dp.register_message_handler(
    rh.reg_fsm_handler_step_5, state=UserReg.name
)
dp.register_message_handler(
    rh.reg_fsm_handler_step_6, state=UserReg.date_of_birth
)
# --- --- --- --- --- --- --- ---

# Все сообщения:
dp.register_message_handler(
    amh.all_messages
)
# --- --- --- --- --- --- --- ---


executor.start_polling(dp, skip_updates=True)
