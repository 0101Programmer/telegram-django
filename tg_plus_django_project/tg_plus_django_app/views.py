import datetime

from config import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, View

from .forms import *
from .models import *


# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        is_active = User.objects.filter(is_active__exact=True)
        return render(request, self.template_name, {'is_active': is_active})


class UserPageView(View):
    template_name = 'user_page.html'

    def get(self, request, *args, **kwargs):
        active_user_filter = User.objects.values().filter(is_active__exact=True)
        active_user_data = ''

        for _ in active_user_filter:
            active_user_data = _

        return render(request, self.template_name, {'active_user_data': active_user_data})

    def post(self, request, *args, **kwargs):
        User.objects.filter(is_active__exact=True).update(is_active=False,
                                                          updated_at=datetime.datetime.now().astimezone().strftime(
                                                              "%Y-%m-%d | %H:%M:%S %z | %Z"))
        return HttpResponseRedirect('/')


class ConfirmOrderView(View):
    form_class = PaymentForm
    initial = {'key': 'value'}
    template_name = 'confirm_order_page.html'

    def get(self, request, order_id_to_change):
        form = self.form_class(initial=self.initial)
        active_user_filter = User.objects.values().filter(is_active__exact=True)
        active_user_order_to_change = ''

        for _ in active_user_filter:
            active_user_order_to_change = _['orders'][f'{order_id_to_change}']

        return render(request, self.template_name, {'active_user_filter': active_user_filter,
                                                    'active_user_order_to_change': active_user_order_to_change,
                                                    'order_id_to_change': order_id_to_change, 'form': form, })

    def post(self, request, order_id_to_change):
        form = self.form_class(request.POST)

        if form.is_valid():
            card_num = str(form.cleaned_data['card_num'])
            card_date = form.cleaned_data['card_date']
            card_cvc = form.cleaned_data['card_cvc']

            if not is_valid_card_num(card_num):
                error = 'Номер дебетовой банковской карты может состоять из 13, 16, 18 или 19 цифр. Укажите его в формате "1 2 22 66 5 10 5..."'
                return render(request, 'error.html', {'error': error})

            elif len(str(card_cvc)) != 3:
                error = 'Некорректный трёхзначный код'
                return render(request, 'error.html', {'error': error})

            elif not is_valid_card_date(card_date):
                error = 'Пожалуйста, укажите срок действия карты в формате ГГГГ-ММ (карта должна быть активной)'
                return render(request, 'error.html', {'error': error})

            else:
                user_filter = User.objects.values().get(is_active=True)

                User.objects.filter(is_active__exact=True).update(orders=user_filter['orders'] |
                                                                         {f'{order_id_to_change}': {"model_name":
                                                                                                        user_filter[
                                                                                                            'orders'][
                                                                                                            f'{order_id_to_change}'][
                                                                                                            'model_name'],
                                                                                                    "model_name_for_client":
                                                                                                        user_filter[
                                                                                                            'orders'][
                                                                                                            f'{order_id_to_change}'][
                                                                                                            'model_name_for_client'],
                                                                                                    "product_amount":
                                                                                                        user_filter[
                                                                                                            'orders'][
                                                                                                            f'{order_id_to_change}'][
                                                                                                            'product_amount'],
                                                                                                    "product_price":
                                                                                                        user_filter[
                                                                                                            'orders'][
                                                                                                            f'{order_id_to_change}'][
                                                                                                            'product_price'],
                                                                                                    "updated_at": datetime.datetime.now().astimezone().strftime(
                                                                                                        "%Y-%m-%d | %H:%M:%S %z | %Z"),
                                                                                                    "status": "confirmed",
                                                                                                    "total":
                                                                                                        user_filter[
                                                                                                            'orders'][
                                                                                                            f'{order_id_to_change}'][
                                                                                                            'total'],
                                                                                                    "paid_by": {"card_num": card_num,
                                                                                                                "card_date": card_date,
                                                                                                                "card_cvc": card_cvc}, }})

                return HttpResponseRedirect('/user_page')

        return render(request, self.template_name, {'form': form})








