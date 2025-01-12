import json

import tzlocal
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from config import *
from ..forms import *
from ..models import *


class ProductPageView(View):
    template_name = 'product_page.html'

    def get(self, request, category_name, product_id):
        product_filter = Product.objects.filter(category__0=category_name, id=product_id)
        return render(request, self.template_name,
                      {"product_filter": product_filter, "category_name": category_name,
                       "product_id": product_id})


class ProductPageViewById(View):
    form_class = BuyForm
    initial = {'key': 'value'}
    template_name = 'product_page.html'

    def get(self, request, user_id, category_name, product_id):
        try:
            if user_id != request.session['id']:
                error = 'Доступ запрещён'
                return render(request, 'error.html', {'error': error})
        except KeyError:
            error = 'Доступ запрещён'
            return render(request, 'error.html', {'error': error})
        product_filter = Product.objects.filter(category__0=category_name, id=product_id)
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name,
                      {"user_id": user_id, "product_filter": product_filter, "category_name": category_name,
                       "product_id": product_id, 'form': form})

    def post(self, request, user_id, category_name, product_id):
        form = self.form_class(request.POST)
        product_filter = Product.objects.filter(category__0=category_name, id=product_id)
        user_filter = User.objects.get(id=user_id)
        if form.is_valid():
            product_amount = form.cleaned_data['product_amount']
            if not user_filter.orders:
                now = datetime.datetime.now(tzlocal.get_localzone())
                user_filter.orders = {1: {"product_name": list(product.name[1] for product in product_filter)[0],
                                          "product_amount": product_amount,
                                          "product_total":
                                              list(product.price for product in product_filter)[0] * product_amount,
                                          "status": ["ordered", "Оформлен"],
                                          "updated_at": now.strftime("%Y-%m-%d %H:%M:%S %Z%z"),
                                          "card_data": None}}
                user_filter.save(update_fields=["orders"])
                return redirect(request.path)
            else:
                now = datetime.datetime.now(tzlocal.get_localzone())
                user_filter.orders = (user_filter.orders |
                                      {int(max(user_filter.orders, key=int)) + 1:
                                           {"product_name": list(product.name[1] for product in product_filter)[0],
                                            "product_amount": product_amount,
                                            "product_total":
                                                list(product.price for product in product_filter)[0] * product_amount,
                                            "status": ["ordered", "Оформлен"],
                                            "updated_at": now.strftime("%Y-%m-%d %H:%M:%S %Z%z"),
                                            "card_data": None}})
                user_filter.save(update_fields=["orders"])
                return redirect(request.path)
        return render(request, self.template_name, {'form': form})
