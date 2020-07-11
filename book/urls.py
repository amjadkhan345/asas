"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# noinspection PyUnresolvedReferences
from abook.views import login, regaster, abut, reg, logout, view_profile, add_profile, edit_profile, profile

#from abook.views import view_profile, add_profile, edit_profile

urlpatterns = [
    #path('post/', post, name='post'),

    path('abut/', abut, name='abut'),
    path('login/', login, name='login'),
    path('regaster/', regaster, name='regaster'),
    path('admin/', admin.site.urls),
    path("reg/", reg, name="reg"),
    path('logout/', logout, name='logout'),
    path('accaont/', include('accaont.urls', namespace='accaont')),
    path('profile/', view_profile, name='profile'),
    #url(r'^frofile/{?p<pk>\d+}/$', frofile, name='frofile_with_pk')
    path('', include('asas.urls', namespace='asas')),
    path('profile/<str:pk_test>', profile, name='find_profiles'),
    path('add_profile/', add_profile, name='add_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('paymant/', include('paymant.urls', namespace='paymant')),
    path('shopping_cart/', include('memberships.urls', namespace='shopping_cart')),
    #path('courses/', include('courses.urls', namespace='courses')),
    path('video/', include('video.urls', namespace='video')),
    path('api/', include('api.urls', namespace='api')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
