# import keyword
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
# Create your views here.
from django.views.generic import View
#from paymant.models import Order
from .forms import SherForm, CommintForm, BookForm, PostForm
from .models import Asas, Commint, Friend, Like_post, Book, Post, add_book
from .decorators import unauthenticated_user, allowed_users, admin_only
from memberships.models import Order


@login_required(login_url='login')
def asas(request, pk=None):
    user = Asas.objects.all()
    args = {'users': user, 'totel': Asas.totel_like}

    return render(request, 'reg.html', args)


@login_required(login_url='login')
def deta(request):
    user = request.user
    form = SherForm
    if request.method == 'POST':
        form = SherForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/')
    return render(request, 'post.html', {'form': form})


@login_required(login_url='login')
def commint(request, pk_test):
    post = Asas.objects.get(pk=pk_test)

    # order=asas.commint.order_set.all()
    # commint= Commint.count()
    user = Commint.objects.filter(post=post).order_by('-id')
    form = CommintForm()
    if request.method == 'POST':
        form = CommintForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = post
            form.save()
            return redirect('asas:asas')
    context = {'form': form, 'users': user, 'post': post,
               'commints': commint, 'totels': Commint.totel}
    return render(request, 'commint.html', context)

@login_required(login_url='login')
def change_friend(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
        # return redirect('asas:asas')
    if operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('asas:home')


# else:
# return redirect('asas:asas')


@login_required(login_url='login')
def home(request):
    users = User.objects.exclude(id=request.user.id)
    friend = Friend.objects.get(current_user=request.user)
    friend = friend.users.all()
    return render(request, 'home.html',
                  {'titles': 'home page', 'users': users, 'friends': friend, 'totel': Friend.totel_friends})

@login_required(login_url='login')
def friend_like(request, operation, pk):
    friend = Asas.objects.get(pk=pk)
    if friend is None:
        pass
    if operation == 'add':
        Like_post.mike_like(request.user.id, friend)
        # return redirect('asas:asas')

    if operation == 'remove':
        Like_post.lose_like(request.user, friend)
    return redirect('asas:asas')

@login_required(login_url='login')
def like_post(request):
    users = User.objects.exclude(id=request.user.id)
    friend = Friend.objects.get(current_user=request.user)
    friend = friend.users.all()
    # user= Asas.objects.all()
    post = get_object_or_404(Asas, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect('/')

@login_required(login_url='login')
def delete(request, pk):
    order = Commint.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('asas:asas')

@login_required(login_url='login')
def view_friend(request):
    users = User.objects.exclude(id=request.user.id)
    friend = Friend.objects.get(current_user=request.user)
    friend = friend.users.all()
    return render(request, 'abut.html', {'titles': 'home page', 'users': users, 'friends': friend})

@login_required(login_url='login')
def sher(request, pk):
    user = Asas.objects.get(pk=pk)
    return render(request, 'share.html', {'users': user})

@login_required(login_url='login')
def book(request):
    form= BookForm
    if request.method == 'POST':
        form=BookForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            #group = Group.objects.get(name='user')
            #form.groups.add(group)

            #messages.success(request, 'Account was created for ' + username)

        return redirect('asas:asas')
    return render(request, 'share.html', {'form': form})

@login_required(login_url='login')
def post(request, pk):
    form= PostForm()
    lion= Book.objects.get(pk=pk)
    user = Book.objects.filter(lion=lion).order_by('-id')
    if request.method == 'POST':
        form= PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.lion= lion
            form.save()
    return render(request, 'page.html', {'form': form, 'user': user, 'lion': lion})


@login_required(login_url='login')
#@allowed_users(allowed_roles=['user'])
def book_home(request):
    post = request.user.id
    user = Book.objects.filter(id=post).order_by('-id')
    args= {'user': user}
    return render(request, 'book_home.html', args)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_page(request, operation, pk):
    friend = Book.objects.get(pk=pk)
    #user = get_object_or_404(Post, id=request.POST.get('post_id'))

    if operation == 'add':
        add_book.make_book(request.user.form, friend)
    return redirect('/')

@login_required(login_url='login')
def book_list(request):
    user= Book.objects.all()
    context={'user': user}
    return render(request, 'book_list.html', context)


@login_required(login_url='login')
def pages_detal(request, pk):
    lion= Book.objects.get(pk=pk)
    user = add_book.objects.filter(lion=lion).order_by('-id')
    args= {'users': user, 'lion': lion}
    return render(request, 'pages_detal.html', args)