class CancelOrderView(View):
    template_name = 'cancel_order_page.html'

    def get(self, request, order_id_to_change):
        user_filter = User.objects.values().get(is_active=True)

        User.objects.filter(is_active__exact=True).update(orders=user_filter['orders'] |
             {f'{order_id_to_change}': {"model_name": user_filter['orders'][f'{order_id_to_change}']['model_name'],
            "model_name_for_client": user_filter['orders'][f'{order_id_to_change}']['model_name_for_client'],
              "product_amount": user_filter['orders'][f'{order_id_to_change}']['product_amount'],
              "product_price": user_filter['orders'][f'{order_id_to_change}']['product_price'],
              "updated_at": datetime.datetime.now().astimezone().strftime("%Y-%m-%d | %H:%M:%S %z | %Z"),
              "status": "canceled",
              "total": user_filter['orders'][f'{order_id_to_change}']['total'], }})

        return HttpResponseRedirect('/user_page')




class ChangeOrderView(View):
    form_class = BuyForm
    initial = {'key': 'value'}
    template_name = 'change_order_page.html'

    def get(self, request, order_id_to_change):
        form = self.form_class(initial=self.initial)
        active_user_filter = User.objects.values().filter(is_active__exact=True)
        active_user_order_to_change = ''

        for _ in active_user_filter:
            active_user_order_to_change = _['orders'][f'{order_id_to_change}']

        return render(request, self.template_name, {'active_user_filter': active_user_filter,
                                                    'active_user_order_to_change': active_user_order_to_change,
                                                    'order_id_to_change': order_id_to_change, 'form': form, })

    def post(self, request, order_id_to_change):
        form = self.form_class(request.POST)

        if form.is_valid():
            product_amount = form.cleaned_data['product_amount']
            user_filter = User.objects.values().get(is_active=True)

            User.objects.filter(is_active__exact=True).update(orders=user_filter['orders'] |
                                                                     {f'{order_id_to_change}': {"model_name":
                                                                                                    user_filter[
                                                                                                        'orders'][
                                                                                                        f'{order_id_to_change}'][
                                                                                                        'model_name'],
                                                                                                "model_name_for_client":
                                                                                                    user_filter[
                                                                                                        'orders'][
                                                                                                        f'{order_id_to_change}'][
                                                                                                        'model_name_for_client'],
                                                                                                "product_amount": product_amount,
                                                                                                "product_price":
                                                                                                    user_filter[
                                                                                                        'orders'][
                                                                                                        f'{order_id_to_change}'][
                                                                                                        'product_price'],
                                                                                                "updated_at": datetime.datetime.now().astimezone().strftime(
                                                                                                    "%Y-%m-%d | %H:%M:%S %z | %Z"),
                                                                                                "status": user_filter[
                                                                                                    'orders'][
                                                                                                    f'{order_id_to_change}'][
                                                                                                    'status'],
                                                                                                "total": round(
                                                                                                    product_amount *
                                                                                                    user_filter[
                                                                                                        'orders'][
                                                                                                        f'{order_id_to_change}'][
                                                                                                        'product_price'],
                                                                                                    2), }})
            return HttpResponseRedirect('/user_page')

        return render(request, self.template_name, {'form': form})


