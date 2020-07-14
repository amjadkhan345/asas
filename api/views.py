from django.shortcuts import render
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

idempotency_key = 'aee984befae64'  # Unique for each 'Create Payment' request.

http_method = 'post'  # Lower case.
base_url = 'https://sandboxapi.rapyd.net'
# path = '/v1/data/countries'  # Portion after the base URL.
path = '/v1/payments'
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
# print(url)

# r = requests.post(url, data={"amount": 99,
#                           },
#                headers=headers)
# print(r.text)
# print(headers)

def payment(request):
    # user =headers
    if request.method == 'POST':
        amount = request.POST['amount']
        receipt_email = request.POST['receipt_email']
        # amount = request.POST['amount']

        body1 = {
            #'receipt_email': str(receipt_email),
            "amount": amount,
            #'payment_method': 'card_fe2e4ae68af029321106c3ac1c0b30de',
            "currency": "SAR",
            'country': 'SA',
            'error_payment_url': 'https://pakpay.herokuapp.com/',
            'complete_payment_url': 'https://pakpay.herokuapp.com',
            'show_intermediate_return_page': True,
        }
        url1 = 'https://sandboxapi.rapyd.net/v1/payments'
        response = requests.post(url, data=body1, headers=headers)

        #               data=create_payment_body)
        pprint(response)

    # return render(request, 'rapydsub.html', {'user': user, 'body': body})

    return render(request, 'bail.html')

# Create your views here.
