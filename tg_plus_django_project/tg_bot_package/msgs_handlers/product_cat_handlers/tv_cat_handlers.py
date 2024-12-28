import tg_plus_django_project.tg_bot_package.keyboards_file as kb_file


async def available_tv_models(call):
    await call.message.answer('У нас есть следующие модели...', reply_markup=kb_file.tv_models_choice_kb)
    await call.answer()


async def buy_samsung_func(call):
    with open('tg_bot_media/tv_models/samsung_tv_01.png', 'rb') as img:
        await call.message.answer_photo(img, 'Хороший тв', reply_markup=kb_file.buy_tv_kb)
        await call.answer()


async def go_back_to_tv_models_func(call):
    await call.message.answer('У нас есть следующие модели...', reply_markup=kb_file.tv_models_choice_kb)
    await call.answer()
