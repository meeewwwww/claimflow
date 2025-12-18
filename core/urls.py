from django.urls import path

from core.views import MainPage

urlpatterns = [
    path('', MainPage.as_view(), name='start-page'),
]