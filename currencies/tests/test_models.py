from datetime import datetime
from django.test import TestCase
from ..models import Currency

class CurrencyModelTests(TestCase):
    

    def test_currency(self):
        """
        Test if the currency is created
        """
        
        currency = Currency.objects.create(name='JPY', date='2021-01-01', value=1.00)
        self.assertEqual(currency.name, 'JPY')
        self.assertEqual(currency.date, '2021-01-01')
        self.assertEqual(currency.value, 1.00)
    
    def test_currency_unique(self):
        """
        Test if the currency is unique in the database, if it is, it will not be created and raise an error
        """
        
        currency = Currency.objects.create(name='JPY', date='2021-01-01', value=1.00)
        # raise an error if the currency is not unique
        with self.assertRaises(Exception):
            currency = Currency.objects.create(name='JPY', date='2021-01-01', value=1.00)

    def test_currency_ordering(self):
        """
        Test if the currency is ordered by date
        """
        
        currency = Currency.objects.create(name='JPY', date='2021-01-01', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-02', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-03', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-04', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-05', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-06', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-07', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-08', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-09', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-10', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-11', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-12', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-13', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-14', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-15', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-16', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-17', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-18', value=1.00)
        currency = Currency.objects.create(name='JPY', date='2021-01-19', value=1.00)

        # get the first currency
        currency = Currency.objects.first()
        self.assertEqual(currency.date, datetime.strptime('2021-01-01', '%Y-%m-%d').date())
        # get the last currency
        currency = Currency.objects.last()
        self.assertEqual(currency.date, datetime.strptime('2021-01-19', '%Y-%m-%d').date())

    def test_currency_str(self):
        """
        Test if the currency is returned as a string
        """
        
        currency = Currency.objects.create(name='JPY', date='2021-01-01', value=1.22)
        self.assertEqual(str(currency), 'JPY 2021-01-01 1.22')

    def test_currency_decimal_constraint(self):
        """
        Test if the currency is created with the correct constraints
        """
        
        # raise an error if the digits are more than 10
        with self.assertRaises(Exception):
            currency = Currency.objects.create(name='JPY', date='2021-01-01', value=12345678901.22)

    def test_currency_name_constraint(self):
        """
        Test if the currency is created with the correct constraints
        """
        
        # raise an error if the name is more than 3 characters
        with self.assertRaises(Exception):
            currency = Currency.objects.create(name='JPY1', date='2021-01-01', value=1.22)
        
    def test_currency_date_constraint(self):
        """
        Test if the currency is created with the correct constraints
        """
        
        # raise an error if the date is not in the correct format
        with self.assertRaises(Exception):
            currency = Currency.objects.create(name='JPY', date='2021-01-011', value=1.22)