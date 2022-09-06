from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime
import datetime

from django.core.exceptions import ValidationError
import datetime

def validate_date(value):
    # transform the date to a datetime object
    if value > datetime.date.today():
        raise ValidationError("The start date cannot be in the future")

class MyDateInput(forms.widgets.DateInput):
    input_type = 'date'

class CurrencyForm(forms.Form):
    currency = forms.ChoiceField ( choices = ( ( 'JPY', 'JPY' ), ( 'BRL', 'BRL' ), ('EUR', 'EUR') ), widget = forms.Select ( attrs = { 'onChange' : 'refresh()' } ) )
    start_date = forms.DateField(widget=MyDateInput(attrs = { 'onChange' : 'refresh()', 'class': 'date-fields', 'id': 'start' }), initial=datetime.date.today, validators=[validate_date])
    end_date = forms.DateField(widget=MyDateInput(attrs = { 'onChange' : 'refresh()', 'class': 'date-fields', 'id': 'end' }), initial=datetime.date.today, validators=[validate_date])
