import tg_plus_django_project.tg_bot_package.texts as txt_file
from tg_plus_django_project.tg_bot_package.keyboards_dir import info_kb


async def info(message):
    await message.answer('Что вас интересует?', reply_markup=info_kb.info_kb)


async def info_address(call):
    await call.message.answer(txt_file.shop_address_text)
    await call.answer()


async def info_about(call):
    await call.message.answer(txt_file.shop_info_text)
    await call.answer()

