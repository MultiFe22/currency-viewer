from ast import arg
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json
from .forms import CurrencyForm
from .models import Currency
import datetime

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
            
            # with start and end date from the form, generate a list of all days between them including the start and end dates
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            date_list = [start_date + datetime.timedelta(days=x) for x in range((end_date-start_date).days + 1)]
            print(date_list)
            # for each day in the list, check if the currency is already in the database
            for date in date_list:
                if Currency.objects.filter(name=currency, date=date).exists():
                    # if it is, do nothing
                    pass
                else:
                    # if it isn't, get the currency value from the API and save it to the database
                    print (f'Getting {currency} value for {date}')
                    response = requests.get(f'https://api.vatcomply.com/rates?date={date}&base=USD')
                    data = response.json()
                    currency_rate = data['rates'][currency]
                    currency_object = Currency(name=currency, date=date, value=currency_rate)
                    currency_object.save()

            currency = Currency.objects.filter(name=currency, date__in=date_list)
            print(currency)
            return render(request, 'currencies/index.html', { 'rates': currency, 'form': form })
    else:
        form = CurrencyForm()
        return render(request, 'currencies/index.html', { 'form': form })

    return render(request, 'currencies/index.html', {'rates': rates})


