from tg_plus_django_project.tg_bot_package.keyboards_dir import main_kb


async def back_to_home_by_message(message):
    await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_kb.main_kb)


async def back_to_home_by_call(call):
    await call.message.answer(f'Добро пожаловать в "Best Price Hardware Store"!', reply_markup=main_kb.main_kb)
    await call.answer()
