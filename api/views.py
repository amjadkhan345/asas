from django.shortcuts import render, redirect
from pprint import pprint

# from utilities import make_request
import hashlib
import base64
import json
import requests
from datetime import datetime
import calendar
import string
from random import *
import hmac
from .rapyd22 import make_request

from django.urls import reverse

idempotency_key = 'aee984befae64'  # Unique for each 'Create Payment' request.

http_method = 'post'  # Lower case.
base_url = 'https://sandboxapi.rapyd.net'
# path = '/v1/data/countries'  # Portion after the base URL.
path = '/v1/payments'
# path = '/v1/checkout'
# salt: randomly generated for each request.
min_char = 8
max_char = 12
allchar = string.ascii_letters + string.punctuation + string.digits
salt = "".join(choice(allchar) for x in range(randint(min_char, max_char)))

# Current Unix time.
d = datetime.utcnow()
timestamp = calendar.timegm(d.utctimetuple())

access_key = '61A18E9C75014C14226B'  # The access key received from Rapyd.
secret_key = '4c69df0562fae551e3562cabb84ffe021bb9e879e47354489cf11cf2af92cf6004f8c6495d4e458b'  # Never transmit the secret key by itself.

body = ''
# JSON body goes here.

to_sign = http_method + path + salt + str(timestamp) + access_key + secret_key + body

h = hmac.new(bytes(secret_key, 'utf-8'), bytes(to_sign, 'utf-8'), hashlib.sha256)

signature = base64.urlsafe_b64encode(str.encode(h.hexdigest()))

url = base_url + path

headers = {
    'access_key': access_key,
    'signature': signature,
    'salt': salt,
    'timestamp': str(timestamp),
    'Content-Type': "application\/json",
    'idempotency': idempotency_key
}

# body = {
#   'amount': 100,
# }
print(url)

r = requests.post(url, data={'receipt_email': 'amjadsh345@gmail.com',  # str(receipt_email),
                             "amount": 99,
                             'payment_method': 'card_fe2e4ae68af029321106c3ac1c0b30de',
                             "currency": "SAR",
                             'show_intermediate_return_page': True,
                             'error_payment_url': 'https://pakpay.herokuapp.com/',
                             'complete_payment_url': 'https://pakpay.herokuapp.com',
                             },
                  headers=headers)
print(r.text)


# print(headers)

def payment(request):
    # users =headers
    if request.method == 'POST':
        amount = request.POST['amount']
        receipt_email = request.POST['receipt_email']
        users = headers
        # amount = request.POST['amount']

        create_payment_body = {
            'receipt_email': str(receipt_email),
            "amount": amount,
            'payment_method': 'card_fe2e4ae68af029321106c3ac1c0b30de',
            "currency": "SAR",
            'country': 'SA',
            "payment_method_type": "sg_grabpay_ewallet",

            'show_intermediate_return_page': True,
            'error_payment_url': 'https://pakpay.herokuapp.com/',
            'complete_payment_url': 'https://pakpay.herokuapp.com',
        }
        
        url1 = 'https://sandboxapi.rapyd.net/v1/payments'
        # response = requests.post(url, data=body1, headers=headers)

        #               data=create_payment_body)
        # pprint(response)
        
        response = make_request(method='post',
                                path='/v1/payments',

                                body=create_payment_body)
        print(response)

        # return render(request, 'rapydsub.html', {'users': users, 'body': body1})
        # from django.urls import reverse
        #re = requests.post(url, headers=users, data=body1)
        #print(re)

    return render(request, 'bail.html')


def index(request, user, body2):
    users = user
    body1 = body2


    create_payment_body = {
            "amount": 100,
            "currency": "USD",
            "description": "Payment by card token",
            "payment_method": "card_fe2e4ae68af029321106c3ac1c0b30de",
            "metadata": {
                "merchant_defined": True
            }
        }
    response = make_request(method='post',
                                path='/v1/payments',

                                body=create_payment_body)
    pprint(response)

    return render(request, 'rapydsub.html', {'users': users, 'body': body1})

# Create your views here.
