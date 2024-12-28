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
        return render(request, self.template_name, {"user_id": user_id})
