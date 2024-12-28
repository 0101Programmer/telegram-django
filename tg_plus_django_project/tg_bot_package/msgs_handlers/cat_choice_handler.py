import tg_plus_django_project.tg_bot_package.keyboards_file as kb_file

async def prod_cat_choice(message):
    await message.answer('Что вас интересует?', reply_markup=kb_file.prod_cat_choice_kb)