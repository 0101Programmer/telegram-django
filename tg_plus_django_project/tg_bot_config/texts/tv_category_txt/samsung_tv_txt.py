from tg_plus_django_project.sqlalchemy_connection_config.existed_db_models import Product, session
samsung_tv_models_dict = {
    1:
        {"name": session.get(Product, 1).name,
         "description": session.get(Product, 1).description,
         "price": session.get(Product, 1).price,
         "images_paths": session.get(Product, 1).images_paths},
}