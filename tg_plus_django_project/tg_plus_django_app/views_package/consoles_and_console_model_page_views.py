from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, TemplateView
from config import *
from ..forms import *
from ..models import *


class ConsolesPageView(TemplateView):
    template_name = 'cat_pages/cons_page.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ConsolesPageViewById(View):
    template_name = 'cat_pages/cons_page.html'

    def get(self, request, user_id):

        try:
            if user_id != request.session['id']:
                error = 'Доступ запрещён'
                return render(request, 'error.html', {'error': error})
        except KeyError:
            error = 'Доступ запрещён'

            return render(request, 'error.html', {'error': error})
        return render(request, self.template_name, {"user_id": user_id, })


class ConsoleModelPageView(View):
    template_name = 'cat_pages/cons_model_page.html'

    def get(self, request, console_model):
        product_filter = Product.objects.values().get(name=console_model)

        return render(request, self.template_name, {'product_filter': product_filter})


class ConsoleModelPageViewById(View):
    form_class = BuyForm
    initial = {'key': 'value'}
    template_name = 'cat_pages/cons_model_page.html'

    def get(self, request, user_id, console_model):

        try:
            if user_id != request.session['id']:
                error = 'Доступ запрещён'
                return render(request, 'error.html', {'error': error})
        except KeyError:
            error = 'Доступ запрещён'
            return render(request, 'error.html', {'error': error})

        form = self.form_class(initial=self.initial)

        product_filter = Product.objects.values().get(model_name=console_model)

        return render(request, self.template_name,
                      {'product_filter': product_filter, 'user_id': user_id, 'form': form, })

    def post(self, request, user_id, console_model):
        form = self.form_class(request.POST)
        product_filter = Product.objects.values().get(model_name=console_model)

        user_filter = User.objects.values().get(id=user_id)

        if form.is_valid():
            product_amount = form.cleaned_data['product_amount']

            if user_filter['orders'] is not None:
                User.objects.filter(id=user_id).update(orders=user_filter['orders'] | {
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
                User.objects.filter(id=user_id).update(orders={f'{1}': {"model_name": console_model,
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

            return HttpResponseRedirect(f'/console_page/{user_id}/{console_model}')

        return render(request, self.template_name, {'form': form})
