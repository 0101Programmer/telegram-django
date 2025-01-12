from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, TemplateView
from config import *
from ..forms import *
from ..models import *


class CategoryPageView(View):
    template_name = 'category_page.html'

    def get(self, request, category_name):
        category_filter = Product.objects.filter(category__0=category_name)
        return render(request, self.template_name,
                      {"category_filter": category_filter, "category_name": category_name})


class CategoryPageViewById(View):
    template_name = 'category_page.html'

    def get(self, request, user_id, category_name):
        try:
            if user_id != request.session['id']:
                error = 'Доступ запрещён'
                return render(request, 'error.html', {'error': error})
        except KeyError:
            error = 'Доступ запрещён'
            return render(request, 'error.html', {'error': error})

        category_filter = Product.objects.filter(category__0=category_name)

        return render(request, self.template_name,
                      {"user_id": user_id, "category_filter": category_filter, "category_name": category_name})
