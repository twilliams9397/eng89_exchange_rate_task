# Currency Exchange Task
- create repo for this task
- new package in pycharm
- python package with setup.py
- put .json file in package directory
- python file to calculate/display exchange rates from .json file
- create functions within a class
- read in above .json file and extract data
- print country codes with corresponding rates
###setup.py
```python
from setuptools import setup

# add some information about package
setup(name="Currency Exchange App") # this is required, lines below are optional
version = "1.0"
description = "Python app"
author = "Tom at Sparta Global"
author_email = "twilliams@spartaglobal.com"
url = "http://spartaglobal.com"
```
### currency_function.py - functional class
```python
class CurrencyExchange:

    def show_base(currency_data): # reads in data chosen by user
        currency_base = currency_data['base'] # extracts the base currency value
        print(f"The base currency for these exchanges is: {currency_base}.") # prints this base currency to the user

    def show_list(currency_data):
        currency_list = currency_data['rates'] # extracts the rates dictionary
        for key, value in currency_list.items(): # iterates through dictionary and prints code/rate pairs
            print(f"{key}: {value}")

    def convert(currency_data, curr1, curr2, amount):
        currency_list = currency_data['rates']
        val1 = currency_list.get(curr1) # takes first currency input
        val2 = currency_list.get(curr2)  # takes second currency input
        rate = val2 / val1 # calculates exchange rate between currencies
        print(f"You would receive {rate * amount:.2f} of {curr2}.") # returns amount to user with currency code
```
### program.py - import and use
```python
from app.currency_function import CurrencyExchange # import functional class
import json

data = open("exchange_rates.json", "r") # imports .json file
currency_data = json.load(data) # convert to python dict

CurrencyExchange.show_base(currency_data)
CurrencyExchange.show_list(currency_data)

curr1 = input("What currency do you have that you would like to exchange? " # takes user inputs
              "\nPlease use the currency code e.g. GBP for Great British Pounds.  ").upper() # ensures that codes 
                                                                                             # match file format
curr2 = input("What currency would you like to exchange to?  ").upper()
amount = int(input("How much of your currency do you have? "
                   "\nPlease enter in digits.  "))

CurrencyExchange.convert(currency_data, curr1, curr2, amount)
```