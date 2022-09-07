from datetime import datetime
from locale import currency
from unicodedata import name
from django.test import TestCase
from ..views import index
from ..models import Currency

class IndexViewTests(TestCase):
        
        def test_index_view(self):
            """
            Test if the index view is created
            """
            
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'currencies/index.html')
            self.assertNotContains(response, 'Hello, world!')

class GetCurrencyViewTests(TestCase):
        
        def test_get_currency_view(self):
            """
            Test if the get_currency view is created and return the currency
            """
            currency = Currency.objects.create(name='JPY', date=datetime.now(), value=1.0)

            response = self.client.get('/currency/JPY')
            self.assertEqual(response.status_code, 200)
            # assert json content response
            self.assertJSONEqual(
                str(response.content, encoding='utf8'),
                [{'date': currency.date.strftime('%Y-%m-%d'), 'value': '1.00'}]
            )
            
        def test_get_currency_view_not_found(self):
            """
            Test if the get_currency view is created and return not found
            """
            response = self.client.get('/currency/JPY')
            self.assertEqual(response.status_code, 404)
            self.assertEqual(
                str(response.content, encoding='utf8'),
                'No data found for JPY'
            )