class ChangeDataView(View):
    form_class = ChangeDataForm
    initial = {'key': 'value'}
    template_name = 'change_data_page.html'

    def get(self, request, user_data_to_change):

        user_data_to_change_name = ''
        if user_data_to_change == 'name':
            user_data_to_change_name = 'Имя'
        elif user_data_to_change == 'email':
            user_data_to_change_name = 'Email'
        elif user_data_to_change == 'password':
            user_data_to_change_name = 'Пароль'
        elif user_data_to_change == 'tg_username':
            user_data_to_change_name = 'Логин в телеграм'
        elif user_data_to_change == 'phone_number':
            user_data_to_change_name = 'Номер телефона'

        form = self.form_class(initial=self.initial)
        active_user_filter = User.objects.values().filter(is_active__exact=True)
        active_user_data_to_change = ''

        for _ in active_user_filter:
            active_user_data_to_change = _[f'{user_data_to_change}']

        return render(request, self.template_name, {'active_user_data_to_change': active_user_data_to_change,
                                                    'user_data_to_change': user_data_to_change, 'form': form,
                                                    'user_data_to_change_name': user_data_to_change_name, })

    def post(self, request, user_data_to_change):
        form = self.form_class(request.POST)

        if form.is_valid():
            variable = form.cleaned_data['variable']
            confirmation_variable = form.cleaned_data['confirmation_variable']

            if user_data_to_change == 'email':
                is_email_existed = User.objects.filter(email__exact=variable)
                if is_email_existed:
                    error = 'Пользователь с таким email уже зарегистрирован'
                    return render(request, 'error.html', {'error': error})
                elif not check_email(variable):
                    error = 'Пожалуйста, укажите email в формате example@mail.ru'
                    return render(request, 'error.html', {'error': error})
                else:
                    User.objects.filter(is_active__exact=True).update(email=variable,
                                                                      updated_at=datetime.datetime.now().astimezone().strftime(
                                                                          "%Y-%m-%d | %H:%M:%S %z | %Z"))
                    return HttpResponseRedirect('/user_page')

            elif user_data_to_change == 'password':
                if not password_validate(variable):
                    error = 'Пожалуйста, придумайте надёжный пароль. Требования: не менее восьми символов, наличие спецсимволов, а также больших и строчных букв. (Пример: -Secr3t.)'
                    return render(request, 'error.html', {'error': error})
                elif variable == '-Secr3t.':
                    error = 'Пожалуйста, не используйте пароль из примера.'
                    return render(request, 'error.html', {'error': error})
                elif variable != confirmation_variable:
                    error = 'Пароли не совпадают'
                    return render(request, 'error.html', {'error': error})
                else:
                    User.objects.filter(is_active__exact=True).update(password=variable,
                                                                      updated_at=datetime.datetime.now().astimezone().strftime(
                                                                          "%Y-%m-%d | %H:%M:%S %z | %Z"))
                    return HttpResponseRedirect('/user_page')

            elif user_data_to_change == 'tg_username':
                is_tg_username_existed = User.objects.filter(tg_username__exact=variable)
                if is_tg_username_existed:
                    error = 'Пользователь с таким телеграм логином уже зарегистрирован'
                    return render(request, 'error.html', {'error': error})
                else:
                    User.objects.filter(is_active__exact=True).update(tg_username=variable,
                                                                      updated_at=datetime.datetime.now().astimezone().strftime(
                                                                          "%Y-%m-%d | %H:%M:%S %z | %Z"))
                    return HttpResponseRedirect('/user_page')

            elif user_data_to_change == 'phone_number':
                is_phone_existed = User.objects.filter(phone_number__exact=variable)
                if is_phone_existed:
                    error = 'Пользователь с таким номером телефона уже зарегистрирован'
                    return render(request, 'error.html', {'error': error})
                elif not check_phone_number(variable):
                    error = 'Введите номер телефона в международном формате. (Например, +7 999 999 99 99)'
                    return render(request, 'error.html', {'error': error})
                else:
                    User.objects.filter(is_active__exact=True).update(phone_number=variable,
                                                                      updated_at=datetime.datetime.now().astimezone().strftime(
                                                                          "%Y-%m-%d | %H:%M:%S %z | %Z"))
                    return HttpResponseRedirect('/user_page')

            elif user_data_to_change == 'name':
                User.objects.filter(is_active__exact=True).update(name=variable,
                                                                  updated_at=datetime.datetime.now().astimezone().strftime(
                                                                      "%Y-%m-%d | %H:%M:%S %z | %Z"))
                return HttpResponseRedirect('/user_page')

        return render(request, self.template_name, {'form': form})


class LogFormView(View):
    form_class = LogForm
    initial = {'key': 'value'}
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            is_email_existed = User.objects.filter(email__exact=email)

            if not check_email(email):
                error = 'Пожалуйста, укажите email в формате example@mail.ru'
                return render(request, 'error.html', {'error': error})

            elif not is_email_existed:
                error = 'Пользователя с указанным email не существует'
                return render(request, 'error.html', {'error': error})

            elif password != User.objects.get(email=email).password:
                error = 'Пароль не подходит'
                return render(request, 'error.html', {'error': error})
            else:
                User.objects.filter(email__exact=email).update(is_active=True,
                                                               updated_at=datetime.datetime.now().astimezone().strftime(
                                                                   "%Y-%m-%d | %H:%M:%S %z | %Z"))
                return HttpResponseRedirect('/user_page')

        return render(request, self.template_name, {'form': form})


