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
    name='test_model',
    description='Just test',
    price=1999.99,
    category='test_cat',
    brand="test_brand",
    images_paths={1: "/test1", 2: "/test2"}
)

# available_cards = {}
# user_data = session.query(User).filter(
#                 User.tg_username == "baranovvk").one_or_none()
# for k, v in user_data.orders.items():
#     if v["card_data"] is not None:
#         if is_valid_card_date(v["card_data"]["card_date"]):
#             available_cards[v["card_data"]["card_number"]] = {"card_date": v["card_data"]['card_date'], "card_cvc": v["card_data"]['card_cvc']}
# print("1234567890000" in available_cards)