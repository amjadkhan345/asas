from django import forms
from django.db.models import TextField
from django.forms import ComboField, CharField
from .models import Asas, Commint, Book, Post, add_book


class SherForm(forms.ModelForm):
    class Meta:
        model = Asas
        fields = ['image', 'title', ]
        exclude = ['user']


class CommintForm(forms.ModelForm):
    class Meta:
        model = Commint
        fields = ['commint', ]
        exclude = ['user']


class BookForm(forms.ModelForm):
    # page=forms.CharFiel(max_length=5000)

    class Meta:
        model = Book
        fields = ['name', 'image', 'price',]
        exclude = ['user']
        extand = ['page', ]


class PostForm(forms.ModelForm):
    # most = ComboField(fields={Charfield(null=True, max_length=75)})
    #most = ComboField(fields=[TextField(max_length=75)])

    class Meta:
        model = add_book
        fields = ['page', ]
        exclude = ['user']
