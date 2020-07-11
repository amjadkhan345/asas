import form as form
import post as post
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, View
#from django.views.generic.base import View

from .forms import usaeupdate, passForm
#from .models import Sher, Asas, Commint


def usar_update(request):
    user = request.user
    form = usaeupdate(instance=user)
    if request.method == 'POST':
        form =usaeupdate(request.POST, instance=user)
        if form.is_valid():
            form =form.save(commit=False)
            form.user=request.user
            form.save()
            return redirect('asas:asas')
    return render(request, 'user_update.html', {'form': form})



