import tg_plus_django_project.tg_bot_package.keyboards_file as kb_file



async def info(message):
    await message.answer('Что вас интересует?', reply_markup=kb_file.info_kb)


async def info_address(call):
    await call.message.answer('Мы располагаемся по адресу...')
    await call.answer()