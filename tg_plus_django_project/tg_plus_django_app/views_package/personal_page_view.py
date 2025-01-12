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
