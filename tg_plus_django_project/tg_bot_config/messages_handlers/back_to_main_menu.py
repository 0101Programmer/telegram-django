from tg_plus_django_project.tg_bot_config.keyboards.kb_main_menu import main_menu_kb


async def back_to_main_menu_by_message(message):
    await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_menu_kb)


async def back_to_main_menu_by_call(call):
    await call.message.answer(f'Добро пожаловать, {call.from_user.username}!', reply_markup=main_menu_kb)
    await call.answer()
