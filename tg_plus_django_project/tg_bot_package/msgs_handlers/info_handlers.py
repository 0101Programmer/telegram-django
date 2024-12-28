import tg_plus_django_project.tg_bot_package.keyboards_file as kb_file
import tg_plus_django_project.tg_bot_package.texts as txt_file


async def info(message):
    await message.answer('Что вас интересует?', reply_markup=kb_file.info_kb)


async def info_address(call):
    await call.message.answer(txt_file.shop_address_text)
    await call.answer()


async def info_about(call):
    await call.message.answer(txt_file.shop_info_text)
    await call.answer()

