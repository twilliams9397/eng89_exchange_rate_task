class CurrencyExchange:

    def show_base(currency_data):
        currency_base = currency_data['base']
        print(f"The base currency for these exchanges is: {currency_base}.")

    def show_list(currency_data):
        currency_list = currency_data['rates']
        for key, value in currency_list.items():
            print(f"{key}: {value}")

    def convert(currency_data, curr1, curr2, amount):
        currency_list = currency_data['rates']
        val1 = currency_list.get(curr1)
        val2 = currency_list.get(curr2) / val1
        rate = val2 / val1
        print(f"You would receive {val1 * rate * amount:.2f} of {curr2}.")


