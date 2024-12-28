from django.shortcuts import render
from django.views.generic import TemplateView, View


class CatalogPageView(TemplateView):
    template_name = 'catalog_page.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CatalogPageViewById(View):
    template_name = 'catalog_page.html'

    def get(self, request, user_id):

        try:
            if user_id != request.session['id']:
                error = 'Доступ запрещён'
                return render(request, 'error.html', {'error': error})
        except KeyError:
            error = 'Доступ запрещён'
            return render(request, 'error.html', {'error': error})

        return render(request, self.template_name, {"user_id": user_id})
