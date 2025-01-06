from tg_plus_django_project.tg_bot_package.keyboards_dir import main_kb


async def start_command(message):
    await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_kb.main_kb)
