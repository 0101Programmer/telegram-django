from django.shortcuts import render
from django.views.generic import TemplateView

from ..models import *


class HomePage(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        is_active = User.objects.filter(is_active__exact=True)
        return render(request, self.template_name, {'is_active': is_active})