from django.shortcuts import render
from django.views.generic import TemplateView, View


class CatalogPageView(TemplateView):
    template_name = 'catalog_page.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CatalogPageViewById(View):
    template_name = 'catalog_page.html'

    def get(self, request, user_id):
        return render(request, self.template_name, {"user_id": user_id})
