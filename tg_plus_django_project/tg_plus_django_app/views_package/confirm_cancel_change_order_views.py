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

    def get(self, request, user_id, order_id_to_change):
        form = self.form_class(initial=self.initial)
        active_user_filter = User.objects.values().filter(id=user_id)
        active_user_order_to_change = ''

        for _ in active_user_filter:
            active_user_order_to_change = _['orders'][f'{order_id_to_change}']

        return render(request, self.template_name, {'active_user_filter': active_user_filter,
                                                    'active_user_order_to_change': active_user_order_to_change,
                                                    'order_id_to_change': order_id_to_change, 'form': form, 'user_id': user_id, })

    def post(self, request, user_id, order_id_to_change):
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
                user_filter = User.objects.values().get(id=user_id)

                User.objects.filter(id=user_id).update(orders=user_filter['orders'] |
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
                                                                                                    "paid_by": {
                                                                                                        "card_num": card_num,
                                                                                                        "card_date": card_date,
                                                                                                        "card_cvc": card_cvc}, }})

                return HttpResponseRedirect(f'/user_page/{user_id}')

        return render(request, self.template_name, {'form': form})


class CancelOrderView(View):
    template_name = 'cancel_order_page.html'

    def get(self, request, user_id, order_id_to_change):
        user_filter = User.objects.values().get(is_active=True)

        User.objects.filter(id=user_id).update(orders=user_filter['orders'] |
                                                                 {f'{order_id_to_change}': {"model_name":
                                                                                                user_filter['orders'][
                                                                                                    f'{order_id_to_change}'][
                                                                                                    'model_name'],
                                                                                            "model_name_for_client":
                                                                                                user_filter['orders'][
                                                                                                    f'{order_id_to_change}'][
                                                                                                    'model_name_for_client'],
                                                                                            "product_amount":
                                                                                                user_filter['orders'][
                                                                                                    f'{order_id_to_change}'][
                                                                                                    'product_amount'],
                                                                                            "product_price":
                                                                                                user_filter['orders'][
                                                                                                    f'{order_id_to_change}'][
                                                                                                    'product_price'],
                                                                                            "updated_at": datetime.datetime.now().astimezone().strftime(
                                                                                                "%Y-%m-%d | %H:%M:%S %z | %Z"),
                                                                                            "status": "canceled",
                                                                                            "total":
                                                                                                user_filter['orders'][
                                                                                                    f'{order_id_to_change}'][
                                                                                                    'total'], }})

        return HttpResponseRedirect(f'/user_page/{user_id}')


class ChangeOrderView(View):
    form_class = BuyForm
    initial = {'key': 'value'}
    template_name = 'change_order_page.html'

    def get(self, request, user_id,  order_id_to_change):
        form = self.form_class(initial=self.initial)
        active_user_filter = User.objects.values().filter(id=user_id)
        active_user_order_to_change = ''

        for _ in active_user_filter:
            active_user_order_to_change = _['orders'][f'{order_id_to_change}']

        return render(request, self.template_name, {'active_user_filter': active_user_filter,
                                                    'active_user_order_to_change': active_user_order_to_change,
                                                    'order_id_to_change': order_id_to_change, 'form': form, 'user_id': user_id, })

    def post(self, request, user_id, order_id_to_change):
        form = self.form_class(request.POST)

        if form.is_valid():
            product_amount = form.cleaned_data['product_amount']
            user_filter = User.objects.values().get(is_active=True)

            User.objects.filter(id=user_id).update(orders=user_filter['orders'] |
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
            return HttpResponseRedirect(f'/user_page/{user_id}')

        return render(request, self.template_name, {'form': form})
