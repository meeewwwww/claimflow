from django import forms

from claims.models import Claim


class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['name', 'surname', 'booking_reference', 'flight_number', 'email', 'claim', 'attachment']