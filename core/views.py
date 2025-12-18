from django.shortcuts import render
from django.views.generic import TemplateView

from core.utils import DefaultDataMixin


class MainPage(DefaultDataMixin, TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        for item in self.additional_data:
            context[item] = self.additional_data[item]
        return context


# Создать шаблон
class About(DefaultDataMixin, TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        for item in self.additional_data:
            context[item] = self.additional_data[item]
        return context


# Создать шаблон
class Contacts(DefaultDataMixin, TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        for item in self.additional_data:
            context[item] = self.additional_data[item]
        return context