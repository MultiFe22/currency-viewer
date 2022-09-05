from turtle import onclick
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime
import datetime

class MyDateInput(forms.widgets.DateInput):
    input_type = 'date'

class CurrencyForm(forms.Form):
    currency = forms.ChoiceField ( choices = ( ( 'USD', 'USD' ), ( 'BRL', 'BRL' ) ), widget = forms.Select ( attrs = { 'onChange' : 'refresh()' } ) )
    start_date = forms.DateField(widget=MyDateInput())
    end_date = forms.DateField(widget=MyDateInput())
