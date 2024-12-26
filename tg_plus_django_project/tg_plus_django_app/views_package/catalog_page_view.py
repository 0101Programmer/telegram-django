from django.shortcuts import render
from django.views.generic import TemplateView


class CatalogPageView(TemplateView):
    template_name = 'catalog_page.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)