import tzlocal
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

    def get(self, request, user_id, order_id):
        try:
            if user_id != request.session['id']:
                error = 'Доступ запрещён'
                return render(request, 'error.html', {'error': error})
        except KeyError:
            error = 'Доступ запрещён'
            return render(request, 'error.html', {'error': error})
        form = self.form_class(initial=self.initial)
        user_filter = User.objects.get(id=user_id)
        order_filter = user_filter.orders[f'{order_id}']
        return render(request, self.template_name, {'user_filter': user_filter,
                                                    'order_filter': order_filter,
                                                    'order_id': order_id, 'form': form,
                                                    'user_id': user_id})

    def post(self, request, user_id, order_id):
        form = self.form_class(request.POST)
        user_filter = User.objects.get(id=user_id)
        product_filter = Product.objects.get(id=user_filter.orders[f"{order_id}"]["product_id"])
        if form.is_valid():
            rating = int(form.cleaned_data['rating'])
            review = form.cleaned_data['review']
            if not product_filter.ratings:
                now = datetime.datetime.now(tzlocal.get_localzone())
                product_filter.ratings = {
                    "reviews": {
                        1: {
                            "rating": rating,
                            "review": review,
                            "created_at": now.strftime("%Y-%m-%d %H:%M:%S"),
                            "created_by": user_filter.name,
                            "user_id": user_filter.id,
                        }},
                    "total_rating": {}
                }
                product_filter.ratings["total_rating"]["total_reviews"] = len(product_filter.ratings["reviews"])
                product_filter.ratings["total_rating"]["ratings_sum"] = (
                    sum([v["rating"] for k, v in product_filter.ratings["reviews"].items()]))
                product_filter.ratings["total_rating"]["average_rating"] = (
                        sum([v["rating"] for k, v in product_filter.ratings["reviews"].items()]) /
                        len(product_filter.ratings["reviews"]))
            else:
                now = datetime.datetime.now(tzlocal.get_localzone())
                product_filter.ratings["reviews"][(int(max(product_filter.ratings["reviews"], key=int)) + 1)] = \
                    {
                            "rating": rating,
                            "review": review,
                            "created_at": now.strftime("%Y-%m-%d %H:%M:%S"),
                            "created_by": user_filter.name,
                            "user_id": user_filter.id,
                        }
                product_filter.ratings["total_rating"]["total_reviews"] = len(product_filter.ratings["reviews"])
                product_filter.ratings["total_rating"]["ratings_sum"] = (
                    sum([v["rating"] for k, v in product_filter.ratings["reviews"].items()]))
                product_filter.ratings["total_rating"]["average_rating"] = (
                        sum([v["rating"] for k, v in product_filter.ratings["reviews"].items()]) /
                        len(product_filter.ratings["reviews"]))
            user_filter.orders[f"{order_id}"]["is_rated"] = True
            user_filter.save(update_fields=["orders", "updated_at"])
            product_filter.save(update_fields=["ratings"])
            return HttpResponseRedirect(f'/user_page/{user_id}')

        return render(request, self.template_name, {'form': form})
