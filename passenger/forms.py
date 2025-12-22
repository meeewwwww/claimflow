from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

from claims.models import Claim


class ClaimForm(forms.ModelForm):

    class Meta:
        model = Claim
        fields = ['name', 'surname', 'booking_reference', 'flight_number', 'email', 'claim', 'attachment']