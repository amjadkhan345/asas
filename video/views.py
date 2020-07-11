from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from .forms import VideoForm
from .models import Video


def video(request):
    form = VideoForm()
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()

    context = {'form': form}
    return render(request, 'asas.html', context)


def videolist(request):
    user = Video.objects.all()
    # object= Video.objects.get()
    context = {'user': user}
    return render(request, 'video_home.html', context)


def acsess(request, pk):
    post= request.user
    user = Video.objects.filter(porm=post).order_by('-id')
    return redirect(reverse, 'paymant:index', args=[user])


def video_fist(request):
    post = request.user.id
    user = Video.objects.filter(porm=post).order_by('-id')
    return render(request, 'video_fist.html', {'user': user})
