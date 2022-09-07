from datetime import datetime
from django.test import TestCase
from ..forms import CurrencyForm

class CurrencyFormTests(TestCase):
        
        def test_currency_form(self):
            """
            Test if the currency form is created
            """
            
            form = CurrencyForm(data={'currency': 'JPY', 'start_date': '2021-01-01', 'end_date': '2021-01-02'})
            self.assertTrue(form.is_valid())
        
        def test_currency_form_invalid(self):
            """
            Test if the currency form is invalid when the data is empty
            """
            
            form = CurrencyForm(data={})
            self.assertFalse(form.is_valid())
            self.assertEqual(len(form.errors), 3)
        
        def test_currency_form_invalid_currency(self):
            """
            Test if the currency form is invalid when the currency is empty
            """
            
            form = CurrencyForm(data={'start_date': '2021-01-01', 'end_date': '2021-01-02'})
            self.assertFalse(form.is_valid())
            self.assertEqual(len(form.errors), 1)
        
        def test_currency_form_invalid_start_date(self):
            """
            Test if the currency form is invalid when the start_date is empty
            """
            
            form = CurrencyForm(data={'currency': 'JPY', 'end_date': '2021-01-02'})
            self.assertFalse(form.is_valid())
            self.assertEqual(len(form.errors), 1)
        
        def test_currency_form_invalid_end_date(self):
            """
            Test if the currency form is invalid when the end_date is empty
            """
                
            form = CurrencyForm(data={'currency': 'JPY', 'start_date': '2021-01-01'})
            self.assertFalse(form.is_valid())
            self.assertEqual(len(form.errors), 1)
