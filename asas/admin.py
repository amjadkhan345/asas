from django.contrib import admin

# Register your models here.
from .models import Asas, Commint, Friend, Like_post, Book, Post, add_book

admin.site.register(Asas)

admin.site.register(Commint)
admin.site.register(Friend)
admin.site.register(Like_post)
admin.site.register(Book)
admin.site.register(Post)
admin.site.register(add_book)
