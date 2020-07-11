from django.urls import path

from .views import (video,
                    videolist,
                    acsess, video_fist)

app_name = 'video'

urlpatterns = [
    path('', videolist, name='video_list'),
    path('video/', video, name='video'),
    path('acsess/<str:args>', acsess, name='acsess'),
    path('video_fist/', video_fist, name='video_fist')

]
