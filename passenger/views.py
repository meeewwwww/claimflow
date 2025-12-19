from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from core.utils import DefaultDataMixin
from employee.models import Flight
from passenger.forms import ClaimForm


class SendClaim(DefaultDataMixin, FormView):
    template_name = 'passenger/send_claim.html'
    success_url = reverse_lazy('passenger:success_send_claim')
    form_class = ClaimForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        for item in self.additional_data:
            context[item] = self.additional_data[item]
        flights = Flight.objects.all()
        context['flights'] = flights
        return context


class SendClaimSuccess(TemplateView):
    template_name = 'passenger/send_claim_success.html'


class SendClaimFail(TemplateView):
    template_name = 'passenger/send_claim_fail.html'