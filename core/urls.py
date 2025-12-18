from django.urls import path

from core.views import MainPage

urlpatterns = [
    path('', MainPage.as_view(), name='start_page'),
    path('about/', MainPage.as_view(), name='about'),
    path('contacts/', MainPage.as_view(), name='contacts'),
]