from django import forms


class RegForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ваше имя")
    email = forms.EmailField(label="Ваш Email")
    password = forms.CharField(max_length=100, label="Пароль")
    repeat_password = forms.CharField(max_length=100, label="Повторите пароль")
    tg_username = forms.CharField(max_length=100, required=False,
                                  label="Логин в Телеграмм (поле можно оставить пустым)")
    phone_number = forms.CharField(max_length=100, label="Номер телефона")
    date_of_birth = forms.CharField(label="Дата рождения")


class ChangeDataForm(forms.Form):
    variable = forms.CharField(max_length=100, label="Новое значение")
    confirmation_variable = forms.CharField(max_length=100, required=False, label="Повторите ввод")


class LogForm(forms.Form):
    email = forms.EmailField(label="Ваш Email")
    password = forms.CharField(max_length=100, label="Пароль")


class BuyForm(forms.Form):
    product_amount = forms.IntegerField(label="Количество", initial=1, min_value=1, max_value=10)


class PaymentForm(forms.Form):
    card_num = forms.CharField(label="Номер карты", required=True)
    card_date = forms.CharField(label="Срок действия", required=True)
    card_cvc = forms.IntegerField(label="Трёхзначный код с обратной стороны", required=True)
