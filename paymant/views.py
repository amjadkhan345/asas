from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse

import stripe

from video.models import Video, Friend

# from book.video.models import Friend

stripe.api_key = 'sk_test_lkFOf1f91VZtgv1woFSMBRoc00ARDo4vDQ'


def index(request, args):
    #post = Video.objects.get(pk=args)
    user = Video.objects.filter(id=args).order_by('-id')
    context = {'user': user}
    return render(request, 'chek.html', context)


def charge(request, args):
    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            source=request.POST['stripeToken']
        )
        stripe.Charge.create(
            customer=customer,
            amount=amount * 100,
            currency='usd',
            description='Donation',
        )
        post = get_object_or_404(Video, id=args)
        post.porm.add(request.user)
        # post = get_object_or_404(Video, id=request.POST.get('post_id'))
        return redirect(reverse('paymant:success', args=[amount]))


def successMsg(request, args):
    # user = args
    amount = args

    # hi= args
    # hi.porm.add(user)
    return render(request, 'success.html', {'amount': amount})
