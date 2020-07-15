from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('', views.payment, name='payment'),
    path(hallo/, views.makepayment, name= 'hallo'
    ]
