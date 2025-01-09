from tg_plus_django_project.tg_bot_config.keyboards.kb_info import info_kb
from tg_plus_django_project.tg_bot_config.texts.about_shop_txt import shop_address_text, shop_info_text


async def general_info(message):
    await message.answer('Что вас интересует?', reply_markup=info_kb)


async def info_address(call):
    await call.message.answer(shop_address_text)
    await call.answer()


async def info_about(call):
    await call.message.answer(shop_info_text)
    await call.answer()