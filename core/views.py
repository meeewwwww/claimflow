from django.shortcuts import render
from django.views.generic import TemplateView


title = 'ClaimFlow - Система урегулирования претензий'


class MainPage(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = title
        return context