from app.currency_function import CurrencyExchange  # import functional class
import json
import requests

data = requests.get("http://data.fixer.io/api/latest?access_key=bfdbc73c2b578d60e12df0b369b55bc4")
currency_data = data.json()

CurrencyExchange.show_base(currency_data)
CurrencyExchange.show_list(currency_data)

inp_err = "Invalid input type please try again."
curr_err = "Invalid currency code please try again"

while True:
    curr1 = input("What currency do you have that you would like to exchange? "  # takes user inputs
                  "\nPlease use the currency code e.g. GBP for Great British Pounds.  ").upper()  # ensures that codes match file format
    if not curr1.isdigit():
        if curr1 in currency_data['rates']:
            curr2 = input("What currency would you like to exchange to?  ").upper()
            if not curr2.isdigit():
                if curr2 in currency_data['rates']:
                    amount = input("How much of your currency do you have? "
                                   "\nPlease enter in digits.  ")
                    if amount.isdigit():
                        CurrencyExchange.convert(currency_data, curr1, curr2, amount)
                        break
                    else:
                        print(inp_err)
                else:
                    print(curr_err)
            else:
                print(inp_err)
        else:
            print(curr_err)
    else:
        print(inp_err)

