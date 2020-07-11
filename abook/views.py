# Create your views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
#from .asas.models import Friend


@login_required(login_url='login')
def add_profile(request):
    # post = Profile.objects.get(id=pk_test)
    form = ProfileForm()
    # Profile= request.user
    if Profile.objects.filter(user_id=request.user.id).exists():
        return redirect('profile')
    else:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES,)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
            return redirect('asas:asas')
    context = {'form': form}
    return render(request, 'add_profile.html', context)


@login_required(login_url='login')
def view_profile(request):
    #post = Profile.objects.get(id=pk_test)
    # users= Profile.objects.all()
    # context={'users': users}
    return render(request, 'view_profile.html', {})

@login_required(login_url='login')
def profile(request, pk_test):
    post = Profile.objects.get(id=pk_test)
    return render(request, 'view_profile.html', {'posts': post})


@login_required(login_url='login')
def edit_profile(request):
    user = Profile.objects.all()
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    # form= ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'frofile.html', {'users': user, 'form': form})





def regaster(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        farst_name = request.POST['farst name']
        last_name = request.POST['last name']
        x = User.objects.create_user(username=username, email=email, password=password, first_name=farst_name,
                                     last_name=last_name)
        x.save()
        messages.info(request, 'grate')
        return redirect('login')
    else:
        return render(request, 'regaster.html', {'titles': 'home page'})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = auth.authenticate(username=username, password=password)

        if User is not None:
            auth.login(request, User)

            messages.info(request, 'wallcome')
            return redirect('asas:asas')

        else:
            messages.info(request, 'possward rong')
            return redirect('login')

    else:
        # messages.info(request, 'rong possward')
        return render(request, 'login.html', {'title': 'loge in page title'})


@login_required(login_url='login')
def abut(request):
    return render(request, 'abut.html', {'title': 'abut page'})


def reg(request):
    if request.method == 'POST':
        username = request.POST['username'],
        email = request.POST['email'],
        password1 = request.POST['password1'],
        # firstname = request.POST['first name'],
        # lastname = request.POST['last name']
        password2 = request.POST['password2'],
        x = User.objects.create_user(username=username, email=email, password1=password1, password2=password2, )
        # first_name=firstname, last_name=lastname)
        x.save()
    return render(request, 'reg.html', {})


def logout(request):
    auth.logout(request)
    return redirect('asas:asas')

# @login_required(login_url='login')
# def post(request):
# if request.method == 'POST':
# data = Sher(
# image=request.POST['image'],
# title=request.POST['title'],

# )
# data.save()

# return redirect('/frofile/')
# cnt = Sher.objects.all()

# return render(request, 'post.html', {'rows': cnt})
