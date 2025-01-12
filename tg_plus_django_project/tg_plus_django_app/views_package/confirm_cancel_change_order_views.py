import tzlocal
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from config import *
from ..forms import *
from ..models import *


class ConfirmOrderView(View):
    form_class = PaymentForm
    initial = {'key': 'value'}
    template_name = 'confirm_order_page.html'

    def get(self, request, user_id, order_id):
        try:
            if user_id != request.session['id']:
                error = 'Доступ запрещён'
                return render(request, 'error.html', {'error': error})
        except KeyError:
            error = 'Доступ запрещён'
            return render(request, 'error.html', {'error': error})
        form = self.form_class(initial=self.initial)
        user_filter = User.objects.get(id=user_id)
        order_filter = user_filter.orders[f'{order_id}']
        return render(request, self.template_name, {'user_filter': user_filter,
                                                    'order_filter': order_filter,
                                                    'order_id': order_id, 'form': form, 'user_id': user_id, })

    def post(self, request, user_id, order_id):
        form = self.form_class(request.POST)
        user_filter = User.objects.get(id=user_id)

        if form.is_valid():
            card_num = str(form.cleaned_data['card_num'])
            card_date = form.cleaned_data['card_date']
            card_cvc = form.cleaned_data['card_cvc']
            if not is_valid_card_num(card_num):
                error = 'Номер дебетовой банковской карты может состоять из 13, 16, 18 или 19 цифр. Укажите его без пробелов'
                return render(request, 'error.html', {'error': error})
            elif len(str(card_cvc)) != 3:
                error = 'Некорректный трёхзначный код'
                return render(request, 'error.html', {'error': error})
            elif not is_valid_card_date(card_date):
                error = 'Пожалуйста, укажите срок действия карты в формате ГГГГ-ММ (карта должна быть активной)'
                return render(request, 'error.html', {'error': error})
            else:
                card_data = {"card_number": card_num, "card_date": card_date, "card_cvc": card_cvc}
                now = datetime.datetime.now(tzlocal.get_localzone())
                user_filter.orders[f"{order_id}"]["status"] = ["confirmed", "Оплачен"]
                user_filter.orders[f"{order_id}"]["updated_at"] = now.strftime("%Y-%m-%d %H:%M:%S %Z%z")
                user_filter.orders[f"{order_id}"]["card_data"] = card_data
                user_filter.save(update_fields=["orders", "updated_at"])
                return HttpResponseRedirect(f'/user_page/{user_id}')
        return render(request, self.template_name, {'form': form})


class CancelOrderView(View):
    template_name = 'cancel_order_page.html'

    def get(self, request, user_id, order_id):
        try:
            if user_id != request.session['id']:
                error = 'Доступ запрещён'
                return render(request, 'error.html', {'error': error})
        except KeyError:
            error = 'Доступ запрещён'
            return render(request, 'error.html', {'error': error})
        user_filter = User.objects.get(id=user_id)
        now = datetime.datetime.now(tzlocal.get_localzone())
        user_filter.orders[f"{order_id}"]["status"] = ["canceled", "Отменён"]
        user_filter.orders[f"{order_id}"]["updated_at"] = now.strftime("%Y-%m-%d %H:%M:%S %Z%z")
        user_filter.save(update_fields=["orders", "updated_at"])
        return HttpResponseRedirect(f'/user_page/{user_id}')


class ChangeOrderView(View):
    form_class = BuyForm
    initial = {'key': 'value'}
    template_name = 'change_order_page.html'

    def get(self, request, user_id, order_id):
        try:
            if user_id != request.session['id']:
                error = 'Доступ запрещён'
                return render(request, 'error.html', {'error': error})
        except KeyError:
            error = 'Доступ запрещён'
            return render(request, 'error.html', {'error': error})
        form = self.form_class(initial=self.initial)
        user_filter = User.objects.get(id=user_id)
        order_filter = user_filter.orders[f'{order_id}']
        return render(request, self.template_name, {'user_filter': user_filter,
                                                    'order_filter': order_filter,
                                                    'order_id': order_id, 'form': form,
                                                    'user_id': user_id})

    def post(self, request, user_id, order_id):
        form = self.form_class(request.POST)
        user_filter = User.objects.get(id=user_id)
        if form.is_valid():
            product_price = (Product.objects.get(id=user_filter.orders[f"{order_id}"]["product_id"])).price
            product_amount = form.cleaned_data['product_amount']
            now = datetime.datetime.now(tzlocal.get_localzone())
            user_filter.orders[f"{order_id}"]["product_amount"] = product_amount
            user_filter.orders[f"{order_id}"]["product_total"] = round(product_price * product_amount, 2)
            user_filter.orders[f"{order_id}"]["updated_at"] = now.strftime("%Y-%m-%d %H:%M:%S %Z%z")
            user_filter.save(update_fields=["orders", "updated_at"])
            return HttpResponseRedirect(f'/user_page/{user_id}')
        return render(request, self.template_name, {'form': form})
