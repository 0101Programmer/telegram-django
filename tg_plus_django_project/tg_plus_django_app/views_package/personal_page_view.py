from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from config import *
from ..forms import *
from ..models import *


class UserPersonalPageView(View):
    template_name = 'user_page.html'

    def get(self, request, user_id):
        try:
            if user_id != request.session['id']:
                error = 'Доступ запрещён'
                return render(request, 'error.html', {'error': error})
        except KeyError:
            error = 'Доступ запрещён'
            return render(request, 'error.html', {'error': error})
        user_data = User.objects.get(id=user_id)
        return render(request, self.template_name, {'user_data': user_data, "user_id": user_id})

    def post(self, request, user_id):
        user_data = User.objects.get(id=user_id)
        user_data.save()
        del request.session['id']
        return HttpResponseRedirect('/')


class ChangeDataView(View):
    form_class = ChangeDataForm
    initial = {'key': 'value'}
    template_name = 'change_data_page.html'

    def get(self, request, user_id, data_to_change):

        try:
            if user_id != request.session['id']:
                error = 'Доступ запрещён'
                return render(request, 'error.html', {'error': error})
        except KeyError:
            error = 'Доступ запрещён'
            return render(request, 'error.html', {'error': error})
        user_filter = User.objects.get(id=user_id)
        data_to_change_label = ''
        if data_to_change == 'name':
            data_to_change_label = 'Имя'
        elif data_to_change == 'email':
            data_to_change_label = 'Email'
        elif data_to_change == 'password':
            data_to_change_label = 'Пароль'
        elif data_to_change == 'tg_username':
            data_to_change_label = 'Логин в телеграм'
        elif data_to_change == 'phone_number':
            data_to_change_label = 'Номер телефона'
        data_to_change_filter = getattr(user_filter, data_to_change)
        form = self.form_class(initial=self.initial)

        return render(request, self.template_name, {'data_to_change': data_to_change,
                                                    'data_to_change_label': data_to_change_label, 'form': form,
                                                    'user_filter': user_filter,
                                                    'user_id': user_id, "data_to_change_filter": data_to_change_filter})

    def post(self, request, user_id, data_to_change):
        form = self.form_class(request.POST)
        user_filter = User.objects.get(id=user_id)

        if form.is_valid():
            variable = form.cleaned_data['variable']
            confirmation_variable = form.cleaned_data['confirmation_variable']

            if data_to_change == 'email':
                is_email_existed = User.objects.filter(email=variable).first()
                if is_email_existed:
                    error = 'Пользователь с таким email уже зарегистрирован'
                    return render(request, 'error.html', {'error': error})
                elif not check_email(variable):
                    error = 'Пожалуйста, укажите email в формате example@mail.ru'
                    return render(request, 'error.html', {'error': error})
                else:
                    setattr(user_filter, data_to_change, variable)
                    user_filter.save(update_fields=[f"{data_to_change}", "updated_at"])
                    return HttpResponseRedirect(f'/user_page/{user_id}')
            elif data_to_change == 'password':
                if not password_validate(variable):
                    error = ('Пожалуйста, придумайте надёжный пароль. Требования: не менее восьми символов, '
                             'наличие спецсимволов, а также больших и строчных букв. (Пример: -Secr3t.)')
                    return render(request, 'error.html', {'error': error})
                elif variable == '-Secr3t.':
                    error = 'Пожалуйста, не используйте пароль из примера.'
                    return render(request, 'error.html', {'error': error})
                elif variable != confirmation_variable:
                    error = 'Пароли не совпадают'
                    return render(request, 'error.html', {'error': error})
                elif variable == getattr(user_filter, data_to_change):
                    error = 'Старый и новый пароли совпадают'
                    return render(request, 'error.html', {'error': error})
                else:
                    setattr(user_filter, data_to_change, variable)
                    user_filter.save(update_fields=[f"{data_to_change}", "updated_at"])
                    return HttpResponseRedirect(f'/user_page/{user_id}')
            elif data_to_change == 'tg_username':
                is_tg_username_existed = User.objects.filter(tg_username=variable).first()
                if is_tg_username_existed:
                    error = 'Пользователь с таким телеграм логином уже зарегистрирован'
                    return render(request, 'error.html', {'error': error})
                else:
                    setattr(user_filter, data_to_change, variable)
                    user_filter.save(update_fields=[f"{data_to_change}", "updated_at"])
                    return HttpResponseRedirect(f'/user_page/{user_id}')
            elif data_to_change == 'phone_number':
                is_phone_existed = User.objects.filter(phone_number=variable).first()
                if is_phone_existed:
                    error = 'Пользователь с таким номером телефона уже зарегистрирован'
                    return render(request, 'error.html', {'error': error})
                elif not check_phone_number(variable):
                    error = 'Введите номер телефона в международном формате. (Например, +7 999 999 99 99)'
                    return render(request, 'error.html', {'error': error})
                else:
                    setattr(user_filter, data_to_change, check_phone_number(variable))
                    user_filter.save(update_fields=[f"{data_to_change}", "updated_at"])
                    return HttpResponseRedirect(f'/user_page/{user_id}')
            elif data_to_change == 'name':
                setattr(user_filter, data_to_change, variable)
                user_filter.save(update_fields=[f"{data_to_change}", "updated_at"])
                return HttpResponseRedirect(f'/user_page/{user_id}')
        return render(request, self.template_name, {'form': form})
