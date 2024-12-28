from config import *
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from ..forms import *
from ..models import *


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
                User.objects.filter(email=email).update(
                                                               updated_at=datetime.datetime.now().astimezone().strftime(
                                                                   "%Y-%m-%d | %H:%M:%S %z | %Z")
                )
                user_filter = User.objects.values().filter(email=email)
                user_data = ''

                for _ in user_filter:
                    user_data = _

                request.session['id'] = user_data["id"]

                return HttpResponseRedirect(f'/user_page/{user_data["id"]}')

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
                user_data = {'user_sys_info': check_user_sys_info()}
                User.objects.create(name=name, email=email, password=password, tg_username=tg_username,
                                    phone_number=phone_number, date_of_birth=date_of_birth, user_data=user_data, is_active=True)
                max_id = User.objects.aggregate(max_id=Max('id'))['max_id']

                request.session['id'] = max_id

                return HttpResponseRedirect(f'/{max_id}')

        return render(request, self.template_name, {'form': form})