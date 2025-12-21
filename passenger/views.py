from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from claims.models import Claim
from core.models import Flight
from core.services import DelayCalculator
from core.utils import DefaultDataMixin
from passenger.forms import ClaimForm


class SendClaim(DefaultDataMixin, FormView):
    template_name = 'passenger/send_claim.html'
    success_url = reverse_lazy('passenger:success_send_claim')
    form_class = ClaimForm

    def form_valid(self, form):
        form.save()
        flight_obj = form.cleaned_data['flight_number']
        flight_obj.time_of_delay = DelayCalculator.calculate_delay_time(flight_obj)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        for item in self.additional_data:
            context[item] = self.additional_data[item]
        flights = Flight.objects.all()
        context['flights'] = flights
        context['title'] = 'ClaimFlow - Подача претензии'
        return context

    def get_success_url(self):
        booking_reference = self.request.POST['booking_reference']
        success_url = reverse_lazy('passenger:success_send_claim', kwargs={'booking_reference': booking_reference})
        return success_url


class SendClaimSuccess(DefaultDataMixin, TemplateView):
    template_name = 'passenger/send_claim_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for item in self.additional_data:
            context[item] = self.additional_data[item]
        booking_reference = context['booking_reference']
        flight_object = Claim.objects.get(booking_reference=booking_reference).flight_number
        context['time_of_delay'] = flight_object.time_of_delay
        context['compensation'] = DelayCalculator.calculate_delay_compensation(flight_object)
        return super().get_context_data(**context)


class SendClaimFail(DefaultDataMixin, TemplateView):
    template_name = 'passenger/send_claim_fail.html'