from django.urls import path

from passenger.views import SendClaim, SendClaimSuccess, SendClaimFail


app_name = 'passenger'

urlpatterns = [
    path('send_claim/', SendClaim.as_view(), name='send_claim'),
    path('success/<str:booking_reference>/', SendClaimSuccess.as_view(), name='success_send_claim'),
    path('fail/', SendClaimFail.as_view(), name='fail_send_claim'),
]