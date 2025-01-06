from tg_plus_django_project.tg_bot_package.keyboards_dir import prod_cat_choice_kb


async def prod_cat_choice(message):
    await message.answer('Что вас интересует?', reply_markup=prod_cat_choice_kb.prod_cat_choice_kb)
