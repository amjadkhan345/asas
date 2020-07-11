from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.urls import reverse


class Asas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL, related_name='parant')
    # slug = models.SlugField(unique=True, null=False)
    likes = models.ManyToManyField(User, related_name='likes')
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='pro')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # @classmethod
    # def Sher(cls, new_friend):
    # friend, created = cls.objects.get_or_create()
    # friend.user.add(new_friend)

    def retweet(self):
        return self.parent

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['image', ]

    def totel_like(self):
        return self.likes.count()

    @staticmethod
    def get_absolute_url():
        return reverse("asas:commints")


class Commint(models.Model):
    commint = models.TextField()
    # slug = models.SlugField(unique=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Asas, on_delete=models.CASCADE, related_name='commint', null=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created', ]

    def __str__(self):
        return self.commint

    def totel(self):
        return self.user.count(self)

    def get_absolute_url(self):
        return reverse("asas:commints")


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.remove(new_friend)

    def totel_friends(self):
        return self.current_user.count()


class Like_post(models.Model):
    post = models.ManyToManyField(Asas)
    current_post = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mysate', null=True)

    @classmethod
    def mike_like(cls, current_post, new_post):
        like, created = cls.objects.get_or_create(current_post=current_post)
        like.post.add(new_post)

    @classmethod
    def lose_like(cls, current_post, new_post):
        like, created = cls.objects.get_or_create(current_post=current_post)
        like.post.remove(new_post)

    def totel(self):
        return self.current_post.count()


class Post(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.TextField(null=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=True)
    image= models.ImageField(null=True, blank=True, upload_to='file')
    #page = models.TextField(null=True, max_length=100)
    lion = models.ManyToManyField('self')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name

class add_book(models.Model):
    page=models.TextField(null=True,)
    lion=models.ForeignKey(Book, on_delete=models.CASCADE)

    @classmethod
    def make_book(cls, lion, new_page):
        page_book, created = cls.objects.get_or_create(lion=lion)
        page_book.most.add(new_page)





