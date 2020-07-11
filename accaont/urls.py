from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path

#from .views import post, asasView, commintDetailView
from .views import usar_update

app_name = 'accaont'
urlpatterns = [
    path('usar_update/', usar_update, name='usar_update'),
    #path('password/', passw, name='password'),
    ##path('admin/', admin.site.urls),
    #ath('asas/', asasView, name='asas'),p
    #url(r'commint/$', commint, name='commint'),
    #path('<slug:slug>', commintDetailView.as_view(), name='commint_detail'),
    #url(r'^commints/{?p<slug>[\w-]+}/$', commint, name='commint_with_pk'),
    #url(r'^commint/{?p<pk>\d+}/$', commint, name='commint_with_pk')
    ]



