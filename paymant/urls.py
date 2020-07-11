from django.conf.urls import url
from django.urls import path

from .views import (index,
                    charge,
                    successMsg)

app_name = 'paymant'

urlpatterns = [
    path('index/<str:args>', index, name='index'),
    path('charge/<str:args>', charge, name='charge'),
    path('success/<str:args>', successMsg, name='success')
]