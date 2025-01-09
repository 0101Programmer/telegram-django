from tg_plus_django_project.tg_bot_config.keyboards.tv_keyboards.kb_brand_choice import tv_brand_choice_kb


async def tv_brand_choice(call):
    await call.message.answer('Выберите интересующую вас марку',
                              reply_markup=tv_brand_choice_kb)
    await call.answer()