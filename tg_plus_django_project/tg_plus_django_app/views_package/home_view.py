from django.shortcuts import render
from django.views.generic import TemplateView, View

from ..models import *


class HomePage(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        all_products_data = Product.objects.all()
        return render(request, self.template_name, {"all_products_data": all_products_data})


class HomePageById(View):
    template_name = 'home.html'

    def get(self, request, user_id):
        try:
            if user_id != request.session['id']:
                error = 'Доступ запрещён'
                return render(request, 'error.html', {'error': error})
        except KeyError:
            error = 'Доступ запрещён'
            return render(request, 'error.html', {'error': error})

        all_products_data = Product.objects.all()
        return render(request, self.template_name, {"user_id": user_id, "all_products_data": all_products_data})
