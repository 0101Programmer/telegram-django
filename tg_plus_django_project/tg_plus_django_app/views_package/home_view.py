from django.shortcuts import render
from django.views.generic import TemplateView, View

from ..models import *


class HomePage(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


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
        return render(request, self.template_name, {"user_id": user_id})