class RegFormView(View):
    form_class = RegForm
    initial = {'key': 'value'}
    template_name = 'reg_and_auth_page.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            tg_username = form.cleaned_data['tg_username']
            phone_number = form.cleaned_data['phone_number']
            date_of_birth = form.cleaned_data['date_of_birth']

            is_email_existed = User.objects.filter(email__exact=email)
            is_phone_existed = User.objects.filter(phone_number__exact=phone_number)
            is_tg_username_existed = User.objects.filter(tg_username__exact=tg_username)

            if not check_email(email):
                error = 'Пожалуйста, укажите email в формате example@mail.ru'
                return render(request, 'error.html', {'error': error})

            elif password == '-Secr3t.':
                error = 'Пожалуйста, не используйте пароль из примера.'
                return render(request, 'error.html', {'error': error})

            elif password != repeat_password:
                error = 'Пароли не совпадают'
                return render(request, 'error.html', {'error': error})

            elif not password_validate(password):
                error = 'Пожалуйста, придумайте надёжный пароль. Требования: не менее восьми символов, наличие спецсимволов, а также больших и строчных букв. (Пример: -Secr3t.)'
                return render(request, 'error.html', {'error': error})

            elif not check_phone_number(phone_number):
                error = 'Введите номер телефона в международном формате. (Например, +7 999 999 99 99)'
                return render(request, 'error.html', {'error': error})

            elif not date_of_birth_validate(date_of_birth):
                error = 'Введите дату рождения в формате ГГГГ-ММ-ДД'
                return render(request, 'error.html', {'error': error})

            elif not is_adult(date_of_birth):
                error = 'Извините, но регистрация у нас возможна только с 18 лет'
                return render(request, 'error.html', {'error': error})

            elif is_email_existed:
                error = 'Пользователь с таким email уже зарегистрирован'
                return render(request, 'error.html', {'error': error})

            elif is_phone_existed:
                error = 'Пользователь с таким номером телефона уже зарегистрирован'
                return render(request, 'error.html', {'error': error})

            elif is_tg_username_existed and len(tg_username) != 0:
                error = 'Пользователь с таким телеграмм логином уже зарегистрирован'
                return render(request, 'error.html', {'error': error})

            else:
                User.objects.create(name=name, email=email, password=password, tg_username=tg_username,
                                    phone_number=phone_number, date_of_birth=date_of_birth, is_active=True)
                return HttpResponseRedirect('/user_page')

        return render(request, self.template_name, {'form': form})


class CatalogPageView(TemplateView):
    template_name = 'catalog_page.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ConsolesPageView(TemplateView):
    template_name = 'cat_pages/cons_page.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ConsoleModelPageView(View):
    form_class = BuyForm
    initial = {'key': 'value'}
    template_name = 'cat_pages/cons_model_page.html'

    def get(self, request, console_model):
        form = self.form_class(initial=self.initial)

        product_filter = Product.objects.values().get(model_name=console_model)

        is_active = User.objects.filter(is_active__exact=True)

        user_filter = User.objects.values().get(is_active=True)

        return render(request, self.template_name,
                      {'product_filter': product_filter, 'is_active': is_active, 'form': form, })

    def post(self, request, console_model):
        form = self.form_class(request.POST)
        product_filter = Product.objects.values().get(model_name=console_model)

        user_filter = User.objects.values().get(is_active=True)

        if form.is_valid():
            product_amount = form.cleaned_data['product_amount']

            if user_filter['orders'] is not None:
                # User.objects.filter(is_active__exact=True).update(orders=None)
                User.objects.filter(is_active__exact=True).update(orders=user_filter['orders'] | {
                    f'{int(max(user_filter["orders"])) + 1}': {"model_name": console_model,
                                                               "model_name_for_client": product_filter[
                                                                   "model_name_for_customer"],
                                                               "product_amount": product_amount,
                                                               "product_price": product_filter["price"],
                                                               "updated_at": datetime.datetime.now().astimezone().strftime(
                                                                   "%Y-%m-%d | %H:%M:%S %z | %Z"), "status": "ordered",
                                                               "total": round(product_amount * product_filter["price"],
                                                                              2), }})
            else:
                User.objects.filter(is_active__exact=True).update(orders={f'{1}': {"model_name": console_model,
                                                                                   "model_name_for_client":
                                                                                       product_filter[
                                                                                           "model_name_for_customer"],
                                                                                   "product_amount": product_amount,
                                                                                   "product_price": product_filter[
                                                                                       "price"],
                                                                                   "updated_at": datetime.datetime.now().astimezone().strftime(
                                                                                       "%Y-%m-%d | %H:%M:%S %z | %Z"),
                                                                                   "status": "ordered", "total": round(
                        product_amount * product_filter["price"], 2), }})

            return HttpResponseRedirect('/console_page')

        return render(request, self.template_name, {'form': form})
