from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path

from .views import asas, deta, commint, change_friend, home, friend_like, like_post, delete, view_friend, sher, book, \
    post, book_home, add_page, book_list, pages_detal

app_name = 'asas'
urlpatterns = [
    path('', asas, name='asas'),
    path('deta/', deta, name='deta'),
    path('home/', home, name='home'),
    path('commint/', commint, name='commints'),
    path('admin/', admin.site.urls),
    path('commints/<str:pk_test>', commint, name='commint'),
    path('connect/<str:operation>/<str:pk>', change_friend, name='change_friend'),
    path('like/<str:operation>/<str:pk>', friend_like, name='friend_like'),
    path('delete/<str:pk>', delete, name='delete_comment'),
    path('likes/', like_post, name='like_post'),
    path('view_friend/', view_friend, name='view_friend'),
    path('share/', book, name='share'),
    path('page/<str:pk>', post, name='page'),
    path('book/', book_home, name='book'),
    path('add_page1/<str:pk>', post, name='add_page1'),
    path('add_page/<str:operation>/<str:pk>', add_page, name='add_page'),
    path('book_list/', book_list, name='book_list'),
    path('pages_detal/<str:pk>', pages_detal, name='pages_detal'),
    #path('add_pa/', add_pa, name='add_pa')
    # url(r'^commint/{<slug:post>}/$', commint, name='commint'),

]
