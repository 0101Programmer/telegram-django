from tg_plus_django_project.tg_bot_config.keyboards.kb_product_categories import product_categories_kb
from tg_plus_django_project.tg_bot_config.keyboards.tv_keyboards.kb_brand_choice import tv_brand_choice_kb


async def product_category_choice_by_message(message):
    await message.answer('Сейчас у нас доступны следующие категории товаров', reply_markup=product_categories_kb)


async def product_category_choice_by_call(call):
    await call.message.answer('Сейчас у нас доступны следующие категории товаров', reply_markup=product_categories_kb)
    await call.answer()

