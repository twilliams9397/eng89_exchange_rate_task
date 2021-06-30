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


