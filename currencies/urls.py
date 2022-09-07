from django.urls import path

from . import views

app_name = 'currencies'

urlpatterns = [
    path('', views.index, name='index'),
    path('currency/<str:currency>', views.get_currency, name='get_currency'),
]