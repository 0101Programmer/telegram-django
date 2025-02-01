from tg_plus_django_project.tg_bot_config.keyboards.tv_keyboards.samsung.kb_samsung_tv_models import \
    tv_samsung_model_choice_kb, back_to_tv_samsung_model_choice_kb
from tg_plus_django_project.tg_bot_config.texts.tv_category_txt.samsung_tv_txt import samsung_tv_models_dict


async def tv_samsung_model_choice(call):
    await call.message.answer('Выберите интересующую вас модель',
                              reply_markup=tv_samsung_model_choice_kb)
    await call.answer()


async def tv_samsung_model_1_choice(call):
    product_name = "QE65Q70DAU"
    with open(f'{samsung_tv_models_dict[product_name]["images_paths"]["1"]}', 'rb') as img:
        await call.message.answer_photo(img, samsung_tv_models_dict[product_name]["name"][1],
                                        reply_markup=back_to_tv_samsung_model_choice_kb)
        await call.message.answer(samsung_tv_models_dict[product_name]["description"])
        await call.answer()
