from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from config import *
from ..forms import *
from ..models import *


class UserPageView(View):
    template_name = 'user_page.html'

    def get(self, request, user_id):

        try:
            if user_id != request.session['id']:
                error = 'Доступ запрещён'
                return render(request, 'error.html', {'error': error})
        except KeyError:
            error = 'Доступ запрещён'
            return render(request, 'error.html', {'error': error})

        active_user_filter = User.objects.values().filter(id=user_id)
        active_user_data = ''

        for _ in active_user_filter:
            active_user_data = _

        return render(request, self.template_name, {'active_user_data': active_user_data, "user_id": user_id})

    def post(self, request, user_id):
        User.objects.filter(id=user_id).update(
            updated_at=datetime.datetime.now()
        )

        del request.session['id']

        return HttpResponseRedirect('/')


class ChangeDataView(View):
    form_class = ChangeDataForm
    initial = {'key': 'value'}
    template_name = 'change_data_page.html'

    def get(self, request, user_id, user_data_to_change):

        try:
            if user_id != request.session['id']:
                error = 'Доступ запрещён'
                return render(request, 'error.html', {'error': error})
        except KeyError:
            error = 'Доступ запрещён'
            return render(request, 'error.html', {'error': error})

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
        active_user_filter = User.objects.values().filter(id=user_id)
        active_user_data_to_change = ''

        for _ in active_user_filter:
            active_user_data_to_change = _[f'{user_data_to_change}']

        return render(request, self.template_name, {'active_user_data_to_change': active_user_data_to_change,
                                                    'user_data_to_change': user_data_to_change, 'form': form,
                                                    'user_data_to_change_name': user_data_to_change_name,
                                                    'user_id': user_id, })

    def post(self, request, user_id, user_data_to_change):
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
                    User.objects.filter(id=user_id).update(email=variable,
                                                           updated_at=datetime.datetime.now())
                    return HttpResponseRedirect(f'/user_page/{user_id}')

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
                    User.objects.filter(id=user_id).update(password=variable,
                                                           updated_at=datetime.datetime.now())
                    return HttpResponseRedirect(f'/user_page/{user_id}')

            elif user_data_to_change == 'tg_username':
                is_tg_username_existed = User.objects.filter(tg_username__exact=variable)
                if is_tg_username_existed:
                    error = 'Пользователь с таким телеграм логином уже зарегистрирован'
                    return render(request, 'error.html', {'error': error})
                else:
                    User.objects.filter(id=user_id).update(tg_username=variable,
                                                           updated_at=datetime.datetime.now())
                    return HttpResponseRedirect(f'/user_page/{user_id}')

            elif user_data_to_change == 'phone_number':
                is_phone_existed = User.objects.filter(phone_number__exact=variable)
                if is_phone_existed:
                    error = 'Пользователь с таким номером телефона уже зарегистрирован'
                    return render(request, 'error.html', {'error': error})
                elif not check_phone_number(variable):
                    error = 'Введите номер телефона в международном формате. (Например, +7 999 999 99 99)'
                    return render(request, 'error.html', {'error': error})
                else:
                    User.objects.filter(id=user_id).update(phone_number=variable,
                                                           updated_at=datetime.datetime.now())
                    return HttpResponseRedirect(f'/user_page/{user_id}')

            elif user_data_to_change == 'name':
                User.objects.filter(id=user_id).update(name=variable,
                                                       updated_at=datetime.datetime.now())
                return HttpResponseRedirect(f'/user_page/{user_id}')

        return render(request, self.template_name, {'form': form})
