import datetime

from db_engine import Base

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
    model_name='test_model',
    model_name_for_customer='Test',
    description='Just test',
    price=1999.99,
    category='test_cat',
    images_paths={1: "/test1", 2: "/test2"}
)
