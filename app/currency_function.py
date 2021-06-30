class CurrencyExchange:

    def show_base(currency_data):
        currency_base = currency_data['base']
        print(f"The base currency for these exchanges is: {currency_base}.")

    def show_list(currency_data):
        currency_list = currency_data['rates']
        for key, value in currency_list.items():
            print(f"{key}: {value}")

    def convert(currency_data):

