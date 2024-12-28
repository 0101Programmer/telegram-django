from aiogram.dispatcher.filters.state import State, StatesGroup


class UserReg(StatesGroup):
    email = State()
    password = State()
    repeat_password = State()
    phone_number = State()
    name = State()
    date_of_birth = State()