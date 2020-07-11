from django import forms

#from .models import Asas, Commint
from django.contrib.auth.models import User

class usaeupdate(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', ]
        exclude = ['user']


class passForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['password', ]
        exclude = ['User']



