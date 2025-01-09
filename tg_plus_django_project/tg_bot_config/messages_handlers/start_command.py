from tg_plus_django_project.tg_bot_config.keyboards.kb_main_menu import main_menu_kb


async def start_command(message):
    await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=main_menu_kb)
