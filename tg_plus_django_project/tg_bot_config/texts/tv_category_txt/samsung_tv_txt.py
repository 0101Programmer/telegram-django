from tg_plus_django_project.sqlalchemy_connection_config.existed_db_models import Product, session
samsung_tv_models_dict = {
    "QE65Q70DAU":
        {"name": session.query(Product).filter(Product.name.contains(["QE65Q70DAU"])).first().name,
         "description": session.query(Product).filter(Product.name.contains(["QE65Q70DAU"])).first().description,
         "price": session.query(Product).filter(Product.name.contains(["QE65Q70DAU"])).first().price,
         "images_paths": session.query(Product).filter(Product.name.contains(["QE65Q70DAU"])).first().images_paths},
}
