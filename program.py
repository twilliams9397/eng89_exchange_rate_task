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
