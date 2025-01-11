from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from config import *
from ..forms import *
from ..models import *


class RateOrderView(View):
    form_class = RatingForm
    initial = {'key': 'value'}
    template_name = 'rate_order_page.html'

    def get(self, request, user_id, order_id_to_rate):
        try:
            if user_id != request.session['id']:
                error = 'Доступ запрещён'
                return render(request, 'error.html', {'error': error})
        except KeyError:
            error = 'Доступ запрещён'
            return render(request, 'error.html', {'error': error})

        form = self.form_class(initial=self.initial)
        user_filter = User.objects.values().filter(id=user_id)
        user_order_to_rate = ''
        for _ in user_filter:
            user_order_to_rate = _['orders'][f'{order_id_to_rate}']
        return render(request, self.template_name, {'user_filter': user_filter,
                                                    'user_order_to_rate': user_order_to_rate,
                                                    'order_id_to_rate': order_id_to_rate, 'form': form,
                                                    'user_id': user_id, })
