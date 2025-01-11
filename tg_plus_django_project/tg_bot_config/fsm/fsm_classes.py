from aiogram.dispatcher.filters.state import State, StatesGroup


class UserReg(StatesGroup):
    email = State()
    password = State()
    repeat_password = State()
    phone_number = State()
    name = State()
    date_of_birth = State()


class MakeAnOrder(StatesGroup):
    category = State()
    brand = State()
    name = State()
    amount = State()
    card_number = State()
    card_date = State()
    card_cvc = State()
    save_card_option = State()
