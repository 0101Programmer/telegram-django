import tg_plus_django_project.tg_bot_package.keyboards_file as kb_file

async def start_command(message):
    await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=kb_file.main_kb)
