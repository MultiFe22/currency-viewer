from ast import arg
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json
from .forms import CurrencyForm
from .models import Currency

def index(request, rates=None):
    # # request to https://api.vatcomply.com/rates and get the BRL rate against USD
    # response = requests.get('https://api.vatcomply.com/rates?base=USD')
    # # convert the response to json
    # data = response.json()
    # # get the BRL rate
    # brl_rate = data['rates']['BRL']

    # return HttpResponse(f'1 USD = {brl_rate} BRL')

    # get the value of the input field from the form and redirect to the index page loading the value

    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            currency = form.cleaned_data['currency']
            currency = Currency.objects.filter(name=currency)
            print(currency)
            return render(request, 'currencies/index.html', { 'rates': currency, 'form': form })
    else:
        form = CurrencyForm()
        return render(request, 'currencies/index.html', { 'form': form })

    return render(request, 'currencies/index.html', {'rates': rates})


