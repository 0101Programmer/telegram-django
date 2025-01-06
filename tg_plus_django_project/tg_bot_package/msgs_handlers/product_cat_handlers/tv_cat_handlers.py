from tg_plus_django_project.tg_bot_package.keyboards_dir.products_models_kbs import tv_models_choice_kb


async def available_tv_models(call):
    await call.message.answer('У нас есть следующие модели телевизоров', reply_markup=tv_models_choice_kb.tv_models_choice_kb)
    await call.answer()


async def buy_samsung_func(call):
    with open('tg_bot_media/tv_models/samsung_tv_01.png', 'rb') as img:
        await call.message.answer_photo(img, 'Хороший тв', reply_markup=tv_models_choice_kb.buy_tv_kb)
        await call.answer()


async def go_back_to_tv_models_func(call):
    await call.message.answer('У нас есть следующие модели...', reply_markup=tv_models_choice_kb.tv_models_choice_kb)
    await call.answer()
