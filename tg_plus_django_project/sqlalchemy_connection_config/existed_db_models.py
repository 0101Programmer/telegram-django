import datetime
import json

from tg_plus_django_project.config import is_valid_card_date
from tg_plus_django_project.sqlalchemy_connection_config.db_engine import Base, session

Product = Base.classes.tg_plus_django_app_product
User = Base.classes.tg_plus_django_app_user

user_example = User(
    name='test_user',
    email='t@mail.ru',
    password='t1',
    tg_username="test",
    phone_number='7 999 999 99 99',
    date_of_birth="2000-01-01",
    orders=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
)

product_example = Product(
    name=["QE65Q70DAU", "QE65Q70DAU"],
    description='Description',
    price=1999.99,
    category=["tv", "Телевизоры"],
    brand=["samsung", "Samsung"],
    images_paths={1: "./bot_media/tv_brands/samsung/samsung_tv_01.png"}
)

# session.add(product_example)
# session.commit()

# product = session.query(Product).filter(Product.name.contains(["QE65Q70DAU"])).first()
