from django import forms
from django.core.validators import RegexValidator

from claims.models import Claim


class ClaimForm(forms.ModelForm):

    class Meta:
        model = Claim
        fields = ['name', 'surname', 'booking_reference', 'flight_number', 'email', 'claim', 'attachment']