import datetime
import re

import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type, NumberParseException

BOT_API = '6408941142:AAH4A5ZDeUHpPrGIJeNJGPCnipORhdrqAi4'

db_password = '1630balalai'
db_name = 'tg_hardware_store_postgres_db'
db_user = "postgres"
db_port = "5432"
db_host = "localhost"


def check_email(email):
    pattern = re.compile(r"^\S+@\S+\.\S+$")
    is_valid = pattern.match(email)
    if is_valid is not None:
        return True
    else:
        return False


def check_phone_number(number):
    try:
        process = carrier._is_mobile(number_type(phonenumbers.parse(str(number))))
        if process:
            p_num = phonenumbers.parse(str(number), None)
            return phonenumbers.format_number(p_num, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        else:
            return False
    except NumberParseException:
        return False


def date_of_birth_validate(date_text):
    try:
        datetime.date.fromisoformat(str(date_text))
        return True
    except ValueError:
        return False


def is_adult(birthdate):
    try:
        birthday = datetime.datetime.strptime(str(birthdate), '%Y-%m-%d')
        today = datetime.datetime.today()
        age = (today - birthday).days // 365
        return age >= 18
    except ValueError:
        return False


def password_validate(password):
    password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    if re.match(password_pattern, str(password)) is None:
        return False
    else:
        return True


def is_valid_card_date(date_str):
    pattern = r'^(\d{4})-(\d{2})$'

    match = re.match(pattern, str(date_str))
    if not match:
        return False

    year = int(match.group(1))
    month = int(match.group(2))

    current_year = datetime.datetime.now().year

    if year >= current_year and 1 <= month <= 12:
        return True
    else:
        return False

def is_valid_card_num(num_str):
    card_number_pattern = "[0-9]{13,19}"
    if not num_str.isnumeric():
        return False
    if re.match(card_number_pattern, str(num_str)) and len(num_str) <= 19:
        return True
    else:
        return False