from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['address', 'contry', 'image',  'mobil', ]
        exclude = ['user']
